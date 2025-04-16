with open("input.txt", 'r') as file , open("cleaned.txt",'w') as file1:
    lines = file.readlines()
    for line in lines:
        if line.strip():
            file1.write(line)


with open("article.txt",'r') as file:
    content = file.read()

    content = content.replace("Python", "PYTHON")

with open('article.txt', 'w') as file:
    file.write(content)


with open("poem.txt",'r') as file:
    cont = file.read()
    cont = cont.upper()
with open("output.txt", 'w') as file:
    file.write(cont)


student = [] 

with open("student.txt",'r') as file, open("report.txt",'w') as report:
    for line in file:
        student.append(line.strip().split(","))
# print(student)
    for i in student:
        if int(i[1]) > 50:
            report.write(f"{i[0]}: {i[1]}\n")
            

with open("quotes.txt",'r') as file, open ("reversed_quotes.txt",'w') as reverse:
    const = file.readlines()
    rever_const = const[::-1]
    reverse.writelines(rever_const)
    