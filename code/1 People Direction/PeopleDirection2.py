# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#1000019,20150406,064653,4haoxiantangqiao,dt,0.0,fyh,
from collections import defaultdict
import pandas as pd
import datetime

starttime = datetime.datetime.now()
data_dict = defaultdict(dict)
df = pd.read_csv("DT-100000ofT3")   
FromStop = ''
FromDay =''
FromTime = ''
ArrivalStop = ''
ArrivalTime = ''
for index, row in df.iterrows():
    if int(row['6']) == 0:                
        FromStop = row['4']#zhandian      
        FromDay = row['2']
        FromTime = row['3']
    else:
        ArrivalStop = row['4']#zhandian 
        ArrivalTime = row['3']       
        ID = FromStop+'-'+ArrivalStop
        data_dict[ID].setdefault('num',0)
        data_dict[ID]['num']+=1
endtime = datetime.datetime.now()
print 'nn'
print (endtime - starttime).seconds
f = open('DT-PeopleDirection2', 'w')
for key, value in data_dict.iteritems():
    f.write(str(key)+","+str(value['num'])+"\n")
f.close()
endtime = datetime.datetime.now()
print 'nn'
print (endtime - starttime).seconds
