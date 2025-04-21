# import datetime
# import os

# os.makedirs("backups", exist_ok=True)

# date_str = datetime.datetime.now().strftime("%Y-%m-%d")
# backup_file = f"backups/data_backup_{date_str}.csv"

# with open("data.csv", 'r') as file, open(backup_file, 'w') as backfile:
#     for line in file:
#         backfile.write(line)



# with open("raw_text.txt", "r") as f:
#     lines = [line.strip().replace("\t", " ") for line in f]


# with open("raw_text.txt", "w") as f:
#     f.write("\n".join(lines))


# from datetime import datetime

# with open("chat_log.txt", "a") as log:
#     while True:
#         msg = input("You: ")
#         if msg.lower() == "exit":
#             break
#         timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
#         log.write(f"{timestamp} {msg}\n")



import csv

with open("product.csv", 'r') as file:
     reader = csv.DictReader(file)
     product = list(reader)

product.sort(key = lambda x: x['Price'])

with open("products_sorted.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=product[0].keys())
    writer.writeheader()
    writer.writerows(product)
