---
topic: Linux
source: boot.dev
date: 2026-08-11
status: seed   # seed | growing | evergreen
---

# CH1: The Command Line

## 1.0 Welcome to Learn Linux

Admittedly, the course name is a bit of a misnomer. It's called "Learn Linux" because "Linux" is what most students think of regarding the concepts in this course. A more accurate title might be "Learn to use shells and terminals in a Unix-like environment," but that's a mouthful.

**Learning goals**

- Understand the difference between a shell and a terminal
- Learn how to navigate and use the file system using the command line
- Learn how to install software using the command line
- Understand how to manage your PATH and environment variables
- Learn how to manage permissions and execute programs

This course will get you comfortable working on a command line, which is a skill that's going to be critical for the rest of your career as a programmer. So, instead of writing code in the browser, in this course you'll interact with a command line interface (CLI).

For the first part of the course, you don't even need to leave the page — boot.dev embeds a real, working shell right in the browser. Later, once comfortable, everything gets set up on your own machine.

## 1.1 What Is a Terminal?

The terms "shell," "CLI," and "terminal" are often used interchangeably to refer to the same thing: a program for issuing text-based commands.

But to get pedantic, the "terminal" is just one specific part of that program. Historically, the word "terminal" meant a physical device you could type commands into — essentially a keyboard and a screen.

These days, when we say "terminal," we really mean "terminal emulator." A terminal emulator is a program that emulates a physical terminal, letting you type commands into a window on your computer.

Which commands you're able to use isn't determined by the terminal emulator, but by the shell (covered later). The terminal emulator is just responsible for drawing text on the screen and processing your keystrokes.

## 1.2 What Is a Shell?

If the terminal is just the program that lets you type commands and displays their output, something else has to actually run those commands. That something is the shell.

Shells do a lot of things, but their main job is to interpret the commands you type and execute them.

**REPL**

Shells are often called "REPLs." REPL stands for:

- **R**ead
- **E**val (evaluate)
- **P**rint
- **L**oop

In other words, a shell is a program that:

1. Reads the command you type
2. Evaluates it, usually by running another program on your computer
3. Prints the output of that command
4. Gives you a new prompt so you can repeat the cycle

## 1.3 Command Line vs. GUI

In other courses, code often gets run by clicking a "Run" button. In real development work, code is more often run from a command line interface (CLI) instead — e.g. running a Python file with `python main.py`.

**What's a CLI?**

"Terminal," "shell," "command line," "CLI," and "command prompt" get used interchangeably (despite some technical differences) to mean the same general thing: a program that lets you interact with your computer in a text-based way.

**What's a GUI?**

A graphical user interface (GUI) is the mouse-and-icons style of interaction most people are used to — clicking buttons, menus, and icons. GUIs are generally easier to learn since you can just point at things. But they have real drawbacks compared to a CLI:

- **Weaker** — a GUI only exposes the options its developer chose to build; a CLI gives far more direct control over the computer.
- **Slower** — once you know the commands, typing them beats clicking through menus.
- **Less reproducible** — commands can be copy-pasted as exact instructions, with no dependency on screen size or UI layout.
- **Not automatable** — it's easy to write code that manipulates text, much harder to write code that manipulates a GUI.

## 1.4 Variables

Once working on a local machine, the shell in play depends on the OS:

- Ubuntu on WSL → probably Bash
- macOS → probably Zsh
- Full Linux → whatever was chosen at setup

For this course, Bash and Zsh are treated as basically interchangeable. The in-browser shell is an in-memory Bash shell (or as close as a browser can get).

Both Bash and Zsh are shells, but they're also full programming languages — variables, functions, loops, and more. In practice though, shell languages are optimized for running other programs and writing small scripts, not for building large applications.

**Creating a variable**

```bash
name="Lane"
```

No spaces around the `=` — `name`, the assignment operator, and `"Lane"` sit right next to each other.

**Using a variable**

```bash
$ echo $name
Lane
```

(The `$` at the start of the line is just the prompt convention, not something to type — the actual command is `echo $name`.)

Unlike Python, where a bare variable name works, the shell needs a `$` prefix to read a variable's value — otherwise it treats it as a literal string.

**Interpolating a variable in a string**

```bash
$ echo Hello $name
Hello Lane
```

## 1.5 History

In a REPL, it's useful to see commands typed in the past — to re-run them, or copy them into a script. The `history` command prints that history.

```bash
history
```

## 1.6 Navigate History

Retyping a command you already ran is a waste of keystrokes. Two shortcuts help:

**Arrow keys** — ↑ walks backward through command history one entry at a time; ↓ walks forward again once you've gone back too far. Arrow up to the command, hit Enter, done.

**Clear** — `clear` (or Ctrl+L) wipes the visible screen when it gets cluttered. It doesn't touch history, just the display.
