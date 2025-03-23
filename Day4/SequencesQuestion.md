# 1. Data Pipeline Validator

    def longest_pipeline(pipelines, threshold):
        longest = max(pipelines,key =lambda x:x[1])[0]
        lst_long = [pipeline for pipeline,time in pipelines if time> threshold]
        print("Longest pipeline:",longest)
        print("Pipelines longer than threshold:",lst_long)

    longest_pipeline(
        [("Data Ingestion", 30),("Preprocessing", 45),("Model Training", 120),("Evaluation", 20)],40)

# 2. Log File Parser

    logs = """ERROR 404: Not Found
    INFO: Connection established
    ERROR 500: Internal Server Error
    ERROR 404: Not Found
    """

    errors = logs.split("\n")
    print(errors)
    codes = {s.split()[1].strip(':') for s in errors if s.startswith("ERROR")}
    print(sorted(codes))


# 3. Config File Reader

    configs = "host=127.0.0.1;port=8080;mode=debug"

    config = configs.split(";")
    config_list = [tuple(x.split("=")) for x in config]
    print(config_list)

# 4. Social Media Data Cleaner

    post = "Loving the new #Python course! #Coding #Python #Learning"

    hashtags =set(word for word in post.split() if word.startswith("#"))
    print(hashtags)


# 5. Secret Code Decoder


# 6. Inventory Tracker

    inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
    ]

    highest =max(inventory,key = lambda x: x[1])[0]
    print(highest)


# 7. Survey Data Analyzer

    survey_data = "5,3,4,1,2"

    maximum = max(survey_data.split(','),key = lambda x: x)
    minimum = min(survey_data.split(','),key = lambda x: x)

    print(f"Max Score: {maximum}, Min Score: {minimum}")  


# 8. Access Control Manager

    users = ["Alice", "Bob", "Charlie"]
    roles = ("Admin", "Editor", "Viewer")

    users_roles = {user: role for user, role in zip(users, roles)}
**zip(users, roles) pairs each user with the corresponding role**
    print(users_roles)


# 9. Customer Support Ticket System

    def categorize_ticket(message):
    length = len(message)
    
    if length < 20:
        return "Category: Short"
    elif 20 <= length <= 50:
        return "Category: Medium"
    else:
        return "Category: Long"

    message = "My account is locked, please help!"
    print(categorize_ticket(message))  


# 10. Product Catalog Manager

    products = ["Laptop", "Smartphone", "Wireless Headphones"]

    longest = max(products,key = lambda x: len(x))
    print(longest)


# 11. Sensor Data Analyzer

    sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
**avg of last 10**
    avg = sum(sensor_readings[-10:])/10
    print(int(avg))


# 12. Transaction Reverser

    transactions = [100, -50, 200, -150, 50]

    rev = transactions[::-1]
    print(rev)


# 13. Log Formatter

    logs = ["System Boot", "Network Connected", "User Login"]
    timestamp = "2025-03-20"

    log_entries = [f"{timestamp}: {log}" for log in logs]
    print(log_entries)


# 14. Pattern Generator

    symbol = "*"
    count = 5

    for i in range(count): # output: '* * * * *'
        print(symbol +" ",end="") 


# 15. Customer Feedback Analyzer

    feedback = "The product is excellent, absolutely excellent!"

    occ = feedback.count("excellent")
    print(f"'exellent' count: {occ}")


# 16. Sentence Index Finder

    log = "INFO: All systems go. ERROR: Failed to start service."

    print(log.index("ERROR"))


# 17. CSV Parser

    csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
    csv = csv_data.split("\n")
    data = [csv.split(",") for csv in csv]
    print(data)


# 18. Username Generator

    names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
    short = [name[0]+ name.split()[1]for name in names]
    print(short)


# 19. Chat Log Analyzer

# 20. Data Compressor