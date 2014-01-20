#-*- encoding: utf-8 -*-

from lib.process_exec import  process_class
import time

class Web_Scan_Frame:
	
	def setScan_Main(self, scan_main):
		self.scan_main=scan_main

	def start(self,url):
#		t=process_class(10)
#		aa=['a','b','c','d','1',1,2,3,4,5,6,7,8,9,0,213123,3,23,23,2,312,312,3,12,31,23,12,3,123,1,231,3,1]
#		t._createProcess(abc,aa)

		self.scan_main.print_log("Load Module: Directory_Scan target: %s" % url)

	def stop(self,target):
		time.sleep(1)
		self.scan_main.print_log("Finish Check Directory_Scan target:%s" % target)
	
	def update_date(self):
		self.scan_main.print_log("Directory Check Result Insert to Database!")

def getPluginClass():
	return Web_Scan_Frame

def abc(item):
	print item
