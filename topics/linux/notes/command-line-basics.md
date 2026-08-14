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

# CH2: The Filesystem

## 2.0 What Is a Filesystem?

All the data on a computer is organized into files and directories, arranged in a tree-like structure called a filesystem.

- **Directories** ("folders" on Windows) are just containers holding files and other directories.
- **Files** are a dump of raw binary data — 1s and 0s. Those bytes can represent anything: text, images, video, whatever.

The tree starts at a single **root directory**. Everything else — files and directories — lives inside it, nested as deep as needed.

Whenever a terminal is open, it's sitting "in" some directory — the **working directory**. Most commonly, that's the home directory.

**Print the working directory**

```bash
pwd
```

`pwd` prints the filepath of the directory the shell is currently in.

## 2.1 Filepaths

The output of `pwd` is a **filepath** — a string describing where a file or directory sits on the filesystem tree.

The leading `/` always represents the root directory, the very top of the tree. Everything after it is a directory name, one level deeper than the last, separated by more `/`s.

Home directory conventions differ by platform:

- **Linux / Windows WSL** — `/home/<username>`, e.g. `/home/wagslane`:

  ```
  root
    └── home
          └── wagslane
  ```

- **macOS** — `/Users/<username>`, e.g. `/Users/wagslane`:

  ```
  root
    └── Users
          └── wagslane
  ```

Both are 2 levels down from root — just a different directory name (`home` vs `Users`) holding the user's folder.

## 2.2 Parent Directories

`cd` ("change directory") moves the shell into a directory. Moving back out uses `..` — a special alias for "the parent directory," letting you step up one level in the tree.

```bash
cd ..
```

Chaining `..` segments with `/` moves up multiple levels at once:

```bash
cd ../..
```

That moves up two directories from the current one.

## 2.3 Absolute vs. Relative Paths

A **relative path** takes the current directory into account — it describes where a file is *relative to* wherever the shell currently sits. Given this structure:

```
vehicles
├── cars
│   ├── fords
│   │   ├── mustang.txt
│   │   └── focus.txt
```

The relative path to `mustang.txt` changes depending on where you're standing:

- From `vehicles`: `cars/fords/mustang.txt`
- From `cars`: `fords/mustang.txt`
- From `fords`: `mustang.txt`

An **absolute path** starts at the filesystem root (`/` on Unix-like systems) instead, so it's the same no matter where the shell currently is:

```
/vehicles/cars/fords/mustang.txt
```

From inside `fords`, both `mustang.txt` (relative) and `/vehicles/cars/fords/mustang.txt` (absolute) point to the same file.

**Which to use** — depends on context:

- Relative paths are shorter and easier to reason about, as long as you know what directory you're in.
- Absolute paths are explicit and unambiguous regardless of current location — useful when the starting directory isn't guaranteed, e.g. giving someone else instructions to find a file.

## 2.4 Files

At their core, files are just blobs of raw data — the bytes can represent anything: text, images, video, whatever.

**The `cat` command** — short for "concatenate" (put things together), used to view a file's contents:

```bash
# Print the contents of a file to the terminal
cat file1.txt

# Concatenate the contents of multiple files and print them to the terminal
cat file1.txt file2.txt
```

The name feels odd for viewing a single file, but makes more sense once you're using it to stitch several files together on output.

## 2.5 Tab Completion

Typing out long paths by hand is slow. Hitting **Tab** while typing a file or directory name asks the shell to autocomplete it.

**Single match** — the rest gets filled in automatically:

```bash
ls w<Tab>
# ls worldbanc/
```

**Multiple matches** — the shell lists the candidates instead of guessing:

```bash
ls worldbanc/p<Tab>
# private public
```

Typing one more distinguishing character and pressing Tab again narrows it down:

```bash
ls worldbanc/pr<Tab>
# ls worldbanc/private/
```

In practice, most path segments only need a few characters typed before Tab resolves them — rarely the full name.

