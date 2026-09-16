#!/usr/bin/env node
// Converte um .html (mind-map) em .png de alta resolução, pronto pra WhatsApp.
// Uso: node scripts/html-to-png.mjs <arquivo.html> [saida.png]

import { chromium } from "playwright";
import path from "node:path";
import fs from "node:fs";

const [, , inputArg, outputArg] = process.argv;

if (!inputArg) {
  console.error("Uso: node scripts/html-to-png.mjs <arquivo.html> [saida.png]");
  process.exit(1);
}

const inputPath = path.resolve(inputArg);
if (!fs.existsSync(inputPath)) {
  console.error(`Arquivo não encontrado: ${inputPath}`);
  process.exit(1);
}

const outputPath = path.resolve(outputArg || inputPath.replace(/\.html$/i, ".png"));
fs.mkdirSync(path.dirname(outputPath), { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 1080, height: 1080 },
  deviceScaleFactor: 3, // resolução máxima (~3x), nítido no WhatsApp
});

await page.goto(`file://${inputPath}`, { waitUntil: "networkidle" });
// espera fontes carregarem antes do print
await page.evaluate(() => document.fonts.ready);

await page.screenshot({ path: outputPath, fullPage: true });
await browser.close();

console.log(`PNG salvo em: ${outputPath}`);
