#-*- encoding: utf-8 -*-
import os
import sys
import hashlib
import random
import string
from lib.log_exec import Log_do


class Scan_Main:

	# 程序的主过程
	def __init__(self):
		try:
			# 生成一个随机的名称作为异常日志的记录
			m=hashlib.md5(str(random.randint(1,100000))+"log")
			self.log_name=m.hexdigest()
			# 日志记录初始化
			self.log=Log_do(os.path.split(os.path.realpath(__file__))[0]+"/log/sys/"+self.log_name+".log")
		except:
			print "[*] Create log file is error! Please check directory purview!"
			sys.exit(0)
		try:
			# 输出Logo
			self.readmade()
			# 输出现有模块(并且自检)
			self.__module()
			# 导入模块
			self.__loadPlugins()
		except:
			self.print_load("Import Error, Or Path Not true!")
			sys.exit(0)
	
	# 程序LOGO
	def readmade(self):
		print r"----------------------------------------------------"
		print r"																		"
		print r"	 w3a_scan_console		"
		print r"																		"
		print r"	       by:Smart		"
		print r"																		"
		print r"----------------------------------------------------"
	
	# 输出现有模块/并自检
	def __module(self):
		ScanFilepath=os.path.split(os.path.realpath(__file__))[0]
		if os.path.exists(ScanFilepath+"/plugin"):
			self.print_log("Module List:")
			for filename in os.listdir(ScanFilepath+'/plugin'):
				if not filename.endswith('.py') or filename.startswith('_'):
					continue
				self.print_log("+ Module: %s" % os.path.splitext(filename)[0])
			self.print_log("-----------------------------------")
		else:
			# 如果模块文档不存在要退出控制，确保模块存在，不然无法检测。
			self.print_log("Plugins directory not in here!")
			self.print_log("Done")
			sys.exit(0)

	# 程序加载模块
	def __loadPlugins(self):
		ScanFilepath=os.path.split(os.path.realpath(__file__))[0]
		if os.path.exists(ScanFilepath+"/plugin"):
			for filename in os.listdir(ScanFilepath+'/plugin'):
				if not filename.endswith('.py') or filename.startswith('_'):
					continue
				self.__runPlugins(filename)

	# 程序执行模块
	def __runPlugins(self,filename):
		# 获得模块名称
		plugins_name=os.path.splitext(filename)[0]
		# 导入模块
		plugin=__import__("plugin."+plugins_name,fromlist=[plugins_name])
		# 获得模块对象
		clazz=plugin.getPluginClass()
		o=clazz()
		# 把自身传给模块
		o.setScan_Main(self)
		## 开始处理
		all_target=["http://www.baidu.com/","http://163.com"]
		while len(all_target)>0:
			for i in all_target:
				o.start(i)
				o.update_date()
				o.stop(i)
				all_target.remove(i)

	# 标准屏幕输出
	def print_log(self,log):
		print "[*] %s" % log

	# 打印提示流/记录日志
	def print_load(self,item):
		flog="[*] %s" % item
		print flog
		self.log.w_log(flog)

if __name__=="__main__":
	scan_main=Scan_Main()
