import os

with open("notes.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

count = 0
with open("poem.txt" , 'r') as file:
    lines = file.readlines()
    for line in lines:
        line.split()
        count+=1
    print(count)


with open('reminder.txt', 'w') as file:
    file.write("1. Sleep\n")
    file.write("2. Finish Python Assignment\n")
    file.write("3. Wake up early in the morning for breakfast\n")
    file.write("4. Hair Wash\n")
    file.write("5. Get ready by 10")


with open("reminder.txt", 'a') as file:
    file.write("\n6. Go to college")
    file.write("\n7. Attend classes")
    file.write("\n8. Complete assignments")
    file.write("\n9. Go to gym")
    file.write("\n10. Sleep early")


if(os.path.exists("data.txt")):
    with open("data.txt", 'r') as file:
        print("file exist")
else:
    print("file does not exist")