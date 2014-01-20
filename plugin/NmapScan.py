#!/usr/bin/python
#-*- encoding: utf-8 -*-

###########################################
#
#   Nmap 扫描类(生成扫描结果)
#
###########################################

import nmap
from lib.process_exec import process_class
import time
import sys

class Web_Scan_Frame:
	
	def setScan_Main(self, scan_main):
		self.scan_main=scan_main

	# 放置:扫描目标,扫描模板
	def start(self,target,temple):
		# 需要根据扫描模板来查询是否有该模块扫描的功能
		self.scan_main.print_log('Nmap Scan Target: %s' % target)
		if temple==1:
			return 
		obj=Nmap_self_module(target)
		obj.nmap_do()

	def stop(self,target):
		time.sleep(1)
		self.scan_main.print_log("Finish Nmap target:%s" % target)
	
	def update_date(self):
		self.scan_main.print_log("Nmap Result Insert to Database!")

def getPluginClass():
	return Web_Scan_Frame

class Nmap_self_module:
   def __init__(self,Ip_list):
      self.Ip_list=Ip_list

   def make_rep(self,item):
      if item =="":
         return None
      elif item is None:
         return None
      else:
         return item

   def  nmap_do(self):
        nm=nmap.PortScanner()
        nm.scan(hosts=self.Ip_list,arguments='-T4 -O')
        for ip in nm.all_hosts():
            try:
                print '[*]'+ip
                print '[*]'+nm[ip]['status']['state']
                print '[*]'+nm[ip]['addresses']['mac']
                print '[*]'+nm[ip]['hostname']

                try:
                    for  port in nm[ip]['tcp'].keys():
                        print "[*] port: "+ str(port) + " name: " + nm[ip]['tcp'][port]['name'] + " status: " + nm[ip]['tcp'][port]['state']
                except:
                    print "tcp Error"

                try:
                    for os in nm[ip]['osmatch']:
                        print "[*] name: "+os['name'] + " accuracy: "+os['accuracy']
                except:
                    print "osmatch error"
            except:
                print "Update or status or mac Error"

