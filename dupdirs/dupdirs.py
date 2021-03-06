#!/usr/bin/env python

import sys
import os
import getopt


def usage():
    print """Usage: dupdirs <dir1> <dir2>

Prints all those directories from <dir1> that are also present in <dir2>. That
is, a directory of the same name is present in <dir2>.

Options:
    -f  Enable fuzzy string comparison
    -m  Minimum score for fuzzy search (only relevant if -f is given)
    -h  Show this help
"""


def _is_directory(d):
    return os.path.exists(d) and os.path.isdir(d)


def subdir_list(d):
    entries = os.listdir(d)
    entries.sort()
    return entries


def subdir_dict(d):
    entries = subdir_list(d)
    result = {}
    for e in entries:
        result[e] = True
    return result


def regularComparison(dir1, dir2):
    result = []
    subdirs1 = subdir_list(dir1)
    subdirs2 = subdir_dict(dir2)
    for d in subdirs1:
        if d in subdirs2:
            result.append(d)
    return result


def fuzzyComparison(dir1, dir2, minScore):

    try:
        import fuzzywuzzy.process
        import fuzzywuzzy.fuzz
    except ImportError:
        print "This program requires the fuzzywuzzy package. Aborting."
        sys.exit(1)

    movies = subdir_list(dir1)
    choices = subdir_list(dir2)

    result = {}

    for m in movies:
        match = fuzzywuzzy.process.extractOne(
                m, choices, scorer=fuzzywuzzy.fuzz.token_set_ratio
                )
        if match is None:
            continue
        else:
            (name, score) = match
            if score >= minScore:
                result[m] = name

    return result


def main():

    (args, config) = parse_options(sys.argv[1:])

    if len(args) != 2:
        usage()
        sys.exit(1)

    (dir1, dir2) = args

    if not _is_directory(dir1):
        print dir1 + " is not a valid directory, stopping."
        sys.exit(1)

    if not _is_directory(dir2):
        print dir2 + " is not a valid directory, stopping."
        sys.exit(1)

    if config['fuzzy']:
        dups = fuzzyComparison(dir1, dir2, config['minScore'])
        for key, val in dups.items():
            print key
            print "\t-> " + val
    else:
        dups = regularComparison(dir1, dir2)
        for d in dups:
            print d


def parse_options(args):
    opts, args = getopt.getopt(args, "hfm:")
    config = {
            'fuzzy': False,
            'minScore': 80
            }

    for opt, val in opts:
        if opt == "-h":
            usage()
            sys.exit()
        elif opt == "-f":
            config['fuzzy'] = True
        elif opt == "-m":
            try:
                config['minScore'] = int(val)
            except ValueError:
                print "Invalid value for minimum score: %s, ignored." % val

    return (args, config)


if __name__ == "__main__":
    main()
