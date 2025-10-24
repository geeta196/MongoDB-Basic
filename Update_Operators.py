from pymongo import MongoClient
from datetime import datetime

# ----------------------------
# 🧩 Connect to MongoDB
# ----------------------------
client = MongoClient("mongodb://localhost:27017")
db = client["student_db"]
collection = db["update_examples"]

# Clean old data
collection.delete_many({})

# ----------------------------
# 🟢 Insert Sample Data
# ----------------------------
collection.insert_many([
    {'name': "Geeta", 'age': 20, 'marks': 85, 'subjects': ["Python", "Math"]},
    {'name': "Radha", 'age': 21, 'marks': 75, 'subjects': ["Java", "C++"]},
    {'name': "Sita", 'age': 22, 'marks': 90, 'subjects': ["HTML", "CSS"]}
])

print("✅ Initial Data Inserted!")

# ----------------------------
# 🧾 $set — set new field value
# ----------------------------
collection.update_one({'name': 'Geeta'}, {'$set': {'course': 'Full Stack'}})
print("\n1️⃣ Used $set → Added 'course' field")

# ----------------------------
# 📅 $currentDate — set current date/time
# ----------------------------
collection.update_one({'name': 'Radha'}, {'$currentDate': {'lastUpdated': True}})
print("2️⃣ Used $currentDate → Added current timestamp")

# ----------------------------
# ➕ $inc — increment numeric field
# ----------------------------
collection.update_one({'name': 'Sita'}, {'$inc': {'marks': 5}})
print("3️⃣ Used $inc → Increased marks by 5")

# ----------------------------
# ✏️ $rename — rename a field
# ----------------------------
collection.update_one({'name': 'Geeta'}, {'$rename': {'marks': 'score'}})
print("4️⃣ Used $rename → Renamed 'marks' to 'score'")

# ----------------------------
# ❌ $unset — remove a field
# ----------------------------
collection.update_one({'name': 'Radha'}, {'$unset': {'age': ""}})
print("5️⃣ Used $unset → Removed 'age' field")

# ----------------------------
# 📚 Array Operators
# ----------------------------

# $push → Add element to array
collection.update_one({'name': 'Geeta'}, {'$push': {'subjects': 'React'}})
print("\n6️⃣ Used $push → Added 'React' to subjects")

# $addToSet → Add unique element only if not exists
collection.update_one({'name': 'Sita'}, {'$addToSet': {'subjects': 'Python'}})
print("7️⃣ Used $addToSet → Added 'Python' if not exists")

# $pull → Remove specific value from array
collection.update_one({'name': 'Radha'}, {'$pull': {'subjects': 'C++'}})
print("8️⃣ Used $pull → Removed 'C++' from subjects")

# $pop → Remove first (-1) or last (1) element
collection.update_one({'name': 'Geeta'}, {'$pop': {'subjects': 1}})
print("9️⃣ Used $pop → Removed last subject")

# ----------------------------
# 🧾 Display final data
# ----------------------------
print("\n📋 Final Data:")
for doc in collection.find():
    print(doc)
