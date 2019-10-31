import numpy
import pandas as pd
import matplotlib.pyplot as plt
import jieba

angry_data = []
disgusted_data = []
happy_data = []
sad_data = []
scared_data = []

angry_count = 0
happy_count = 0
disgusted_count = 0
sad_count = 0
scared_count = 0

angry_txt = open("angry.txt", "r", encoding='utf-8-sig').read().splitlines()
angry_data.append(angry_txt)

disgusted_txt = open("disgusted.txt", "r", encoding='utf-8-sig').read().splitlines()
disgusted_data.append(disgusted_txt)

happy_txt = open("happy.txt", "r", encoding='utf-8-sig').read().splitlines()
happy_data.append(happy_txt)

sad_txt = open("sad.txt", "r", encoding='utf-8-sig').read().splitlines()
sad_data.append(sad_txt)

scared_txt = open("scared.txt", "r", encoding='utf-8-sig').read().splitlines()
scared_data.append(scared_txt)

weibo_txt = open("weibo_test.txt", "r", encoding="utf-8-sig").read()
words = jieba.lcut(weibo_txt)



