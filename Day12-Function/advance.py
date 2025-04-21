def analyze_text(text: str):
#return number of words\
#return number of unique words
#frequency f each word
    
    words = text.split()
    num_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)
    
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    print(f"Number of words: {num_words}\n Number of unique words: {num_unique_words}\n Word frequency: {word_frequency}")

text = "hello world hello python"
analyze_text(text)



def is_palindrome(s: str) -> bool:
    return s == s[::-1]

s = "anna"
print(is_palindrome(s))



def nested_sum(data: list) -> int:

    sum = 0
    for i in data:
        if isinstance(i, list): 
            sum += nested_sum(i)
        else:
            sum += i
    return sum
data = [[1, 2], [3, [4, 5]], 6]
print(nested_sum(data))  



def safe_divide(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Division by zero")

x = 10
y = 0
print(safe_divide(x, y))




def time_increment(h: int, m: int) -> tuple[int, int]:
    #simulate digital clock that returns time after 1 minute handle boundary casee
    m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    print(f"{h} : {m}")

h = 22
m = 30
print(time_increment(h, m))