#!/usr/bin/env python
"Convert the number of spaces in an indent in a file."
from sys import stdin, argv
import re

if len(argv[1:]) != 2:
  raise ValueError('''You should run me like this.
./change_indent.py 2 4

The first number is the current number of
spaces representing an indent, and the
second is the desired number of spaces.

You gave me %d arguments instead of two.
''' % len(argv[1:]))
else:
  for arg in argv[1:3]:
    try:
      int(arg)
    except:
      raise ValueError('''You should run me like this.
./change_indent.py 2 4

The first number is the current number of
spaces representing an indent, and the
second is the desired number of spaces.

I could not convert "%s" to an integer.
''' % arg)

FROM = int(argv[1])
TO = int(argv[2])
indent_adjustment_factor = TO / FROM

for oldline in stdin.readlines():
  old_indent_length = len(re.findall(r'^[ \t]*', oldline)[0])
  new_indent_length_float = old_indent_length * indent_adjustment_factor
  new_indent_length = int(old_indent_length * indent_adjustment_factor)

  if float(new_indent_length) != new_indent_length_float:
    raise ValueError("This line's indent has a non-round length:\n" + oldline)

  #Consider doing something if it's not a normal indent.
  #if old_indent_length % FROM != 0:

  newline = ' ' * new_indent_length + oldline[old_indent_length:]
  print(newline[:-1]) #Skip the \n at the end.
