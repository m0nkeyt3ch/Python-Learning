import pandas as pd
import matplotlib.pyplot as plt
import jieba

# encoding='utf-8'

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


"""
with open("angry.txt", encoding='utf-8') as f:
    content = f.read().splitlines()
    angry_data.append(content)
    f.close()

with open("disgusted.txt", encoding='utf-8') as f:
    content = f.read().splitlines()
    disgusted_data.append(content)
    f.close()

with open("happy.txt", encoding='utf-8') as f:
    content = f.read().splitlines()
    happy_data.append(content)
    f.close()

with open("sad.txt", encoding='utf-8') as f:
    content = f.read().splitlines()
    sad_data.append(content)
    f.close()

with open("scared.txt", encoding='utf-8') as f:
    content = f.read().splitlines()
    scared_data.append(content)
    f.close()
"""
print(scared_data)

