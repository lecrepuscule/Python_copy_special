#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  filenames = os.listdir(dir)
  abs_path = os.path.abspath(dir)
  special_paths = []
  for filename in filenames:
    if re.search(r"__\w+__", filename):
      special_paths.append(os.path.join(abs_path, filename))
      print os.path.join(abs_path, filename)
  return special_paths

def copy_to(paths, dir):
  abs_path = os.path.abspath(dir)
  if not os.path.exists(abs_path):
    os.makedirs(abs_path)
  for path in paths:
    shutil.copy(path, abs_path)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir:
    special_paths = get_special_paths(args[0])
    copy_to(special_paths, todir)
  # elif tozip:
  else:
    print "output is: " + str(get_special_paths(args[0]))
  
if __name__ == "__main__":
  main()
