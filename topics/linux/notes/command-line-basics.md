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

## Compiled vs. Interpreted

A program is just a set of instructions that a computer can execute, and an "executable" is just a file that contains a program. The words "program" and "executable" are often used interchangeably. Broadly speaking, there are two types of programs:

- Compiled programs
- Interpreted programs

### Compiled Programs

A compiled program is a program that has been converted from human-readable source code into machine code (binary). Machine code is a set of instructions that a computer can execute directly: your computer's CPU is hardware that's been designed to execute machine code.

Programming languages like Go, C, and Rust produce compiled programs.

### Interpreted Programs

An interpreted program is a program that is executed by another program. The program that executes the interpreted program is called an interpreter. The interpreter reads the source code of the interpreted program and executes it.

Programming languages like Python, Ruby, and JavaScript, are typically interpreted as they run, which means your computer needs to have the interpreter installed to run the program.

Another example is the `.sh` shell script files we talked about. Those are interpreted by the shell program.

### The `which` Command

The `which` command tells you the location of an installed command line program. For example, `which sh` asks for the location of the `sh` (shell) program. On most machines it lives at `/bin/sh`.

If you were to `cat /bin/sh`, you wouldn't see readable text. You'd see a screen full of garbage. That's because your `sh` program is a compiled executable, probably written in C. The raw machine code isn't meant for human eyes.

A file with a `.sh` extension, on the other hand, is a shell script. It's a text file that contains commands that will be interpreted and run by the `sh` program. They are both executable programs, but only one can be run without the help of another program.

## Executables

You're familiar with the idea of reading and writing data into files. But what about executing them? Executable files are just files where the data stored inside is a program that you can run on your computer.

Files with a `.sh` extension are shell scripts. They're just text files that contain shell commands. You can run a file in your shell by typing its filepath:

```bash
mydir/program.sh
```

Interestingly, if the program is in the current directory (in this example, the `mydir` directory), you need to prefix it with `./` to run it:

```bash
./program.sh
```

As far as file paths go, `./program.sh` and `program.sh` are the same. The dot (`.`) is an alias for the current directory. We need the prefix when running executables so that the shell knows we're trying to run a file from a file path, not an installed command like `ls`, `mkdir`, `chmod`, etc.

## Shebang

As we talked about before, you can run any executable file by typing its file path into your shell. For example:

```bash
bin/genids.sh
```

That works out-of-the-box for files that are compiled executables. But what about scripts that need to be interpreted by another program? The computer needs to be told what program to use to interpret the file.

A "shebang" is a special line at the top of a script that tells your shell which program to use to execute the file.

The format of a shebang is:

```
#! interpreter [optional-arg]
```

For example, if your script is a Python script and you want to use Python 3, your shebang might look like this:

```
#!/usr/bin/python3
```

This tells the system to use the Python 3 interpreter located at `/usr/bin/python3` to run the script.

## Bourne Shell

As we talked about before:

- If you're using Ubuntu on WSL, you're probably running a Bash shell.
- If you're using macOS, you're probably running a Zsh shell.
- If you're running a raw Linux installation, I pray you already know what you're using.

To get hand-wavy about it, I want to explain the difference between the 3 shells you're likely to encounter:

- `sh`: The Bourne shell. This is the original Unix shell and is POSIX-compliant. It's very basic and doesn't have many quality-of-life features.
- `bash`: The Bourne Again shell. This is the most popular shell on Linux. It builds on `sh`, but also has a lot of extra features.
- `zsh`: The Z shell. This is the most popular shell on macOS. Like `bash`, it does what `sh` can do, but also has a lot of extra features.

Both `zsh` and `bash` are "sh-compatible" shells, meaning they can run `.sh` scripts, but they also have extra features that generally make them more pleasant to use. For your purposes, the differences between `zsh` and `bash` are not super significant. Everything we do in this course will work in both shells.

## Environment Variables

We talked about how you can create and use local variables in your shell:

```bash
name="Lane"
echo $name
# Lane
```

There is another type of variable called an environment variable. They are available to all programs that you run in your shell.

You can view all of the environment variables that are currently set in your shell with the `env` command.

### Export

