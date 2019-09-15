#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step 1: s1_get_all_news.py

import requests
import time
import re
import random
from bs4 import BeautifulSoup

class NewsLinkCrawler:
	# Crawler of page webpage
	def __init__(self, url):
		self.rooturl = url
		self.pageurls = []

	# Get the urls of all news articles
	def run(self):
		html = requests.get(self.rooturl)

		soup = BeautifulSoup(html.text)  #Parse webpage by using BeautifulSoup
		links = soup.select("urlset > url > loc")
		for link in links:
			url = link.get_text()  #Get the text of each tag
			if '/news/' in url:
				self.pageurls.append(url)
		f = open('./../data/all_news.txt', 'w')
		f.write('\n'.join(self.pageurls))
		f.close()

def main():
	url="https://www.investopedia.com/sitemap_1.xml" #Initial url for getting all page tags
	crawler = NewsLinkCrawler(url)
	crawler.run()
main()
