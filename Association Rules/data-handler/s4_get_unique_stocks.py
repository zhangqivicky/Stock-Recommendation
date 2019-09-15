#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step 4: s4_get_target_stocks.py

from pathlib import Path

#Get the list of pages on the first page based on tag url
file = "./../data/co-occurrence_all.txt"
rows = Path(file).read_text().split("\n")
start = 0
end = 10000

stocks = []
for row in rows[start:end]:
	if len(row) > 0:
		stocks = stocks + row.split("\t")
ustocks = set(stocks)
nustocks = []
for stock in ustocks:
	if "." not in stock:
		nustocks.append(stock)
#print(ustocks)
nustocks.sort()
filename = "./../data/unique-stocks.txt"
f = open(filename, 'w')
f.write('\n'.join(nustocks))
f.close()
