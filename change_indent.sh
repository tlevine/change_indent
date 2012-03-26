#!/bin/bash

# From this many indents to this many indents
from=$1
to=$2

# Check numberness
for var in $from $to; do
  case $var in
    [24]) ;;
    *) echo You should run me like this.
       echo ./change_indent.sh 2 4
       echo
       echo The first number is the current number of
       echo spaces representing an indent, and the
       echo second is the desired number of spaces.
       echo
       echo The numbers 2 and 4 are currently supported.
       echo $var is not \"2\" or \"4\".
       exit 1;;
  esac
done

if [ $from -eq $to ]; then
  cat
elif [ $from -eq 2 ]; then
  sed "s/\(^[ ]*\)\([^ ]\)/\1\1\2/"
elif [ $from -eq 4 ]; then
  echo Converting 4-space indents to 2-space indents isn\'t supported yet.
  exit 1
fi
