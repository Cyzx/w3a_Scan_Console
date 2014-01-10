#-*- encoding: utf-8 -*-
import time

class Directory_Scan:
	def setScan_Main(self, scan_main):
		self.scan_main=scan_main

	def start(self,url):
		self.scan_main.print_load("Load Module: Directory_Scan target: %s" % url)

	def stop(self,target):
		time.sleep(1)
		self.scan_main.print_load("Finish Check Directory_Scan target:%s" % target)
	
	def update_date(self):
		self.scan_main.print_load("Directory Check Result Insert to Database!")

def getPluginClass():
	return Directory_Scan
