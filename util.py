# Functions to read api data
import urllib2

import json

__author__ = 'xz'



class Util():

	def __init__(self):
		self.base_url_head = "http://api.crunchbase.com/v/1/"
		self.base_url_tail = ".js?api_key=97swynz7qjjd9rsrbtkz38vt"

# Example: data = urllib2.urlopen("http://api.crunchbase.com/v/1/company/zynga.js?api_key=97swynz7qjjd9rsrbtkz38vt")


	def getCompanyJsonFromUrl(self,permalink):
		url_token = "company/"
		try:
			data = urllib2.urlopen(self.base_url_head + url_token + permalink + self.base_url_tail)
			j = json.load(data)
			return j
		except urllib2.HTTPError, e:
			print e.msg

	def getPersonJsonFromUrl(self,permalink):
		url_token = "person/"
		try:
			data = urllib2.urlopen(self.base_url_head + url_token + permalink + self.base_url_tail)
			j = json.load(data)
			return j
		except urllib2.HTTPError, e:
			print e.msg


	def getFinancialOrgJsonFromUrl(self,permalink):
		url_token = "financial-organization/"
		try:
			data = urllib2.urlopen(self.base_url_head + url_token + permalink + self.base_url_tail)
			j = json.load(data)
			return j
		except urllib2.HTTPError, e:
			print e.msg








