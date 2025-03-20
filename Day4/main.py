sentence ="Python is fun"
words = sentence.split()
res =" "
for word in words:
    if(len(word) > len(res)):
        res = word
print(res)