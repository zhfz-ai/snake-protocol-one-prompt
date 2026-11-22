// SNAKE PROTOCOL entrypoint (Node 22, stdlib only): copy POST.json to /output.
// The entry is the X post itself; this program only hands its address to the grader.
import { copyFileSync, mkdirSync, chmodSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
// Outside the grader, MAKEFUN_BOT_DIR / MAKEFUN_OUTPUT_DIR stand in for /bot and /output.

mkdirSync(outputDir, { recursive: true });
// Best-effort only: in the grader sandbox /output is owned by another user,
// so chmod can throw PermissionError. Never let that fail the run.
try {
  chmodSync(outputDir, 0o755);
} catch {
  // ignore: permissions are advisory here
}
const sourcePath = join(botDir, 'POST.json');
const targetPath = join(outputDir, 'POST.json');
copyFileSync(sourcePath, targetPath);
try {
  chmodSync(targetPath, 0o644);
} catch {
  // ignore: permissions are advisory here
}
console.log(`POST.json copied to ${targetPath}`);
