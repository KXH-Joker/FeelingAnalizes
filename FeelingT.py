# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:26:56 2018

@author: joker
"""

import pandas as pd

input1 = "C:/Users/joker/Desktop/date/qg_bad.txt"
input2 = "C:/Users/joker/Desktop/date/qg_good.txt"

output1 = "C:/Users/joker/Desktop/date/haier_jd_bad.txt"
output2 = "C:/Users/joker/Desktop/date/haier_jd_good.txt"

data1 = pd.read_csv(input1 , encoding = "utf-8" , header = None)
data2 = pd.read_csv(input2 , encoding = "utf-8" , header = None)

data1 = pd.DataFrame(data1[0].str.replace('.*\d+?\\t',""))
data2 = pd.DataFrame(data2[0].str.replace('.*\d+?\\t',""))

data1.to_csv(output1 , index = False , header = False , encoding = "utf-8")
data2.to_csv(output2 , index = False , header = False , encoding = "utf-8")