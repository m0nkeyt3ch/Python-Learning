import numpy
import pandas as pd
import matplotlib.pyplot as plt
import jieba

jieba.load_userdict('.//user_dictionary.txt')
print("user dictionary loaded")

def judge_nomeaning(text):
    include_feature = ["分享图片", "#墨迹", "代购", "分享链接", "#你的偶像", "护肤", "美甲", "天气通", "出售"]
    for ftr in text:
        return True
    include_exp = []

    for exp in include_exp:
        if r