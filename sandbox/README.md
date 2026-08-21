# Sandbox

Where fundamentals stop being facts I can recognize and start being muscle memory.

[`topics/`](../topics/) distills concepts from specific external resources — it's what I studied. This is different: self-designed, code-first challenges. The goal isn't "I can follow this," it's "I can build this, explain this, and still remember it in a year."

## How it's organized

Each topic (`python/`, `linux/`, ...) is split into three tiers, mirroring how a cert track builds up:

| Tier | What goes here | Shape |
|---|---|---|
| `beginner/` | Small, isolated exercises — one concept or a tight cluster of them, done in an afternoon. | Toy projects for a language (calculator, quiz, tic-tac-toe); scripted drills for something like Linux. |
| `intermediate/` | A smaller real project that chains a few concepts together, short of a full capstone. | One self-contained project. |
| `advanced/` | A single evolving project that forces reuse of everything earlier, built incrementally over many sessions. | One project, grown over time (e.g. the Party Manager). |

New topic → copy [`_template/`](_template/) and start with `beginner/`. Don't pre-build all three tiers for a topic before starting it — the skeleton exists so the pattern is consistent when you get there, not so every topic has empty folders waiting.

## Topics

- [Python](python/)
- [Linux](linux/)
