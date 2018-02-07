# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:57:34 2018

@author: joker
"""

import pandas as pd
import jieba

input1 = "C:/Users/joker/Desktop/date/haier_jd_bad.txt"
input2 = "C:/Users/joker/Desktop/date/haier_jd_good.txt"

output1 = "C:/Users/joker/Desktop/date/bad.txt"
output2 = "C:/Users/joker/Desktop/date/good.txt"

data1 = pd.read_csv(input1 , encoding = "utf-8" , header = None)
data2 = pd.read_csv(input2 , encoding = "utf-8" , header = None)

mycut = lambda s : ' '.join(jieba.cut(s))

data1 = data1[0].apply(mycut)
data2 = data2[0].apply(mycut)

data1.to_csv(output1 , index = False , header = False , encoding = "utf-8")
data2.to_csv(output2 , index = False , header = False , encoding = "utf-8")