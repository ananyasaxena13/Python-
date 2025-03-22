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