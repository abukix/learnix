# Intermediate

One smaller real project — chains a handful of concepts together, built in one continuous push rather than day-by-day like the advanced tier.

## System Health-Check Script

One shell script that reports on system state in a single pass: disk usage, memory usage, uptime, and the top few processes by resource use.

- Pipe/filter command output (`df`, `free`, `ps`, `uptime`) into a clean, formatted report
- Conditionals to flag anything over a threshold (e.g. disk >80% full)
- Optionally write the report to a timestamped log file

Concepts exercised: piping, `grep`/`awk`/`sed`, conditionals, redirection.
