# Sequences in Python

- An ordered collection of objects, such as lists, tuples or strings allowing you to access manipulate elements by their position(index).

## Types of Sequences

1. **Mutable Sequeence --** can be changed after their creation, and also we can modify elements, adding new elements and removing existing ones.

    - **Lists(list):** A list is a mutable, ordered collection of items.
    - **Byte Arrays(bytes):** mutable sequence of bytes, used for handling binary data.
    - **Arrays:** A collection of items, storing elements of the same data type.

2. **Immutable Sequences --** classified as immutable have elements that are unchangeable once they are produced.

    - **Tuples(tuples):** collections of objects that are ordered and immutable.
    - **Strings:** Collection of Character sequences separated by single quotes ('') or double quotes ("")
    - **Integers:** defined as Whole numbers, both positive and negative, and are represented as integers, an immutable data type.

# Difference between strings, list and tuples

## Strings
    - immmutable 
    - ordered/indexed
    - allows deplicate values
    - empty string = " "
    - string with single element ="A"
   

## Lists
    - mutable
    - ordered/indexed
    - allows deplicate values
    - empty string = []
    - string with single element =["Apple"]
   

## Tuples
    - immmutable 
    - ordered/indexed
    - allows deplicate values
    - empty string = ( )
    - string with single element =("Apple")
    

# Indexing works in Python

    - starts at 0, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on. For example, if we have a string "Hello", we can access the first letter "H" using its index 0 by using the square bracket notation: string[0] .

# Code to access the last character of the string

s ="Hello"
print(s[-1])

# Create the list of number and access the third element

list =[1,2,3,4,5,6]
print(list[2])

# Result of len([1, [2, 3], 4]) and why?

 - output will be  3 becuase iit count th enumber of elements in the outer list.

 # Explain slicing with a practical example.

  - It follows the format string[start:end], where start is the index where slicing begins (inclusive) and end is the index where it ends (exclusive).
  **example:**
   str = "Hello World"
   print(str[7:12]) **Output: World**
   print(str[:2]) **Output: Hel**

# Reverse a string using slicing

 str = "Hello"
 print(str[::-1]) **Output: olleH**

 # List concatenation and repetition

 - If you concatenate a list with 2 items and a list with 4 items, you will get a new list with 6 items (not a list with two sublists). 
 - Similarly, repetition of a list of 2 items 4 times will give a list with 8 items.

lst1 = [1,2,3]
lst2 = [3,4,5]
print(lst1 + lst2) **concatenation**
print(lst1 * 2) **repetition**

# Code to count the occurrences of an element in a list.

num =[1,2,3,2,4,3,3,1,3]
print(num.count(3)) **Output: 4**

# Tuple output

my_tuple = (1, 2, 3); 
print(my_tuple[1:]) **Output: 2,3**

# Difference between list.append() and list.extend()

 - append() adds a single element to the end of the list as a whole. Adds a single object to the list.
 - extend() adds multiple elements from an iterable (such as a list, tuple, or set) to the list. Merges elements from another iterable.

 # Code to split the sentence: "Learn Python, step by step!" into words.

 sentence = "Learn Python, step by step!"
 word = sentence.split()
 print(word) **Output:['Learn', 'Python,', 'step','by','step!']**

# Join a list ['Python', 'is', 'fun'] into a single string.

 lst = ['Python', 'is', 'fun']
 sentence = " ".join(lst)
 print(sentence) **Output: Python is fun**

 # Given a list numbers = [1, 2, 2, 3, 4, 2], find the index of the first 2.

lst = [1, 2, 2, 3, 4, 2]
print(lst.index(2)) **Output: 1** 

# Code to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("anna"))
print(is_palindrome("phone"))

#  Function that returns the length of the longest word in a sentence.

sentence ="Python is fun"
words = sentence.split()
res =" "
for word in words:
    if(len(word) > len(res)):
        res = word
print(res)

# Demonstrate nested list indexing.

  - nested list is list inside another list.
  - allow you to access elements witin lists that   are inside other lists.
  - We access elements using two indices: one for the outer list and one for the inner list.

# Convert a list of characters into a string

    - using the join function
    charl = ['a','b','c','d']
    print("".join(charl))  
**Output : abcd**

# Code to remove duplicates from a list while preserving order

    lst =[2,3,5,4,1,2,4,3,5,6]
    res =[]
    for i in lst:
        if i not in res:
            res.append(i)
    print(sorted(res)) 
**or by using list(set(lst)) it removes duplicates but does not guarantee the order of element**


#  A function that takes a list of tuples and sorts it by the second element of each tuple.

    lst =[(1,4),(3,2),(5,6)]
    res=[]
    for tup in lst:
        res.append(tup[1])
    print(sorted(res))


# A program to flatten a nested list of arbitrary depth.

    lst =[[1,2,3],[4,5,6],[7,8,9]] # flaten output: [1,2,3,4,5,6,7,8,9]
    res =[]
    for i in lst:
        for j in i:
             res.append(j)
    print(res)

**OR using recursive call**

    def flaten(lst): 
    res =[]
    for i in lst:
        if isinstance(i,list): # check if i is list
            res.extend(flaten(i)) # recursive call
        else:
            res.append(i)
    return res
    print(flaten([[1,2,3],[4,5,6],[7,8,9]]))

# A function that rotates a list to the right by k steps.

    def rotate_list(lst,k):
    n = len(lst)
    k = k % n
    for i in range(k):
        last = lst[-1]
        for j in range(n-1,0,-1):
            lst[j] = lst[j-1]
        lst[0] = last
    return lst
    print(rotate_list([1,2,3,4,5],2))        
    

# Given two strings, write a function that returns True if they are anagrams.

    def anangram(s1,s2):
        return sorted(s1) == sorted(s2)
    print(anangram("listen","silent")) 

# Create a function to split a list into chunks of a specified size.

    lst = [1,2,3,4,5,6,7,8,9]
    n = 3
    chunks = [lst[i:i+n] for i in range(0,len(lst),n)]
    print(chunks)

# Implement a function that merges two sorted lists into one sorted list.
    
    def merge(l1,l2):
        l1.extend(l2)
        return sorted(l1)
    print(merge([1,2,3],[4,5,6]))


