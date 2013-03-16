#!/bin/bash
echo "DB-Backup:" $(date) | mutt -a "/home/j12d/timetracker/times.db" -s [Backup] -- juliandebus@me.com alexanderschilbach@googlemail.com
