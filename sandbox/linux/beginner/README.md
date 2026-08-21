# Beginner

Small, self-contained shell scripts. Each one should be completable in a sitting and target one concept or a tight cluster of them (permissions, piping, find/grep, process management, ...) — no dependency on any other exercise here.

## Ideas

- [ ] File organizer — sorts files into folders by extension/date; loops, conditionals, `mv`
- [ ] Log grep tool — search & filter log files by pattern/date range; `grep`, `awk`, pipes
- [ ] Backup script — archives a directory on demand or on a schedule; `tar`, `cron`, permissions
- [ ] Permissions playground — `chmod` (symbolic and octal), `chown`, deliberately trigger and read a permission-denied error; isolated rehearsal of CH6 before it's one step among six in Homelab Bootstrap
- [ ] Environment inspector — print `$PATH`, set/read a plain shell variable vs. an `export`ed environment variable, temporarily modify `PATH`; nothing else currently touches CH1/CH3's variables and PATH material
- [ ] Package checker/installer — check whether a given package is installed and install it if missing (`which`, `dpkg`/`apt`, or `brew`); isolated rehearsal of CH7 before Homelab Bootstrap step 2
- [ ] File finder & symlink drill — locate files with `find` by name/type/date, create and follow symbolic links, hard vs. soft link basics
- [ ] Process control drill — background a throwaway process (`sleep 100 &`), find it with `ps`/`top`, kill it with `kill`/an interrupt; safe because the target process does nothing but sleep
- [ ] Shell customization drill — add an alias to shell config, confirm a new session picks it up, use `man` to look up a command's docs
- [ ] Exit code / error handling drill — check `$?` after commands, exit non-zero on failure, `&&`/`||` short-circuiting, redirecting stdout vs. stderr separately

## Suggested order

Matches these drills to the course chapter that teaches what each one needs, so review and practice stay paired instead of piling up at the end. Cross-reference: [`topics/linux/notes/command-line-basics.md`](../../../topics/linux/notes/command-line-basics.md).

| After reviewing... | Build |
|---|---|
| CH2 (Filesystem) | File organizer, Log grep tool |
| CH3 (Programs) | Environment inspector (PATH/env vars), Exit code / error handling drill |
| CH4 (Input/Output) | reinforced by Log grep tool (piping) and the exit-code drill (stdout/stderr) — no new build |
| CH5 (Local CLI) | Shell customization drill, Process control drill, File finder & symlink drill (needs CH2's `find` too — do it here once both CH2 and CH5 are covered) |
| CH6 (Permissions) | Permissions playground |
| CH7 (Editors and Packages) | Package checker/installer |
| Synthesis, once the above are done | Backup script — combines `tar`/cron/permissions; good capstone before the intermediate System Health-Check project |
