data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]

def groupbyDepart(data):
    from collections import defaultdict

    result = defaultdict(list) # 

    for dept, emp, salary in data:
        result[dept].append((emp, salary))

    for dept in result:
        result[dept].sort(key=lambda x: x[1], reverse=True)
    print(dict(result))

groupbyDepart(data)



def invert_index(sentence):
    index ={}
    i =0
    for sentence in sentence:
        words = sentence.split()
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(i)
        i += 1
    return index

sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
print(invert_index(sentences))


import copy

original = {
    "marks" : [45,50,60]
}

shallow = original.copy()
deep = copy.deepcopy(original)

original["marks"].append(70)

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)



def word_length(words):
    dict = {}
    for word in words:
        length = len(word)
        if length not in dict:
            dict[length] = []
        dict[length].append(word)
    print(dict)

words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
word_length(words)



def merge_dicts(d1, d2):
    for key, value in d2.items():
        if key in d1:
            d1[key] = max(d1[key], value)
        else:
            d1[key] = value
    print(d1)

d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}

merge_dicts(d1, d2)
