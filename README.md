These scripts convert indentation size. Use them like so

    cat change_indent.py|./change_indent.py 2 4

They take two arguments. The first is the original indent size (number of spaces),
and the second is the future indent size. A tab is treated as one space.

The conversion is quite forceful, so it migth do some things you don't want it to.