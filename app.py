from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.healthcare_data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_data = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "income": float(request.form["income"]),
            "expenses": {
                "utilities": float(request.form.get("utilities", 0)),
                "entertainment": float(request.form.get("entertainment", 0)),
                "school_fees": float(request.form.get("school_fees", 0)),
                "shopping": float(request.form.get("shopping", 0)),
                "healthcare": float(request.form.get("healthcare", 0))
            },
            "submitted_at": datetime.datetime.utcnow()
        }
        db.users.insert_one(user_data)
        return "Data submitted successfully!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)