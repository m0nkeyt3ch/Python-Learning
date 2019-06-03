#declaring web as input
web = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
#temp is declaring for empty list
temp = []
#in here is doing for every key in web we do split 2 times
for key in web:
     temp.append(key.split(".", 2))
#in here we just print the third member of each list //you can use 2 or -1, for -1 is reverse indexing.
for suffix in temp:
    print(suffix[-1])