**Beyond paths** — Tab completion also works for command names (typing `cl` + Tab completes to `clear` if it's the only match), and many CLI tools (e.g. `git`) support it for their own subcommands and options, though that often requires enabling a completion script in the shell's config file (covered later).

## 2.6 `head` and `tail`

`cat` dumps a whole file, which isn't great for big files. Two commands print just a slice instead:

**`head`** — prints the first `n` lines, set with the `-n` flag (defaults to 10 if omitted):

```bash
head -n 10 file1.txt
```

**`tail`** — same idea, but the last `n` lines:

```bash
tail -n 10 file1.txt
```

Useful for a CSV: `head -n 6` grabs the header row plus the first 5 data rows in one shot.

## 2.7 More and Less

`more` and `less` are **interactive pagers** — they take over the terminal window so a file can be viewed one page (or line) at a time, instead of dumping everything at once like `cat`.

`less` does everything `more` does plus more (the name is a pun — "less is more"). As a general rule, prefer `less`; only reach for `more` on a system where `less` isn't installed.

**Inside `less`:**

- Spacebar — move down one page
- `b` — move up one page
- `/` — search
- `q` — quit back to the shell prompt

## 2.8 Directories

A directory is just a location in the filesystem that can contain files and other directories — some systems call them "folders," but it's the same concept.

**The `mkdir` command** — "make directory," creates a new directory inside (or relative to) the current one:

```bash
mkdir my_directory
```

## 2.9 Move

**The `mv` command** — moves a file or directory from one location to another. It doubles as "rename" when the destination is just a new name in the same directory. (A directory being moved can't be the current working directory.)

**Rename a file** (same location, new name):

```bash
mv draft.md final.md
```

**Move into a nested directory:**

```bash
mv report.csv archives/report.csv
```

**Move up to the parent directory:**

```bash
mv invoice.pdf ../invoice.pdf
```

**Move without renaming** — omit the filename on the destination, keeping the original name:

```bash
mv photo.png images/
```

Both source and destination are resolved relative to the current working directory (or given as absolute paths) — `pwd` and `ls` are the go-to sanity checks before and after a move, since a wrong destination silently relocates the file rather than erroring.

## 2.10 Remove

**The `rm` command** — deletes a file, or an empty directory:

```bash
rm some_file.txt
```

The `-r` (recursive) flag deletes a directory and everything inside it — files, subdirectories, and their contents, applied again at each level down:

```bash
rm -r some_directory
```

Deleting a non-empty directory without `-r` fails; `-r` is what's needed to remove both a directory and its contents in one go.

## 2.11 Copy

**The `cp` command** — copies a file from one location to another, leaving the original in place:

```bash
cp source_file.txt destination/
```

Copying a directory and all its contents needs the recursive flag:

```bash
cp -R my_dir new_dir
```

On most Linux distros, `-r` and `-R` both mean "recursive" for `cp` and either works — same idea as the `-r` flag on `rm`, just case-insensitive here. Worth being deliberate with `-R` on a directory that recurses into itself (e.g. copying a directory into its own subdirectory) — that can spiral indefinitely.

## 2.12 Home

A user's **home directory** holds their personal files, and is where they land on login. It's the directory to spend most of development time in — e.g. a `workspace` directory inside home, with programming projects as subdirectories of that.

**Danger** — other top-level directories (`/bin`, `/etc`, `/var`, etc.) are critical to the OS or other programs. Working carelessly in them can break the system; home is the safe place to experiment.

**The `$HOME` variable** — an environment variable holding the absolute path to the current user's home directory:

```bash
echo $HOME
```

On macOS this might print `/Users/wagslane`; on Linux, `/home/wagslane`.

**The `~` alias** — shorthand for the home directory, so `cd ~` gets there without typing out `cd $HOME` or the full absolute path.

## 2.13 Grep

**The `grep` command** — searches for text in files, the CLI equivalent of a GUI's Ctrl+F/Cmd+F.

```bash
grep "hello" words.txt
```

Prints every line in `words.txt` containing `hello`. The search is case-sensitive by default — this matches `hello` but not `Hello` or `HELLO`.

## 2.14 `grep` Multiple Files

**Multiple files at once** — list them all after the search term:

```bash
grep "hello" hello.txt hello2.txt
```

**Recursive search** — the `-r` flag searches a whole directory, including all subdirectories:

```bash
grep -r "hello" .
```

`.` is a special alias for the current directory — the same directory-alias pattern as `..` for the parent (see [2.2](#22-parent-directories)).

## 2.15 Find

**The `find` command** — locates files and directories by *name*, not by contents (that's `grep`'s job).

**Exact name:**

```bash
find some_directory -name hello.txt
```

**Pattern search** — `*` is a wildcard matching anything, so it works for extensions or substrings:

```bash
# Every file ending in .txt
find some_directory -name "*.txt"

# Every filename containing "chad"
find some_directory -name "*chad*"
```
# CH3: Programs