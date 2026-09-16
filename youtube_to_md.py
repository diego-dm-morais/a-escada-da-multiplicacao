#!/usr/bin/env python3
"""Convert a YouTube video into a Markdown document with metadata and transcript."""

import argparse
import re
import sys
import tempfile
from pathlib import Path

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url: str) -> str:
    patterns = [
        r"(?:v=|/)([0-9A-Za-z_-]{11}).*",
        r"(?:youtu\.be/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video id from: {url}")


def fetch_metadata(url: str) -> dict:
    opts = {"quiet": True, "skip_download": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def fetch_transcript(video_id: str) -> list[dict]:
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=["pt", "pt-BR", "en"])
    return fetched.to_raw_data()


def transcribe_audio(url: str) -> list[dict]:
    """Fallback: download audio and transcribe locally with faster-whisper."""
    from faster_whisper import WhisperModel

    print("No captions available, downloading audio for local transcription...", file=sys.stderr)
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = str(Path(tmpdir) / "audio.%(ext)s")
        opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio/best",
            "outtmpl": audio_path,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])

        mp3_path = Path(tmpdir) / "audio.mp3"
        print("Transcribing audio (faster-whisper, this may take a while)...", file=sys.stderr)
        model = WhisperModel("small", device="cpu", compute_type="int8")
        segments, _info = model.transcribe(str(mp3_path), language=None, vad_filter=True)
        return [{"text": segment.text} for segment in segments]


def slugify(title: str) -> str:
    text = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE).strip()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:150] or "video"


def build_markdown(info: dict, transcript: list[dict], url: str) -> str:
    title = info.get("title", "Untitled")
    channel = info.get("uploader", "Unknown")

    full_text = " ".join(
        entry["text"].replace("\n", " ").strip() for entry in transcript
    )
    full_text = re.sub(r"\s+", " ", full_text).strip()

    lines = [
        f"# {title}",
        "",
        f"- **URL:** {url}",
        f"- **Channel:** {channel}",
        "",
        "## Resumo",
        "",
        "_(preencher)_",
        "",
        "## Texto completo",
        "",
        full_text,
        "",
        "## Conclusão",
        "",
        "_(preencher)_",
        "",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Convert a YouTube video into Markdown.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", help="Output .md path (default: <video_id>.md)")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    print(f"Fetching metadata for {video_id}...", file=sys.stderr)
    info = fetch_metadata(args.url)

    print("Fetching transcript...", file=sys.stderr)
    try:
        transcript = fetch_transcript(video_id)
    except (TranscriptsDisabled, NoTranscriptFound):
        transcript = transcribe_audio(args.url)

    markdown = build_markdown(info, transcript, args.url)

    out_dir = Path("content/youtube")
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = Path(args.output) if args.output else out_dir / f"{slugify(info.get('title', video_id))}.md"
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Saved: {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
