from pymongo import MongoClient

# 1️⃣ Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# 2️⃣ Create / Connect to Database
db = client['student_db']

# 3️⃣ Create / Connect to Collection
collection = db['logical_example']

# ----------------------------
# 🧹 Clean old data
# ----------------------------
collection.delete_many({})

# ----------------------------
# 🟢 Insert Sample Data
# ----------------------------
students_data = [
    {'name': "Geeta", 'age': 20, 'course': "Python", 'marks': 85},
    {'name': "Radha", 'age': 21, 'course': "Java",   'marks': 75},
    {'name': "Sita",  'age': 22, 'course': "Python", 'marks': 92},
    {'name': "Ravi",  'age': 19, 'course': "C++",    'marks': 65},
    {'name': "Pooja", 'age': 23, 'course': "Java",   'marks': 70}
]
collection.insert_many(students_data)
print("✅ Data Inserted Successfully!\n")

# ----------------------------
# 📋 Display All Data
# ----------------------------
print("📘 All Students:")
for s in collection.find():
    print(s)

# ----------------------------
# ⚙️ Logical Operators Examples
# ----------------------------

# 1️⃣ $and → BOTH conditions true
print("\n1️⃣ $and — Students with course = 'Python' AND marks > 80")
query = { "$and": [ {"course": "Python"}, {"marks": {"$gt": 80}} ] }
for s in collection.find(query):
    print(s)

# 2️⃣ $or → EITHER condition true
print("\n2️⃣ $or — Students with course = 'Java' OR marks < 70")
query = { "$or": [ {"course": "Java"}, {"marks": {"$lt": 70}} ] }
for s in collection.find(query):
    print(s)

# 3️⃣ $not → Negate condition
print("\n3️⃣ $not — Students where marks are NOT greater than 80")
query = { "marks": { "$not": { "$gt": 80 } } }
for s in collection.find(query):
    print(s)

# 4️⃣ $nor → None of the conditions true
print("\n4️⃣ $nor — Students where course ≠ 'Python' AND marks ≯ 80")
query = { "$nor": [ {"course": "Python"}, {"marks": {"$gt": 80}} ] }
for s in collection.find(query):
    print(s)

print("\n🎯 All Logical Operators Executed Successfully!")
