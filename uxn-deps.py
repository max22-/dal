#!/usr/bin/env python3

# A little bit overkill, or useless :)
# TODO: rewrite it in uxntal

import sys

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} file.tal")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

deps = []

for l in lines:
    if l[0] == "~":
        deps.append(l[1:].strip())

deps_file = sys.argv[1][0:-4] + ".d"
with open(deps_file, "w") as f:
    f.write(f"{sys.argv[1]}: ")
    f.write(" ".join(deps))
