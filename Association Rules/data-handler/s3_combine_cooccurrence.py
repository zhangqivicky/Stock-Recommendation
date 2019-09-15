#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step 3: s3_combine_occurrence.py

from pathlib import Path

rows = []
for x in range(0, 10):
	start = x * 1000
	end = ( x + 1) * 1000
	file = "./../data/co-occurrence_" + str(start) + "-" + str(end) + ".txt"
	rows = rows + Path(file).read_text().split("\n")

filename = "./../data/co-occurrence_all.txt"
f = open(filename, 'w')
f.write('\n'.join(rows))
f.close()
