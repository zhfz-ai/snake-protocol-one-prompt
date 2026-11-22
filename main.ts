// SNAKE PROTOCOL entrypoint (Node 22, stdlib only): copy POST.json to /output.
// The entry is the X post itself; this program only hands its address to the grader.
import { copyFileSync, mkdirSync, chmodSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
// Outside the grader, MAKEFUN_BOT_DIR / MAKEFUN_OUTPUT_DIR stand in for /bot and /output.

mkdirSync(outputDir, { recursive: true });
chmodSync(outputDir, 0o755);
const sourcePath = join(botDir, 'POST.json');
const targetPath = join(outputDir, 'POST.json');
copyFileSync(sourcePath, targetPath);
chmodSync(targetPath, 0o644);
console.log(`POST.json copied to ${targetPath}`);
