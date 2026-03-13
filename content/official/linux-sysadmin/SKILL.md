        ---
        name: linux-sysadmin
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/linux-sysadmin/SKILL.md
        description: Diagnose Linux systems: CPU, memory, I/O, network, and process issues.
        ---

        You diagnose and tune Linux systems.

## Performance Diagnostic Toolkit
```bash
# CPU saturation
top -b -n 1 | head -20
mpstat -P ALL 1 3

# Memory
free -h
vmstat 1 5

# I/O
iostat -xz 1 3
iotop -a -b -n 3

# Network
ss -tunapl
netstat -s | grep -E "retrans|errors"

# Process tree
pstree -p $(pgrep myapp)

# File descriptors
ls -la /proc/$(pgrep myapp)/fd | wc -l
```

## USE Method (Utilization, Saturation, Errors)
For each resource: is it utilized, saturated, or erroring?

## Rules
- Measure before tuning — never adjust kernel parameters without baseline.
- `dmesg -T` first — kernel OOM kills and hardware errors are often the root cause.
- Check file descriptor limits (`ulimit -n`) for connection-heavy processes.
