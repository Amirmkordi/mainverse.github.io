
# Connect Four — ANSI + Drop Animation + Strong AI (Java CLI)

A simple, polished Connect Four you play in your terminal. It looks nice (colors, animation),
and the computer player is strong (Iterative Deepening + **PVS/Negascout** + **LMR** + Transposition Table).

- **Human:** `X▲` (yellow)
- **AI:** `O●` (cyan)

> Works on macOS, Windows, and Linux. Requires **Java 11+**.

---

## Quick Start (super simple)

### Option A — Double‑click (recommended)
- **macOS:** double‑click `Launch-Mac.command`  
  If macOS blocks it, right‑click → **Open** → continue.
- **Windows:** double‑click `Launch-Windows.bat`

These launchers will **compile** the game if needed and run it with good defaults.

### Option B — Manual (Terminal / CMD / PowerShell)
```bash
javac ConnectFourCLI.java
java ConnectFourCLI --time 12 --ai-first true --ansi true --anim true --anim-delay 40
```

If colors look odd, add `--ansi false`. If animation feels slow, use `--anim false`.

---

## How to Play (for absolute beginners)

1. **Goal:** make a line of **4** of your own pieces before the computer does.  
   Lines can be **horizontal**, **vertical**, or **diagonal**.

2. **Your piece:** `X▲` (yellow). **Computer’s piece:** `O●` (cyan).  
   Shapes + letters make it easy to tell them apart.

3. **Your turn:** look at the numbers printed under the board: `1  2  3  ...`  
   Type a **number** and press **Enter** to drop your piece in that column.

4. **What happens:** the piece **falls** to the lowest empty spot in that column (you’ll see it drop).

5. **Computer turn:** it thinks for a bit (based on the time setting), then plays.

6. **Mistake?** Type `u` and press Enter to **undo** your last move (and the AI’s reply).

7. **Game end:** someone connects 4, or the board fills up (draw). You can type `new` to play again.

**That’s it.** You only need to type a column number each turn. Everything else is optional.

---

## Controls (any time during the game)

- `1..W` — drop in that column (W = number of columns, default 7)
- `u` or `undo` — undo your last move (and AI’s move if present)
- `auto [n]` — watch the AI play itself for `n` half‑moves (default 1)
- `new` — start a fresh game
- `time S` — set seconds per AI move (e.g., `time 15`)
- `depth N` — fixed search depth (use when `--time 0`)
- `help` — show help
- `q` — quit

---

## Settings you might care about

- **Strength via time (recommended):** `--time 12` means the AI thinks for ~12s per move.  
  Stronger play? Try `--time 15` or `--time 20`.
- **Fixed depth (deterministic):** `--time 0 --depth 20`
- **Board size:** `--rows 6 --cols 7` (classic), can increase width/height a bit
- **Who starts:** `--ai-first true|false`
- **Look & feel:** `--ansi true|false`, `--anim true|false`, `--anim-delay 0..500`

**Examples**
```bash
# Human starts, responsive AI
java ConnectFourCLI --time 5 --ai-first false

# Maximum strength (fixed depth)
java ConnectFourCLI --time 0 --depth 20

# Bigger board, slower thoughtful AI
java ConnectFourCLI --rows 6 --cols 9 --time 15
```

---

## Troubleshooting

- **Colors weird on Windows?** Try `--ansi false` or run in Windows Terminal.
- **macOS says the launcher can't be opened?** Right‑click → **Open** once, or run:
  ```bash
  chmod +x Launch-Mac.command
  ```
- **Compiler errors?** Check Java version:
  ```bash
  java -version
  javac -version
  ```
  Needs **Java 11 or newer**.

---

## What’s included

- `ConnectFourCLI.java` — the whole game (engine, rules, renderer, CLI)
- `Launch-Mac.command` — macOS launcher (compiles then runs)
- `Launch-Windows.bat` — Windows launcher (compiles then runs)
- `LICENSE` — MIT License
- `README.md` — this guide

---

## License

This project is released under the **MIT License**. See `LICENSE` for details.

Built with ❤️ for the terminal. No external libraries. Pure Java.
