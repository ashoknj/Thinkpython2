from __future__ import print_function, division


"""
Write a function called sed that takes as arguments a pattern string, a replacement string,
and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should
catch the exception, print an error message, and exit
"""
"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    pattern = 'how'
    replace = 'cow'
    source = 'Chapter14/sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()
