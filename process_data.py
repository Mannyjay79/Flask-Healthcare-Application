import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.healthcare_data
users = list(db.users.find())

data = []
for user in users:
    record = {
        "name": user["name"],
        "age": user["age"],
        "gender": user["gender"],
        "income": user["income"],
        "utilities": user["expenses"]["utilities"],
        "entertainment": user["expenses"]["entertainment"],
        "school_fees": user["expenses"]["school_fees"],
        "shopping": user["expenses"]["shopping"],
        "healthcare": user["expenses"]["healthcare"]
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_csv("user_data.csv", index=False)
print("Data exported to user_data.csv")