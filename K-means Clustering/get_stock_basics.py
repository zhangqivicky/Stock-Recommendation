#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step 1: s1_get_all_news.py

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
import time

class StockBasicsCrawler:
	# Crawler of page webpage
	def __init__(self, url):
		self.rooturl = url

	# Get the urls of all news articles
	def run(self):
		file = "./../data/unique-stocks.txt"
		stocks = Path(file).read_text().split("\n")
		with open('./../data/stock_basics.csv', mode='w') as basics_file:
			basics_writer = csv.writer(basics_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			header = ["Stock", "Price", "Volume", "Market Cap", "Beta", "PE Ratio", "EPS"]
			basics_writer.writerow(header)
			count = 0	
			for stock in stocks:
				html = requests.get(self.rooturl + stock)
				soup = BeautifulSoup(html.text, features="lxml")  #Parse webpage by using BeautifulSoup
				pricetd = soup.select('td[data-test="PREV_CLOSE-value"]')
				price = pricetd[0].get_text().replace(",", "") if pricetd else "na"
				volumetd = soup.select('td[data-test="TD_VOLUME-value"]')
				volume = volumetd[0].get_text().replace(",", "") if volumetd else "na"
				mktcaptd = soup.select('td[data-test="MARKET_CAP-value"]')
				mktcap = mktcaptd[0].get_text().replace(",", "") if mktcaptd else "na"
				if "B" in mktcap:
					mktcap = float(mktcap.replace("B", ""))*1000
				elif "M" in mktcap:
					mktcap = mktcap.replace("M", "")
				elif mktcap.isdigit() :
					mktcap = float(mktcap)/1000000
				
				betatd = soup.select('td[data-test="BETA_3Y-value"]')
				beta = betatd[0].get_text() if betatd else "na"
				petd = soup.select('td[data-test="PE_RATIO-value"]')					
				pe = petd[0].get_text() if petd else "na"
				epstd = soup.select('td[data-test="EPS_RATIO-value"]')
				eps = epstd[0].get_text() if epstd else "na"
				record = [stock, price, volume, mktcap, beta, pe, eps]
				basics_writer.writerow(record)
				count += 1
				if count%20 == 0:
					print(count)
					time.sleep(3) 
				#break
				
def main():
	url="https://finance.yahoo.com/quote/" #Initial url for getting all page tags
	crawler = StockBasicsCrawler(url)
	crawler.run()
main()


