#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step 2: s2_get_cooccurrence.py

import requests
import time
import re
import random
from bs4 import BeautifulSoup
from pathlib import Path

class OccurrenceRetriever:
	# Crawler of page webpage
	def __init__(self, file, start, end):
		self.pageurls = []
		self.occurrences = []
		self.file = file
		self.start = start
		self.end = end

	# Parse stock symbols from news article
	def StockParser(self, url):
		stock_list = []
		html = requests.get(url) #Get the content of page webpage by url
		bsoup = BeautifulSoup(html.text.encode("utf-8"), "lxml")
		body_soup = bsoup.find('div', {'class':'article-body'})
		#print(body_soup)
		for stock in body_soup.findAll('a', {'href':re.compile('https://www.investopedia.com/markets/stocks/*')}):
			matchObj = re.search( r'markets/stocks/(.*?)/', stock.get('href'), re.M|re.I)
			if matchObj:
				stock_list.append(matchObj.group(1))
		return stock_list

	# Start to retrieve
	def run(self):

		# Get the urls of all news articles
		self.pageurls = Path(self.file).read_text().split("\n")
		self.pageurls = self.pageurls[self.start : self.end]

		#Get the list of pages on the first page based on tag url
		count = 0
		for url in self.pageurls:
			stocklist = self.StockParser(url)
			occurrence = '\t'.join(stocklist)
			self.occurrences.append(occurrence)
			# time.sleep(1)
			count += 1
			print(count)
		filename = './../data/co-occurrence_' + str(self.start) + '-' + str(self.end) + '.txt'
		f = open(filename, 'w')
		f.write('\n'.join(self.occurrences))
		f.close()

def main():
	newsFile = "./../data/all_news.txt" #Initial url for getting all page tags
	start = 0
	end = 1000
	crawler = OccurrenceRetriever(newsFile, start, end)
	crawler.run()
main()
