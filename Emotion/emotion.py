import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import os

def import_text(filepath):
    weibo = pd.DataFrame(index=np.arange(5000),
    columns=['text','coord1','coord2','datetime'])
    with open(filepath, 'r') as f:
        cnt = 0
        for line in f:
            line = (line.strip()).split()
            if line[3] == 'Tue':
                weibo.loc[cnt,:] = [line[0],float(line[1]),float(line[2]), np.nan]
                weibo.loc[cnt, 'text'] = weibo.loc[cnt, 'text'].split('http')[0]
                # datetime: exact to minute
                weibo.loc[cnt,'datetime'] = datetime(int(line[8]), 7, int(line[5]),
                int(line[6].split(':')[0]), int(line[6].split(':')[1]))
                cnt += 1
    weibo = weibo.dropna()
    # July 08 Tue and sort by time
    weibo = weibo.sort_values(by=['datetime'])
    return weibo[['text','coord1','coord2','datetime']]

def import_dict(dictpath):
    all_dicts = {}
    dict_list = os.listdir(dictpath)
    for dict in dict_list:
        jieba.load_userdict(dictpath+'/'+dict) # load to jieba
        dict_words = []
        with open(dictpath+'/'+dict, 'r') as f:
            for word in f:
                dict_words.append(word.strip())
        all_dicts[dict[:-4]] = dict_words
    return all_dicts

def emo_dic_freq(weibo, dicts):
    emotions = ['angry','disgusted','happy','sad','scared']
    weibo = pd.concat([weibo, pd.DataFrame(index=weibo.index, columns=emotions)],axis=1)
    weibo[emotions] = 0
    # word count
    for i in weibo.index:
        for w in jieba.cut(weibo.loc[i,'text']):
            for emo in emotions:
                if w in dicts[emo]:
                    weibo.loc[i, emo] += 1
    return weibo

def main():
    # if dataframe exist, then load
    if os.path.exists("./weibo_initial.pkl"):
        weibos = pd.read_pickle("./weibo_initial.pkl")
    else:
        text_path = 'data/weibo_test.txt'
    weibos = import_text(text_path)
    weibos.to_pickle("./weibo_initial.pkl")
    print(weibos.shape)
    # import to jieba user dict and save as list category
    dictpath = 'data/emotion_dictionary_test'
    all_dicts = import_dict(dictpath)
    # count emotion vector
    if os.path.exists("./weibo_emotions.pkl"):
        weibos = pd.read_pickle("./weibo_emotions.pkl")
    else:
        weibos = emo_dic_freq(weibos, all_dicts)
    weibos.to_pickle("./weibo_emotions.pkl")
    print(weibos.shape)
    print(weibos.iloc[:10, -5:])
