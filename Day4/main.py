# s ="Hello"
# print(s[-1])

# list =[1,2,3,4,5,6]
# print(list[2])

# str = "Hello"
# print(str[::-1])

# lst1 = [1,2,3]
# lst2 = [3,4,5]
# print(lst1 + lst2) 
# print(lst1 * 2)

# num =[1,2,3,2,4,3,3,1,3]
# print(num.count(3))

# my_tuple = (1, 2, 3); 
# print(my_tuple[1:]) 

# sentence = "Learn Python, step by step!"
# word = sentence.split()
# print(word)

# lst = ['Python', 'is', 'fun']
# sentence = " ".join(lst)
# print(sentence)

# lst = [1, 2, 2, 3, 4, 2] 
# print(lst.index(2))

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("anna"))
# print(is_palindrome("phone"))


# sentence ="Python is fun"
# words = sentence.split()
# res =" "
# for word in words:
#     if(len(word) > len(res)):
#         res = word
# print(res)

# lst =['a','b','c','d']
# print("".join(lst))

# lst =[(1,4),(3,2),(5,6)]
# res=[]
# for tup in lst:
#     res.append(tup[1])
# print(sorted(res))

# lst =[[1,2,3],[4,5,6],[7,8,9]] # flaten output: [1,2,3,4,5,6,7,8,9]
# res =[]
# for i in lst:
#     for j in i:
#         res.append(j)

# print(res)

# def flaten(lst): # flaten nested list of arbitary depth
#     res =[]
#     for i in lst:
#         if isinstance(i,list): # check if i is list
#             res.extend(flaten(i)) # recursive call
#         else:
#             res.append(i)
#     return res
# print(flaten([[1,2,3],[4,5,6],[7,8,9]]))

# def rotate_list(lst,k):
#     n = len(lst)
#     k = k % n # to handle case when k > n
#     for i in range(k): # rotate k times
#         last = lst[-1] 
#         for j in range(n-1,0,-1): # start from last element and move to first element  and shift elements to right
#             lst[j] = lst[j-1]
#         lst[0] = last
#     return lst
# print(rotate_list([1,2,3,4,5],2))        

# def anangram(s1,s2):
#     return sorted(s1) == sorted(s2)
# print(anangram("listen","silent")) 

# lst = [1,2,3,4,5,6,7,8,9]
# n = 3
# chunks = [lst[i:i+n] for i in range(0,len(lst),n)]
# print(chunks)


# def merge(l1,l2):
#     l1.extend(l2)
#     return sorted(l1)
# print(merge([1,2,3],[4,5,6]))


# def longest_pipeline(pipelines, threshold):
#     longest = max(pipelines,key =lambda x:x[1])[0]
#     lst_long = [pipeline for pipeline,time in pipelines if time> threshold]
#     print("Longest pipeline:",longest)
#     print("Pipelines longer than threshold:",lst_long)
# longest_pipeline([("Data Ingestion", 30),("Preprocessing", 45),("Model Training", 120),("Evaluation", 20)],40)


# logs = """ERROR 404: Not Found
# INFO: Connection established
# ERROR 500: Internal Server Error
# ERROR 404: Not Found
# """
# errors = logs.split("\n")
# print(errors)
# codes = {s.split()[1].strip(':') for s in errors if s.startswith("ERROR")}
# # print(sorted(codes))


# configs = "host=127.0.0.1;port=8080;mode=debug"

# config = configs.split(";")
# config_list = [tuple(x.split("=")) for x in config]
# print(config_list)


# post = "Loving the new #Python course! #Coding #Python #Learning"

# hashtags =set(word for word in post.split() if word.startswith("#"))
# print(hashtags)

 
# inventory = [
#     ("Apples", 50),
#     ("Oranges", 75),
#     ("Bananas", 30)
# ]


# highest =max(inventory,key = lambda x: x[1])[0]
# print(highest)


# survey_data = "5,3,4,1,2"

# maximum = max(survey_data.split(','),key = lambda x: x)
# minimum = min(survey_data.split(','),key = lambda x: x)

# print(f"Max Score: {maximum}, Min Score: {minimum}")  


# users = ["Alice", "Bob", "Charlie"]
# roles = ("Admin", "Editor", "Viewer")

# users_roles = {user: role for user, role in zip(users, roles)}
# print(users_roles)


# def categorize_ticket(message):
#     length = len(message)
    
#     if length < 20:
#         return "Category: Short"
#     elif 20 <= length <= 50:
#         return "Category: Medium"
#     else:
#         return "Category: Long"

# message = "My account is locked, please help!"
# print(categorize_ticket(message))  


# products = ["Laptop", "Smartphone", "Wireless Headphones"]

# longest = max(products,key = lambda x: len(x))
# print(longest)


# sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
# #avg of last 10
# avg = sum(sensor_readings[-10:])/10
# print(int(avg))

# transactions = [100, -50, 200, -150, 50]

# rev = transactions[::-1]
# print(rev)

# logs = ["System Boot", "Network Connected", "User Login"]
# timestamp = "2025-03-20"

# log_entries = [f"{timestamp}: {log}" for log in logs]
# print(log_entries)


# symbol = "*"
# count = 5

# for i in range(count): # output: '* * * * *'
#     print(symbol +" ",end="") 


# feedback = "The product is excellent, absolutely excellent!"
# #check high occurence
# occ = feedback.count("excellent")
# print(f"'exellent' count: {occ}")


# log = "INFO: All systems go. ERROR: Failed to start service."
# print(log.index("ERROR"))


# csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
# csv = csv_data.split("\n")
# data = [csv.split(",") for csv in csv]
# print(data)


# names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
# short = [name[0]+ name.split()[1]for name in names]
# print(short)

# a = [1,2,3,4,5,6,7,8,9,10]

# res = list(filter(lambda x: x%2 ==0, a))

# print(res)


# data = "abababababab"

# res = set(data)
# print(res)
# for i in res:
#     count =0
#     for i in data:
#         if(i in res):
#             count+=1
#     print(i,count)