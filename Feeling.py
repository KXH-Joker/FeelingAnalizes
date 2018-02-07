# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:50:38 2018

@author: joker
"""

import pandas as pd

date = pd.read_csv("C:/Users/joker/Desktop/date/huizong.csv",encoding = 'utf-8')

date = date[['评论']][date['品牌'] == '海尔']

date.to_csv("C:/Users/joker/Desktop/date/haier_jd.txt" , index = False , encoding = 'utf-8'  , header = False)

print(date.head())

S_date = pd.read_csv("C:/Users/joker/Desktop/date/haier_jd.txt",encoding = 'utf-8',header = None)

l = len(S_date)

S_date = pd.DataFrame(S_date[0].unique())

l1 = len(S_date)

S_date.to_csv("C:/Users/joker/Desktop/date/haier_jd1.txt",index = False , header = False , encoding = 'utf-8')

print('删除了 %s 条评论' %(l - l1))