To set a variable for your current shell session, use the `export` command (it won't persist if you close the terminal):

```bash
export NAME="Lane"
```

You can then use the variable in your shell, just as before:

```bash
echo $NAME
# Lane
```

The interesting part is that programs and scripts you run in your shell can also use that variable:

For example, if we have a script called `introduce.sh` with the following contents:

```bash
#!/bin/sh
echo "Hi I'm $NAME"
```

We can run it and it will use the `NAME` environment variable we set earlier:

```bash
./introduce.sh
# Hi I'm Lane
```

You can also temporarily set a variable for a single command, instead of exporting it for the whole session.

For example:

```bash
WARN_MESSAGE="this works too" bash worldbanc/private/bin/warn.sh
```

### Unset

You can use the `unset` command to remove an environment variable from your current shell session:

```bash
unset NAME
```

## PATH

This is one of the most important lessons in this entire course! Listen up.

There are environment variables that are sort of "built-in" to your shell. By "built-in" I just mean that different programs and parts of your system know about them and use them. The `PATH` variable is one of those.

### Why Do We Care About the PATH?

If it weren't for the `PATH`, you'd have to remember the filesystem path of every executable you wanted to run in your shell. Instead of just running `ls`, you'd have to run `/bin/ls` (or whatever the location of the `ls` executable is on your system). That's not very convenient.

The `PATH` variable is a list of directories that your shell will look into when you try to run a command. If you type `ls`, your shell will look in each directory listed in your `PATH` variable for an executable called `ls`. If it finds one, it will just run it. If it doesn't, it will give you an error like: "command not found."

### What's in the PATH Variable?

Take a look at your current `PATH` variable:

```bash
echo $PATH
```

You should see a list of directories separated by colons (`:`). Here in the browser, you'll see:

- `/usr/bin`
- `/bin`

Each of those directories is a place where your shell will look for executables. A more realistic `PATH` for your local machine might look like this:

```
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

Which means your shell will use all these directories to look for executables:

- `/usr/local/bin`
- `/usr/bin`
- `/bin`
- `/usr/sbin`
- `/sbin`

## Change Your PATH

A common problem you'll run into when installing programs via the terminal is that after installing, you try to run the program and get an error like this:

```
$ my-new-program
-bash: my-new-program: command not found
```

Nine times out of ten, it's because the program is installed in a directory that's not in your `PATH` variable. Oftentimes when you install a program using the CLI, it will print a message during the installation process that tells you where the executable was installed. Don't let your eyes glaze over when your terminal prints important messages! Sometimes you just gotta rtfm.

To add a directory to your `PATH` without overwriting all of the existing directories, use the `export` command and reference the existing `PATH` variable:

```bash
export PATH="$PATH:/some/new/directory"
```

The `$PATH` part is a reference to the existing `PATH` variable. The `:` separates the existing directories from the new directory that you're adding.

# CH4: Input/Output

## Help

By convention, most production-ready CLI tools have a "help" option that prints information about how to use the tool. It's usually accessed with one of the following:

- `--help` (flag)
- `-h` (flag)
- `help` (first positional argument)

The "help" output is often easier to parse than a full man page. It's usually more of a quick start guide than a full manual.

For example:

```bash
grep --help
```

## Flags

As you've already seen in this course, some commands accept flags. Flags are options that you can pass to a command to change its behavior.

For example, the `ls` command can take a `-l` flag to show a "long" listing of files:

```bash
ls -l
```

Or the `-a` flag to show "all" files, including hidden files:

```bash
ls -a
```

You can also combine flags:

```bash
ls -al
```

### Conventions

Whether or not a command takes flags, and what those flags are, is up to the developer of the command. That said, there are some common conventions:

- Single-character flags are prefixed with a single dash (e.g. `-a`)
- Multi-character flags are prefixed with two dashes (e.g. `--help`)
- Sometimes the same flag can be used with a single dash or two dashes (e.g. `-h` or `--help`)

## Positional Arguments

Programming languages have functions, and functions take arguments. For example, this Python function takes two parameters, `xp` and `level`:

```python
def print_player(xp, level):
    print("Player has", xp, "xp and is level", level)
```

It can then be called with two arguments:

```python
print_player(100, 2)
# Player has 100 xp and is level 2
```

In a shell, commands (programs) can also take arguments. For example, the `cd` command takes a single argument (the directory to change to):

```bash
cd /home/wagslane
```

Other commands might take multiple arguments. For example, the `mv` command takes two arguments: the file to move, and the destination to move it to:

```bash
mv file.txt dest/file.txt
```

## Exit Codes

Exit codes (sometimes called "return codes" or "status codes") are how programs communicate back whether they ran successfully or not.

`0` is the exit code for success. Any other exit code is an error. 9 times out of 10, if a non-zero exit code is returned (meaning an error) it will be `1`, which is the "catch-all" error code.

Programs that call other programs use error codes to figure out if execution was successful. For example, if the Boot.dev server program exits with a non-zero exit code, we have another program that will automatically restart it and log the error.

### Printing Exit Codes

In a shell, you can access the exit code of the last program you ran with the question mark variable (`$?`):

```bash
cat greeting.txt
# General Kenobi!
echo $?
# 0

cat file/that/does/not/exist.txt
echo $?
# 1
```

### Running Commands Conditionally

You can run multiple commands on a single line by separating them with a semicolon (`;`):

```bash
command1 ; command2
```

If you only want the second command to run when the first command succeeds (exit code 0), use `&&`:

```bash
command1 && command2
```

## Standard Output

You might not even know it yet, but you're already a pro at using standard output. You've been using it since you started the first exercise in this course.

"Standard Output", usually called "standard out" or stdout, is the default place where programs print their output. It's just a stream of data that prints to your terminal, but we'll talk later about how it can be redirected to other places.

All programming languages have a simple way to print to stdout. In Python, it's the `print` function:

```python
print("Hello world")
# Hello world
```

In a shell, it's the `echo` command:

```bash
echo "Hello world"
# Hello world
```

## Standard Error

Standard Error, usually called stderr, is a data stream just like standard output, but is intended to be used for error messages.

It's a separate stream so that you can redirect it to a different place if need be, but by default, it prints to your terminal just like stdout.

### Redirecting Streams

You can redirect stdout and stderr to different places using the `>` and `2>` operators. `>` redirects stdout, and `2>` redirects stderr.

### Redirect stdout to a File

```bash
echo "Hello world" > hello.txt
cat hello.txt
# Hello world
```

### Redirect stderr to a File

```bash
cat doesnotexist.txt 2> error.txt
cat error.txt
# cat: doesnotexist.txt: No such file or directory
```

In this example, `cat` is used to intentionally generate an error message (since the file doesn't exist), which is then redirected to `error.txt`.

## Standard In

If there's a standard output, there must be a standard input, right?

"Standard Input", usually called "standard in" or stdin, is the default place where programs read their input. It's just a stream of data that programs can read from as they run.

All major programming languages provide a simple way to read from stdin. In Python, it's the `input` function:

```python
# execution stops until the user types
# something (in this case "Lane") and presses enter
name = input("What is your name? ")

print("Hello,", name)
# Hello, Lane
```

### Redirecting Input

The `<` operator redirects a file into a program's stdin. For example, to feed the contents of a file called `input.txt` into the "word count" program, you can run:

```bash
wc < input.txt
```

This is not the same as:

```bash
wc input.txt
```

In `wc input.txt`, the `wc` program is accepting a filepath string as an argument, and it opens the file itself.

In `wc < input.txt`, the `wc` program doesn't know anything about the file, the file's contents are just being sent to the program's stdin, and it reads from there.

## Piping

One of the most beautiful things about the shell is that you can pipe the output of one program into the input of another program. With this one simple concept, you can run incredibly powerful automation tasks.

### Pipe

The pipe operator is `|`. It's the character that looks like a vertical line. It's usually on the same key as the backslash (`\`) above the enter key. The pipe operator takes the stdout of the program on the left and "pipes" it into the stdin of the program on the right.

```bash
echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w
# 10
```

In the example above, the `echo` command sends "Have you heard the tragedy of Darth Plagueis the Wise?" to stdout.

However, instead of that text being sent to your terminal, the pipe operator pipes it into the `wc` (word count) command. The `wc` command counts the number of words in the input it receives. The `-w` flag tells `wc` to only count words.

This only works because the `wc` command, like most shell commands, can optionally read from stdin instead of a filepath argument.

## Unix Philosophy

The Unix Philosophy is a simple set of principles that have guided the development of Unix-like operating systems for decades. It can be summarized as:

1. Write programs that do one thing and do it well.
2. Write programs to work together.
3. Write programs to handle text streams, because that is a universal interface.

### 1. Write Programs That Do One Thing and Do It Well

This is why programs like `ls`, `grep`, and `less` exist. They do one thing, and they do it well. They don't try to do too much.

- `ls` lists files and directories
- `grep` searches for text
- `less` displays text

### 2. Write Programs to Work Together

Because, at least according to the Unix Philosophy, programs should do one thing and do it well, it's easy to write programs that work together. For example, you can use `grep` to search for text in a file, and then pipe the output of `grep` into `less` to display the results interactively:

```bash
grep "hello" some_file.txt | less
```

### 3. Write Programs to Handle Text Streams, Because That Is a Universal Interface

This point is more the "how" of the previous point. Programs work together easily when they all use the same interface: text streams. A text stream is just a sequence of characters that can be read or written sequentially. In other words, a text stream is just text.

This hearkens back to the point we talked about at the beginning of this course: the shell is a command-line (text) interface. Text-based interfaces are much more powerful and extensible than graphical interfaces. That's why developers have been using them for decades, and why what we can do with them looks like magic to the uninitiated.

# CH5: Local CLI

## Open a Terminal

Everything done so far used boot.dev's in-browser shell. This lesson is about finding the real thing — a terminal on your own machine — since that's where the rest of the course (and real development work) happens.

Where to find it depends on the OS:

- **macOS** — the "Terminal" app, found via Spotlight (the magnifying glass, top-right corner).
- **Windows** — "Command Prompt," found via the Start Menu. A nicer replacement gets installed in the next lesson.
- **Linux** — already home. A sanity-check command works fine here:

  ```bash
  echo "I love the command line"
  ```

## Installing Windows Subsystem for Linux

Skippable on macOS or Linux — both are Unix-like enough for the whole course. Windows' built-in Command Prompt is rough by comparison, so Windows users are steered toward installing **WSL 2** (Windows Subsystem for Linux) with Ubuntu instead.

WSL 2 gives Windows a real Linux OS, filesystem, and command line — no dual-boot needed — while leaving the normal Windows desktop (games, Windows apps, etc.) untouched. It's an official Microsoft product, so it doesn't interfere with the base Windows install.

Two things worth keeping in mind:

- **Version matters** — there are two WSL versions; the course uses the newer **WSL 2**.
- **Separate filesystems** — the WSL 2 filesystem is entirely separate from the Windows filesystem. General rule of thumb: keep games/documents/Windows apps on the Windows side, and put all code on the Linux side.

## Terminal Alternatives

The default terminal that ships with the OS is fine, but other options exist worth knowing about:

- **Editor/IDE built-in terminals** — most developer text editors (VS Code, Zed, Cursor) bundle a terminal. Not recommended for this course specifically, since the extra text-editor features aren't needed here.
- **Ghostty** — a new terminal emulator, fast, feature-rich, and native. Good pick for anyone who likes customizing their setup.
- **Alacritty** — another fast, extensible terminal emulator; the go-to before Ghostty came along.
- **Windows Terminal** — the terminal emulator for Windows. Its default shell can be changed via the "cmd.exe" program settings; when using it with WSL, remember to start WSL each time a new terminal window opens.

## Download Worldbanc

Earlier lessons had the `worldbanc` files pre-loaded into the browser shell. On a local machine, that's no longer automatic — it has to be downloaded for real:

```bash
curl -L https://github.com/bootdotdev/worldbanc/archive/refs/heads/main.zip -o worldbanc.zip
unzip worldbanc.zip
rm worldbanc.zip
mv worldbanc-main worldbanc
```

Step by step:

1. `curl -L ... -o worldbanc.zip` — downloads the file at that URL and saves it locally as `worldbanc.zip`. The `-L` flag tells `curl` to follow redirects (GitHub's archive links redirect before landing on the actual file), and `-o` sets the output filename.
2. `unzip worldbanc.zip` — extracts the archive's contents into a new `worldbanc-main` directory (GitHub zip archives are named `<repo>-<branch>`).
3. `rm worldbanc.zip` — the zip itself is no longer needed once extracted, so it gets cleaned up.
4. `mv worldbanc-main worldbanc` — renames the extracted directory to the shorter, branch-agnostic `worldbanc`.

## Shell Configuration

Bash and Zsh each run a configuration file automatically every time a new shell session starts. These files are the place to set up aliases, functions, and environment variables so they're available in every session, rather than typed fresh each time.

They live in the home directory (`~`) and are hidden by default — filenames starting with `.` don't show up in a plain `ls`. The `-a` flag (seen back in [Flags](#flags)) reveals them:

```bash
ls -a ~
```

- **Bash** — the file to edit is `.bashrc`.
- **Zsh** — the file to edit (creating it if it doesn't exist yet) is `.zshrc`.

## PATH Config

Earlier ([Change Your PATH](#change-your-path)), the `PATH` variable got changed with `export` — but that only lasts for the current shell session. Restart the shell and it resets to default, meaning a tool like `worldbanc.sh` wouldn't be runnable from anywhere without redoing that `export` every single time.

The fix: put that same `export` line in the shell's configuration file (`.bashrc` or `.zshrc`, from the previous lesson) so it runs automatically on every new shell session, permanently.

**Reloading without restarting** — after editing the config file, the changes don't apply to the *current* session automatically (only new ones). Instead of closing and reopening the shell, the `source` command (or its shorthand, `.`) re-runs a file's commands in the current session:

```bash
source ~/.bashrc
```

## Shell Aliases

A shell alias is a command shortcut — useful for shortening commands run all the time.

**Creating an alias** — say `ls -la` gets typed constantly; a shortcut can be made for it:

```bash
alias ll="ls -la"
```

This only lasts for the current shell session — `ll` runs `ls -la` until the shell is closed. Running `alias` with no arguments lists every active alias in the session; passing a specific name (`alias ll`) lists just that one.

**Removing an alias** — `unalias` drops one from the current session:

```bash
unalias ll
```

**Persisting an alias** — same pattern as [PATH Config](#path-config): a temporary `alias` command only survives the current session, so to have it available every time the shell starts, add the `alias` line to the shell's configuration file (`.bashrc` or `.zshrc`).

## Man

`man`, short for "manual," displays the manual page for another program. It only works for programs it has a manual entry for, but that covers most built-in commands and Unix programs. Manuals get more useful as a developer gains experience — they read as less intimidating once there's a habit of actually opening them.

**Using `man`** — pass the command name as an argument. Fittingly, the manual's own manual is a good starting point:

```bash
# open the man pages for the 'man' command
man man
```

**Searching** — man pages are usually opened to look something up, not read start to finish (same `less`-style pager as [More and Less](#27-more-and-less)). Press `/` to search forward (or `?` to search backward), type the search text, and press Enter:

```bash
man ls
# type '/-r' to start searching

# press 'n' to jump to the next result
# press 'N' to go back if you went too far
```

## Symbolic Links

A symbolic link — "symlink" for short — is a special file that points to another file or directory, similar to a shortcut in a GUI. The symlink has its own path, but using it just makes the OS follow the link to whatever it's pointing at.

**The `ln` command** — creates links; the `-s` flag makes it a symbolic one:

```bash
ln -s target_path link_path
```

The target path comes first, then the path where the symlink itself gets created — easy to get backwards. For example:

```bash
ln -s documents/important.txt important.txt
```

This creates a symlink named `important.txt` in the current directory, pointing at `documents/important.txt`.

**Relative vs. absolute target** — a relative target path is resolved from the *symlink's* location, not from wherever `ln` was run. Each has a tradeoff:

- **Absolute path** — the symlink can be moved freely without breaking, but moving the target breaks it.
- **Relative path** — keeps working as long as the symlink's position *relative to* the target stays the same (e.g. moving a parent directory that contains both together is fine).

**Symlinks vs. copies** — a symlink is not a copy. It doesn't duplicate the file's contents, just adds another path pointing at the original:

- Target file changes → the symlink reflects the new contents (there's nothing separate to go stale).
- Symlink deleted → the target file is untouched.
- Target file deleted → the symlink breaks (points at nothing).

`ls -l` reveals where a symlink points:

```
important.txt -> documents/important.txt
```

## Top

`top` shows which programs are using the most resources on the computer — the command-line equivalent of Windows' Task Manager or macOS's Activity Monitor. It's a go-to for diagnosing performance issues, both on a local machine and on remote servers.

## Interrupt

Sometimes a program gets stuck and needs to be stopped. Common causes:

- A typo in the command, so it's not doing what was intended.
- It's trying to reach the internet, but there's no connection.
- It's chewing through too much data to wait out.
- A bug is causing it to hang.

**Ctrl+C** stops the program in these cases — it sends a **SIGINT** ("signal interrupt") telling the program to stop.

## Kill

Sometimes a program is stuck badly enough (or malicious enough) that it ignores SIGINT. The fix then is a separate shell session (a new terminal window) used to manually kill it.

**Syntax:**

```bash
kill <PID>
```

A **PID** ("process ID") is a unique number every running process on the machine gets assigned. The `ps` ("process status") command lists running processes along with their PIDs:

```bash
ps aux
```

`aux` here isn't one flag but three combined — it means "show every process, including ones owned by other users, plus extra detail about each."

# CH6: Permissions

## Users

Unix-like systems support multiple users. Each user has their own home directory, their own files, and their own permissions.

Most machines these days only have one user. It used to be more common for multiple people to share a single computer, or for multiple people to do their work on the same computer over a network.

## Sudo

The `sudo` keyword runs a command as the root "superuser" — short for "superuser do." Using it requires the password of an account with superuser privileges, which is already the case for the only user on a machine.

```bash
sudo some_command
```

**Danger** — `sudo` grants unrestricted access, and can risk damaging the system when used carelessly. Any command should be understood before running it with `sudo`.

## Whoami and Sudo

**The `whoami` command** — prints the user currently logged in:

```bash
whoami
```

Running a command with `sudo` runs it as the root superuser instead, so `whoami` prefixed with `sudo` prints `root` rather than the logged-in user:

```bash
sudo whoami
# root
```

## Permissions

Permissions control who can do what to a given file or directory. They're visually represented as a 10-character string, e.g.:

```
drwxrwxrwx
```

**First character** — whether the entry is a file or a directory:

- `-` — regular file (e.g. `-rwxrwxrwx`)
- `d` — directory (e.g. `drwxrwxrwx`)

**Remaining 9 characters** — three groups of 3, one each for "owner," "group," and "others," in that order. Each group of 3 represents read, write, and execute, in that order:

- `rwx` — all permissions
- `rw-` — read and write, but not execute
- `r-x` — read and execute, but not write

- **Owner** (first 3 characters) — usually the user who created the file or directory, though it can be changed manually.
- **Group** (next 3 characters) — Unix-like systems support groups of users, and each file or directory belongs to exactly one owning group. Not usually a concern outside of system administration.
- **Others** (last 3 characters) — everyone who is neither the owner nor a member of the owning group.

On a personal machine, day-to-day programming work mostly only cares about the "owner" permissions, since that's usually the only user. Full examples:

- `-rwxrwxrwx` — a file where everyone can do everything
- `-rwxr-xr-x` — a file where everyone can read and execute, but only the owner can write
- `drwxr-xr-x` — a directory where everyone can read (`ls` the contents) and execute (`cd` into it), but only the owner can write (modify the contents)
- `drwx------` — a directory where only the owner can read, write, and execute

**Symbolic vs. octal** — the `rwx` string form is the "symbolic" notation; permissions can also be written as a 3-digit "octal" number, one digit per owner/group/others group. For example, an owner with full read/write/execute and group/others with only read+execute is:

- Symbolic: `drwxr-xr-x`
- Octal: `755`

## Changing Permissions

**The `chmod` command** — short for "change mode," changes the permissions of a file or directory:

```bash
chmod u=rwx,g=,o= some_file.txt
```

`u`, `g`, and `o` stand for "user" (owner), "group," and "others." `=` means "set the permissions to the following" — `u=rwx` sets owner permissions to read, write, and execute; `g=` and `o=` (nothing after the `=`) clear group and others permissions entirely.

**Recursive** — the `-R` flag applies the change to a directory and everything inside it:

```bash
chmod -R u=rwx,g=,o= some_directory
```

As with other commands, `.` works as the alias for the current directory (see [2.14](#214-grep-multiple-files)):

```bash
chmod -R u=rwx,g=,o= .
```

## Making a Script Executable

A script that's right there, with no typos, can still refuse to run:

```bash
$ ./conquerworld.sh
bash: ./conquerworld.sh: Permission denied
```

That's a missing execute permission, not a bug in the code. The fix is `chmod +x`, adding the execute bit without having to spell out the full `u=rwx,g=,o=`-style permission set:

```bash
chmod +x conquerworld.sh
./conquerworld.sh
# it works!
```

**Danger** — only make executable (and run) scripts from publishers and authors that are trusted; the internet is a shady place.

## Root User

The "root" user is a superuser with access to everything on the system, able to do anything. Running a command with `sudo` runs it as root (assuming the system hasn't been configured otherwise).

`sudo` is convenient because it quickly grants elevated permissions for a single command, but that same power makes it dangerous — running a command with `sudo` without understanding what it does can cause serious damage.

For example, `rm` with the `r` (recursive) and `f` (force) flags, run against the root directory (`/`), deletes every file on the system:

```bash
sudo rm -rf /
```

Most systems block this by default, but running it with `sudo` bypasses that protection and destroys the system. Some modern systems require an explicit `--no-preserve-root` flag on top of that as an extra safeguard — but reaching for that flag is still a very bad idea.

## Should I Use sudo?

Yes, as long as the command being run is actually understood first. Just be careful.

## Chown

`chmod` only changes permissions on files or directories already owned by the current user. Changing the *owner* of a file or directory not owned by the current user is where `sudo` becomes necessary.

**The `chown` command** — short for "change owner," changes the owner of a file or directory, and requires root privileges:

```bash
sudo chown new_owner some_directory
```

## Using Sudo

Before an exercise involving `sudo`, it's worth sanity-checking the starting state of the file or directory in question — permissions, owner, and which user is currently signed in. **The `ls -l` command** (seen back in [Symbolic Links](#symbolic-links)) is the go-to check for permissions and ownership:

```bash
ls -l worldbanc/private/contacts
```

For example, before an exercise expecting `worldbanc/private/contacts` to be `drwx------`, owned by `root`, and the current user *not* signed in as `root`, `ls -l` confirms all three before proceeding.

# CH7: Editors and Packages

## Package Managers

A package manager is a software tool that helps install other software. Its primary functions:

- Downloading software from official sources
- Installing software
- Updating software
- Removing software
- Managing dependencies

Package managers see frequent use as a developer, as the way to get access to whatever software is needed for the work at hand.

### APT

APT ("Advanced Package Tool") is the primary package manager for Ubuntu — other package managers can be used on Ubuntu too, but APT is the default and most common, and what WSL + Ubuntu setups use.

Checking APT is installed:

```bash
apt --version
```

### Brew

macOS has no "default" package manager; the most popular (unofficial) one is **Homebrew**. Installing it, if not already present:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Using Neovim

Not a full course on Neovim — just enough to edit a file and exit the program. Exiting Vim (or Neovim) without already knowing how is a notorious rite of passage for developers.

## Package Manager Review

APT and Brew aren't the only package managers out there — just two of the most popular, especially on Linux and macOS respectively.

### How Does a Package Manager Work?

Running an install command, e.g. `apt install neovim`, has the package manager:

1. Check whether the package is already installed.
2. If not installed, download the package from a repository.
3. Install the package on the computer.
4. Install any dependencies the package needs to run.
5. Add the package to `PATH` (see [PATH](#path)), if it should be there.

A good package manager also tracks what's installed and at what version, keeping the filesystem tidy rather than accumulating multiple installed copies of the same package.

**Locating an installed package** — `which` (seen back in [The `which` Command](#the-which-command)) shows where the package manager put an executable on the filesystem:

```bash
which nvim
```

## Code Editors

Boot.dev's in-browser editor and a standalone terminal have been the tools so far. Some developers work entirely inside a terminal with a terminal editor like Neovim; many others prefer a hybrid GUI/terminal experience instead.

**Zed** — a fast, lightweight editor, easy to pick up as a beginner but powerful enough for professional use. Recommended for this course.

Inline AI tab completion (e.g. GitHub Copilot) is best left off while still learning to code.

Other popular GUI editors:

- VS Code — the most widely used editor among developers today
- Cursor
- IntelliJ IDEA

Other popular terminal editors:

- Neovim
- Vim
- Emacs