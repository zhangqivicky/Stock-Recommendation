#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step5: s5_preprocess_occurrence.py

from pathlib import Path
import csv

rownum = 0
colnum = 0
file = "./../data/co-occurrence_all.txt"
rows = Path(file).read_text().split("\n")
rows_new = []
for row in rows:
	if len(row) > 0:
		stocks = row.split("\t")
		vlstocks = []
		for stock in stocks:
			if "." not in stock:
				vlstocks.append(stock)
		if len(vlstocks) >0 :
			rownum += 1
			rows_new.append(vlstocks)
			if len(vlstocks) > colnum:
				colnum = len(vlstocks)

print("Row number: " + str(rownum))
print("Colume number: " + str(colnum))

with open('./../data/preprocessed-cooccurrence.csv', mode='w') as occurrence_file:
	ooccurrence_writer = csv.writer(occurrence_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	# write header to csv
	header = list(range(0, colnum))
	ooccurrence_writer.writerow(header)	
	for row_new in rows_new:
		ooccurrence_writer.writerow(row_new)