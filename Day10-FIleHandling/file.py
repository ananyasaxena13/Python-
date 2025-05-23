# Opening a file in read mode

import csv

stu_list = [] 

with open("student.txt",'r') as file:
    for line in file:
        stu_list.append(line.strip().split(","))
# print(stu_list)

total = sum(int(i[1]) for i in stu_list)
# print("Total marks: ", total)
average = total / len(stu_list)
print(f"Average marks: {average:.2f}")

with open("top_student.txt",'w') as top_student:
    for i in stu_list:
        if int(i[1]) > average:
            top_student.write(f"{i[0]}: {i[1]}\n")

with open("student.csv",'w') as csvfile:

    writer = csv.writer(csvfile)
    writer. writerow(["Name", "Marks"]) # header
    #writer.writerow(stu_list)
    writer.writerows(stu_list) 
        