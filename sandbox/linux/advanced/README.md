# Advanced

One evolving automation project, grown incrementally over many sessions. Each step builds on and reuses what the previous steps already established — no clean slate, no throwaway scripts.

## Homelab Bootstrap Script

A script suite that provisions a server from a bare install, growing step by step — same shape as the Python Party Manager, sysadmin-flavored instead of RPG-flavored.

1. Create a non-root user, set up SSH key access, lock down permissions
2. Install a baseline package set via the system package manager
3. Deploy and manage config files (dotfiles, service configs)
4. Add cron-scheduled backups
5. Add log monitoring / alerting for error patterns
6. (later) Tie it all together into one idempotent bootstrap script

Steps beyond this outline aren't fixed yet — extend this list as it grows, the same way the Party Manager's day list did.
