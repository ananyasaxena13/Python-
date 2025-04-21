# Log File Analyzer

import os
count =0
with open("server.log",'r') as file, open("errors_only.log",'w') as error:
    lines = file.readlines()
    for line in lines:
        if "ERROR" in line:
            count +=1
            error.write(line)
print(f"Total number of errors: {count}")

# Word Frequency Counter

with open("story.txt",'r') as file:
    lines = file.readlines()
    word_freq ={}
    for line in lines:
        words = line.split() 
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
with open("frequency.txt",'w') as file:
    for word, freq in word_freq.items():
        file.write(f"{word}: {freq}\n")


# CSV Reader + Filter

import csv 

with open ("sales.csv",'r') as file, open("high_sales.csv",'w') as writecsv:
    reader = csv.DictReader(file)
    writer = csv.DictWriter(writecsv, fieldnames=reader.fieldnames)

    writer.writeheader()

    for row in reader:
        if int(row['Amount'].replace('Rs.', '')) > 10000:
            writer.writerow(row)


# Merge Multiple Files

filenames = ['chapter1.txt', 'chapter2.txt', 'chapter3.txt']

with open('full_book.txt', 'w') as file:
    for name in filenames:
        with open(name, 'r') as chapterfile:
            content = chapterfile.read()
            file.write(content)


# Directory File Scanner

import os
counttxt =0
countcsv =0
folder_path = "C:/Users/anasa/OneDrive/Desktop/Python-Training/Python-/Day10-FIleHandling/MiniProject"
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        counttxt +=1
    elif filename.endswith('.csv'):
        countcsv +=1
print(f"Number of .txt files: {counttxt}\nNumber of .csv files: {countcsv}")