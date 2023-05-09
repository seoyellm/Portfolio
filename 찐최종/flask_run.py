#------------------------------------------------
# pip install Flask,  requests
#------------------------------------------------

from flask import Flask, session, render_template, make_response, jsonify, request, redirect, url_for

import cx_Oracle
import pandas as pd
import numpy as np
import random

import folium
from folium import plugins
import re
import googlemaps
import pprint


import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys


app = Flask(__name__)
app.secret_key = "1111122222"


import pandas as pd
from youtubesearchpython import VideosSearch
import json

#------------------------------------------------------------
def my_youtube_search(search_str='금리상승영향', nrows=7) :
	videosSearch = VideosSearch(search_str, limit=nrows)
	json_res = videosSearch.result()

	#print(videosSearch.result())  ## [{},{},{}]
	#print(json.dumps(videosSearch.result(), sort_keys=True, indent=4))

	movie_list = json_res['result']
	# print(json.dumps(movie_list, sort_keys=True, indent=4))

	tot_list = []
	for movie in movie_list:
		dict = {}
		# print(movie['thumbnails'][0]['url'])
		# print(movie['link'])
		# print(movie['title'])
		dict["title"] 	 = movie['title']
		try :
			dict["movie"] = movie['richThumbnail']['url']
		except :
			dict["movie"] = movie['thumbnails'][0]['url']

		dict["img"] 	 = movie['thumbnails'][0]['url']
		dict["duration"] = movie['duration']
		dict["url"] 	 = movie['link']
		dict["rdate"] 	 = movie['publishedTime']
		dict["cnt"]  = movie['viewCount']['text']
		tot_list.append(dict)
	return tot_list  #[{},{}]


from pykrx import stock
from datetime import date

def mysearch() :
	try :
		driver = webdriver.Chrome('chromedriver_110.exe')
		driver.get("https://www.google.com/finance/quote/KOSPI:KRX")
		htmlstr = driver.page_source
		soup = BeautifulSoup(htmlstr, features="html.parser") #selenium을 통해 긁어온 정보를 파싱하기
		div_list = soup.select_one("#yDmH0d > c-wiz.zQTmif.SSPGKf.u5wqUe > div > div.e1AOyf > div > main > div.Gfxi4 > div.yWOrNb > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b > c-wiz > div > div:nth-child(1) > div > div.rPF6Lc > div > div:nth-child(2) > div > span.NydbP.VOXKNe.tnNmPe > div > div").text
		return div_list
	except :
		a="0.17%"
		# today = date.today().strftime('%Y-%m-%d')
		# # print(today,type(today))
		# df = stock.get_index_ohlcv_by_date(today, today, '1001')
		# #print(df['종가'].values[0])
		# return df['종가'].values[0]
		return a



def mysearch11() :

	driver = webdriver.Chrome('chromedriver_110.exe')
	driver.get("https://www.google.com/finance/quote/.IXIC:INDEXNASDAQ")

	htmlstr = driver.page_source

	soup = BeautifulSoup(htmlstr, features="html.parser") #selenium을 통해 긁어온 정보를 파싱하기


	div_list = soup.select_one("#yDmH0d > c-wiz > div > div.e1AOyf > div > main > div.Gfxi4 > div.yWOrNb > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b > c-wiz > div > div:nth-child(1) > div > div.rPF6Lc > div > div:nth-child(2) > div > span.NydbP.nZQ6l.tnNmPe > div > div").text
	return div_list

def mysearch22() :

	driver = webdriver.Chrome('chromedriver_110.exe')
	driver.get("https://ecos.bok.or.kr/#/")

	htmlstr = driver.page_source

	soup = BeautifulSoup(htmlstr, features="html.parser") #selenium을 통해 긁어온 정보를 파싱하기


	div_list = soup.select_one("#root > div.wrap-body > div > div.main-wrap.clearfix > div.main-row3.clearfix > div.main-right > div > div > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(1) > div > div.indi-value.value-current").text
	print(div_list)
	return div_list



@app.route('/')
def index():
	tot_list = my_youtube_search('금리상승영향', 10)
	new_list =[]
	for i in range(len(tot_list)):
		if i in (0,1,2,3,5,6):
			new_list.append(tot_list[i])
	print(new_list)

	map = folium.Map(location=[41.9152843, 12.0193372], zoom_start=0.45,
					 tiles='OpenStreetMap')  # Stamen Terrain')

	tooltip = "클릭하면 금리를 알 수 있습니다."

	folium.Marker([37.562323135234415, 126.9756004113592],
				  popup='한&nbsp;국&nbsp;은&nbsp;행 : 3.50%',  # 클릭해서 나오는 팝업
				  tooltip=tooltip,
				  icon=folium.Icon(color="yellow", icon="info-sign")
				  ).add_to(map)

	folium.Marker(
		[39.2125759, -94.3652379],
		popup="<i>Federal Reserve System : 4.75%</i>",  # 클릭해서 나오는 팝업
		tooltip=tooltip,
		icon=folium.Icon(color="red", icon="info-sign")
	).add_to(map)

	map.get_root().width = "340px"
	map.get_root().height = "200px"
	html_str = map.get_root()._repr_html_()


	return render_template('index.html',KEY_MY_LIST=new_list, KEY_MAP=html_str,KOSPI=mysearch(),NASDAQ=mysearch11(),DOLLAR=mysearch22())






@app.route('/chart')
def chart():
    return render_template('chart-morris.html')
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=998225)