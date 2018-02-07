# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:16:01 2018

@author: joker
"""

import pandas as pd
from gensim import corpora,models

bad = "C:/Users/joker/Desktop/date/bad.txt"
good = "C:/Users/joker/Desktop/date/good.txt"

stop = "C:/Users/joker/Desktop/date/stoplist.txt"

baddata = pd.read_csv(bad , encoding = 'utf-8' , header = None)
gooddata = pd.read_csv(good , encoding = 'utf-8' , header = None)

stop = pd.read_csv(stop , encoding = 'utf-8' , header = None , sep = "tipdm")
'''
    sep设置分割词 由于csv默认以半角逗号为分割词，而改词恰好再停用词表中，因此会导致读取出错
    所以解决办法是手动设置一个不存在的分割词
'''
stop = [' ',''] + list(stop[0]) 

baddata[1] = baddata[0].apply(lambda s : s.split(" "))
baddata[2] = baddata[1].apply(lambda x : [i for i in x if i not in stop])

gooddata[1] = gooddata[0].apply(lambda s : s.split(" "))
gooddata[2] = gooddata[1].apply(lambda x : [i for i in x if i not in stop])
'''
    负面主题分析
'''
bad_dict = corpora.Dictionary(baddata[2])
bad_corpus = [bad_dict.doc2bow(i) for i in baddata[2]]
bad_lda = models.LdaModel(bad_corpus,num_topics=3,id2word=bad_dict)
for i in range(3):
    print(bad_lda.print_topic(i))
    bad_lda.print_topic(i)
    
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
'''
    正面主题分析
'''
good_dict = corpora.Dictionary(gooddata[2])
good_corpus = [good_dict.doc2bow(i) for i in gooddata[2]]
good_lda = models.LdaModel(good_corpus,num_topics=3,id2word=good_dict)
for i in range(3):
    print(good_lda.print_topic(i))
    good_lda.print_topic(i)