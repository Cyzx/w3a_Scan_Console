#-*- encoding:utf-8 -*-
from lib.DB_module import Db_module

db_key=Db_module()
count=db_key.select_count('w3a_Scan_Task')
print count
