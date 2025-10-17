from pymongo import MongoClient

# 1️⃣ Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# 2️⃣ Create / Connect to Database
db = client['student_db']

# 3️⃣ Create / Connect to Collection
collection = db['comparison_example']

# ----------------------------
# 🧹 Clean old data (optional)
# ----------------------------
collection.delete_many({})

# ----------------------------
# 🟢 INSERT Sample Data
# ----------------------------
students_data = [
    {'name': "Geeta", 'age': 20, 'marks': 85},
    {'name': "Radha", 'age': 21, 'marks': 75},
    {'name': "Sita",  'age': 22, 'marks': 92},
    {'name': "vedant",  'age': 19, 'marks': 65},
    {'name': "varsha", 'age': 23, 'marks': 70}
]
collection.insert_many(students_data)
print("✅ Data Inserted Successfully!\n")

# ----------------------------
# 📘 Display All Data
# ----------------------------
print("📋 All Students:")
for s in collection.find():
    print(s)

# ----------------------------
# ⚖️ COMPARISON OPERATORS
# ----------------------------

# 1️⃣ $eq (Equal)
print("\n1️⃣ Students where age = 20")
for s in collection.find({'age': {'$eq': 20}}):
    print(s)

# 2️⃣ $ne (Not Equal)
print("\n2️⃣ Students where age != 20")
for s in collection.find({'age': {'$ne': 20}}):
    print(s)

# 3️⃣ $gt (Greater Than)
print("\n3️⃣ Students where marks > 80")
for s in collection.find({'marks': {'$gt': 80}}):
    print(s)

# 4️⃣ $lt (Less Than)
print("\n4️⃣ Students where marks < 80")
for s in collection.find({'marks': {'$lt': 80}}):
    print(s)

# 5️⃣ $gte (Greater Than or Equal)
print("\n5️⃣ Students where age >= 21")
for s in collection.find({'age': {'$gte': 21}}):
    print(s)

# 6️⃣ $lte (Less Than or Equal)
print("\n6️⃣ Students where marks <= 75")
for s in collection.find({'marks': {'$lte': 75}}):
    print(s)

print("\n🎯 All Comparison Operators Executed Successfully!")
