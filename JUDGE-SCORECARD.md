# Judge scorecard — post-x-the-agent-builds-a-game-from-20261122-1709

Brief (from RULES.txt): show the prompt, the agent working, and the finished game in one short clip; keep it moving; show the real result; end on the game running with the call to come build on make.fun. Ranking is post engagement (views + 10x interactions), so the hook must read in the first seconds.

Criteria scored 0-2 each, in brief order:
1. Prompt unmistakably visible (one prompt, readable on screen)
2. Agent visibly working (code/build shown, not claimed)
3. Finished game visibly played (real result, not a mock)
4. Keeps moving (no dead frames; motion in every segment)
5. Ends on the game running + CTA to build on make.fun

| # | Concept + one-prompt | Hook for the video | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---|---|---|
| 1 | SNAKE PROTOCOL — neon snake that plays itself when idle, speeds up every 5 apples | "I gave my AI one prompt. It built a snake that plays itself." | 2 | 2 | 2 | 2 | 2 | 10 |
| 2 | FLAPPY BYTE — flappy where the bird is a terminal cursor dodging code brackets | Cursor flaps through `[]{}()` gates | 2 | 2 | 2 | 2 | 1 | 9 |
| 3 | BRICK BREAKER 9000 — breakout where bricks are commit messages | Paddle smashes `fix:`, `feat:`, `wip` bricks | 2 | 2 | 2 | 1 | 2 | 9 |
| 4 | BUG DODGER — endless runner, robot dodges bugs, collects USDC coins | Robot hops bugs, grabs coins | 2 | 1 | 2 | 2 | 2 | 9 |
| 5 | PONG: AGENT vs HUMAN — pong against an AI paddle | "Can you beat the agent that wrote this?" | 2 | 2 | 1 | 2 | 2 | 9 |
| 6 | MEMORY//MATCH — memory cards about agent tools | Flip cards: terminal, wallet, bundle | 2 | 1 | 1 | 0 | 1 | 5 |
| 7 | TYPE RACER — out-type an AI agent | Race the agent's WPM live | 2 | 1 | 1 | 1 | 1 | 6 |

## Pick: #1 SNAKE PROTOCOL

- Wins C3/C4 outright: the auto-demo AI drives the snake on load, so the "finished game" segment is real continuous gameplay with zero input — no mock, no dead frames, and it survives the end-card overlay still running underneath.
- C1: the prompt is short enough to show verbatim on screen: "Build me a neon snake game that plays itself when I'm idle and speeds up every 5 apples — one file, no libraries."
- C2: single-file canvas game means the code segment can show real lines being written (snake step, AI pathing, speed tiers) that map 1:1 to what then runs.
- C5: game keeps running under the referral end card; CTA line over live gameplay before the card.
- Rejected: memory match (static cards kill C4), type racer (needs a human typist for C3), pong (ball alone reads thin at small size).

Entry title: "SNAKE PROTOCOL — neon snake that plays itself when idle, built from one prompt"
