# Linux

**Resources used:** boot.dev
**Cert status:** —

## Key takeaways

- The shell reads, evaluates, prints, and loops (REPL); `PATH` is the list of directories it searches to resolve a bare command name.
- Everything is a file in a tree rooted at `/`; permissions (`rwx` for owner/group/others, or octal) gate what each user can do to it, and `sudo` temporarily elevates to root for the rest.
- Package managers (APT, Brew, ...) handle downloading, installing, updating, and removing software plus its dependencies, keeping the filesystem from accumulating duplicate installs.

## Notes

- [Command line basics](notes/command-line-basics.md)
