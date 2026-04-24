# COLAB Note Link: https://colab.research.google.com/drive/1JKepiIkmGmXEFtsRfo1qvgGuUc4tV2jh?usp=sharing#scrollTo=b1910e4b

# 1) Python Basics Refresh
# Topics: types, slicing, truthiness, f‑strings
border = "-------------------------------------------------------------------------------------------------------------"

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Core types & literals ---

x = 42  # int
y = 3.14  # float
z = "hello"  # str
t = True  # bool
lst = [[1, 2, 3, ["Arif", "Rahul", 3.5, 100 * 2], 4], [10, 20, 30]]
ls2D = [[1, 2, 3], [4, 5, 6]]  # list (mutable)
tpl = (1, 2, 3, [1, 2, 3], "Arif")  # tuple (immutable)
dct = {"a": 1, "b": 2, "a": 3}  # dict (mapping)
st = {1, 2, 2, 3, "Arif"}  # set (unique)
lst.append(10)

print(dct)
print(lst)
print(ls2D)
print(tpl)
print(st)

print(type(x), type(y), type(z), type(lst), type(tpl), type(dct), type(st))
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# **Python Data Types – ছোট নোট**
#
# Python এ কয়েকটি built-in data type আছে:
#
# int → পূর্ণ সংখ্যা (যেমন 42)
# float → দশমিক সংখ্যা (যেমন 3.14)
# str → লেখা বা string (যেমন "hello")
# bool → True বা False
#
# Collection type গুলো:
#
# list → mutable, মান পরিবর্তন করা যায় (append করা যায়)
# tuple → immutable, পরিবর্তন করা যায় না
# dict → key-value pair আকারে ডাটা রাখে, একই key বারবার দিলে শেষেরটা থাকবে
# set → unique value রাখে, duplicate নেয় না
#
# মনে রাখবে: list পরিবর্তনযোগ্য, কিন্তু tuple পরিবর্তনযোগ্য না।

# ----------------------------------------------------------------------------------------------------------------------

# Python এ মূলত built-in core data type কয়েকটি প্রধান ভাগে ভাগ করা যায়। নিচে প্রতিটা ১ লাইনে explanation ও ১টা example দিচ্ছি।
#
# int → পূর্ণসংখ্যা টাইপ
# Example: x = 10
#
# float → দশমিক সংখ্যা টাইপ
# Example: y = 3.14
#
# complex → বাস্তব ও কাল্পনিক অংশসহ সংখ্যা
# Example: z = 2 + 3j
#
# bool → True বা False logical মান
# Example: is_valid = True
#
# str → লেখা বা text টাইপ
# Example: name = "Arif"
#
# list → mutable sequence (পরিবর্তনযোগ্য তালিকা)
# Example: lst = [1, 2, 3]
#
# tuple → immutable sequence (অপরিবর্তনযোগ্য তালিকা)
# Example: tpl = (1, 2, 3)
#
# range → নির্দিষ্ট সংখ্যা ধারা তৈরি করে
# Example: r = range(5)
#
# dict → key-value pair আকারে ডাটা সংরক্ষণ করে
# Example: d = {"a": 1, "b": 2}
#
# set → unique unordered value সংরক্ষণ করে
# Example: s = {1, 2, 3}
#
# frozenset → immutable set
# Example: fs = frozenset({1, 2, 3})
#
# bytes → immutable binary data
# Example: b = b"hello"
#
# bytearray → mutable binary data
# Example: ba = bytearray(5)
#
# memoryview → binary data-এর উপর view তৈরি করে
# Example: mv = memoryview(b"abc")
#
# NoneType → কোনো মান নেই বোঝায়
# Example: x = None
#
# এগুলোই Python এর প্রধান built-in data types।

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Slicing sequences ---
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])  # middle slice
print(nums[-3:])  # last 3
print(nums[::2])  # step slice
print(nums[::-1])  # reverse
print(nums[:-3])
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# Slicing মানে হলো sequence (যেমন list, str, tuple) থেকে নির্দিষ্ট অংশ বের করা।
#
# Syntax: sequence[start:stop:step]
#
# start → কোন index থেকে শুরু করবে
# stop → কোন index পর্যন্ত যাবে (stop index include হয় না)
# step → কয় ধাপ পর পর element নেবে
#
# nums[1:4] → index 1 থেকে 3 পর্যন্ত অংশ নেয়
# nums[-3:] → শেষের ৩টা element নেয়
# nums[::2] → প্রতি ২টা পর পর element নেয়
# nums[::-1] → পুরো list উল্টো করে দেয়
# nums[:-3] → শেষের ৩টা বাদ দিয়ে বাকি অংশ নেয়
#
# Slicing খুব powerful কারণ এক লাইনে extract, copy বা reverse করা যায়।

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Truthiness ---
samples = [0, 1, "", "text", [], [1], {}, {"k": 1}, None]
for item in samples:
    if item:
        print(repr(item), "→ Truthy")
    else:
        print(repr(item), "→ Falsy")

# --- DEMO: f-strings ---
name = "John"
score = 95
print(f"{name} scored {score}% (next: {score + 1}%)")
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# Truthiness মানে হলো কোনো value কে if condition এ ব্যবহার করলে সেটা True হিসেবে ধরা হবে নাকি False হিসেবে ধরা হবে।
#
# Falsy value গুলো হলো: 0, "", [], {}, None — এগুলো empty বা zero হওয়ায় False হিসেবে গণ্য হয়।
# Truthy value গুলো হলো: 1, "text", [1], {"k":1} — মানে যেগুলো empty না বা zero না।
#
# if item: লিখলে Python নিজেই check করে নেয় সেটা Truthy না Falsy।
#
# f-string হলো string format করার সহজ ও modern উপায়।
# f"{name} scored {score}%" এর ভিতরে {} এর মধ্যে variable বা expression লিখে সরাসরি print করা যায়।

# repr() এর কাজ হলো কোনো object এর **official string representation** দেখানো।
# মানে, Python যেভাবে internally value টাকে দেখায়, ঠিক সেইভাবে output দেয়।
#
# এই code এ repr(item) ব্যবহার করা হয়েছে যেন empty string "" আর normal string "text" আলাদা বোঝা যায়।
#
# উদাহরণ:
# print("") দিলে কিছুই দেখা যায় না।
# print(repr("")) দিলে "" দেখা যায়।
#
# তাই repr() debugging এর সময় খুব useful, কারণ এটা value এর আসল structure স্পষ্ট করে দেখায়।

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Nested data structures ---
data = {
    "user": {
        "name": "Alice",
        "id": 123,
        "contact": {
            "email": ["alice@example.com", "abc@edu.com"],
            "phone": "555-1234"
        }
    },
    "items": [
        {"name": "Laptop", "price": 1200},
        {"name": "Keyboard", "price": 75}
    ]
}

print("User Name:", data["user"]["name"])
print("First Item Price:", data["items"][0]["price"])
print("User Email:", data["user"]["contact"]["email"][1])
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# Nested data structure মানে হলো একটার ভিতরে আরেকটা data structure রাখা।
#
# এখানে dict এর ভিতরে dict, dict এর ভিতরে list, আর list এর ভিতরে আবার dict আছে।
#
# এমন structure সাধারণত complex data যেমন JSON response handle করার জন্য ব্যবহার হয়।
#
# Access করার সময় step by step key এবং index ব্যবহার করতে হয়, যেমন:
# data["user"]["contact"]["email"][1]
#
# মনে রাখবে, আগে key, তারপর index — structure বুঝে access করতে হয়।

# ----------------------------------------------------------------------------------------------------------------------

# Problem: Analyze Order Data
# Given the following nested dictionary representing a customer order, extract and print the following information:
#
# The customer's full name.
# The total price of all items in the order.
# A list of the names of all items in the order.

# ----------------------------------------------------------------------------------------------------------------------

order_data = {
    "customer": {
        "first_name": "Bob",
        "last_name": "Johnson"
    },
    "items": [
        {"item_name": "Book",
         "price": 25.99
         },
        {"item_name": "Notebook",
         "price": 4.50
         },
        {"item_name": "Pen",
         "price": 1.20
         }
    ]
}

# 1. Customer's full name
full_name = f"{order_data['customer']['first_name']} {order_data['customer']['last_name']}"
print("Customer Full Name:", full_name)

# 2. Total price of all items
total_price = sum(item["price"] for item in order_data["items"])
print("Total Order Price:", total_price)

# 3. List of item names
item_names = [item["item_name"] for item in order_data["items"]]
print("Item Names:", item_names)
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# List comprehension হলো এক লাইনে নতুন list তৈরি করার একটি smart এবং concise পদ্ধতি।
#
# এটি সাধারণত loop এবং condition একসাথে ব্যবহার করে নতুন list বানাতে কাজে লাগে।
#
# Syntax: [expression for item in iterable if condition]
#
# এতে code ছোট, readable এবং efficient হয়।

# ----------------------------------------------------------------------------------------------------------------------

# Exercises (quick checks)
#
# E1.1: Slice mylist = [1,2,3,4,5,6,7,8] to get the even-indexed items.
# E1.2: Using f‑strings, print: "User: <your name>, Items: <count>" where count is the length of a list.
# Stretch: Create a dict and print a sentence using f‑strings that reference two keys.

# ----------------------------------------------------------------------------------------------------------------------

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print('E1.1 Result: ', mylist[::2])

your_name = f"{order_data["customer"]["first_name"] + " " + order_data["customer"]["last_name"]}"
item_count = len(order_data["items"])
print('E1.2 Result: ', f"User: {your_name}, Items: {item_count}")
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# 2) Control Flow & Comprehensions
# Topics: if/elif/else, loops, list/dict/set comprehensions

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Control flow ---
for i in range(0, 51):
    if i == 0:
        label = "zero"
    elif i % 2 == 0:
        label = "even"
    else:
        label = "odd"
    print(i, "→", label)

print(border)

# ----------------------------------------------------------------------------------------------------------------------

for i in range(5):
    for j in range(5):
        print(i)
        print(j)

print(border)

# ----------------------------------------------------------------------------------------------------------------------

# Control flow হলো program এর execution flow নিয়ন্ত্রণ করার পদ্ধতি।
#
# এখানে for loop দিয়ে একাধিক value iterate করা হচ্ছে এবং if, elif, else দিয়ে condition check করা হচ্ছে।
#
# Condition অনুযায়ী even, odd বা zero label assign হচ্ছে।
#
# Control flow ব্যবহার করে decision making এবং logical branching করা যায়।

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Comprehensions ---
temp = [35, 40, 28, 32, 30]

fahrenheit = [item * (9 / 5) + 32 for item in temp]
print(f"First {fahrenheit}")

fahrenheit1 = [item * (9 / 5) + 32 for item in temp if item % 2 == 0]
print(fahrenheit1)

for item in temp:
    print(item * (9 / 5) + 32)

squares = [x ** 2 for x in range(6)]

evens = [x for x in range(20) if x % 2 == 0]

square_map = {x: x ** 2 for x in range(5)}

unique_initials = {item[0].lower() for item in ["Alice", "Bob", "alex", "Beta"]}

print(f"Square is : {squares}")
print(f"even: {evens}")
print(f"smap: {square_map}")
print(f"ui : {unique_initials}")

print(border)

# ----------------------------------------------------------------------------------------------------------------------

# Create a list of lists where inner lists contain squares of even numbers
nested_squares = [[x ** 2 for x in range(i, i + 5) if x % 2 == 0] for i in range(1, 10, 3)]
print("Nested Squares:", nested_squares)
print(border)

# ----------------------------------------------------------------------------------------------------------------------

# Nested list comprehension মানে list এর ভিতরে আরেকটা list comprehension ব্যবহার করা।
#
# এখানে বাইরের comprehension i এর জন্য range(1, 10, 3) থেকে মান নিচ্ছে।
# প্রতি i এর জন্য ভিতরের comprehension range(i, i+5) থেকে even সংখ্যা (x % 2 == 0) নির্বাচন করে তাদের square (x**2) তৈরি করছে।
#
# ফলাফল হবে একটা 2D list, যেখানে প্রতিটা sublist আলাদা আলাদা condition অনুযায়ী তৈরি।
#
# সংক্ষেপে: Nested comprehension দিয়ে কম লাইনে complex 2D data structure তৈরি করা যায়।

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Nested Comprehensions and Conditional Logic ---

# Create a dictionary mapping numbers to a description based on conditions
number_descriptions = {
    num: ("Even and divisible by 3" if num % 2 == 0 and num % 3 == 0
          else "Even" if num % 2 == 0
    else "Odd and divisible by 3" if num % 3 == 0
    else "Odd")
    for num in range(1, 100)
}
print("Number Descriptions:", number_descriptions)

print(border)

# ----------------------------------------------------------------------------------------------------------------------

# এটা একটি dictionary comprehension এর উদাহরণ।
#
# এখানে range(1, 100) থেকে প্রতিটি num নিয়ে condition অনুযায়ী value সেট করা হচ্ছে।
# ternary expression ব্যবহার করে এক লাইনে একাধিক condition check করা হয়েছে।
#
# প্রথমে check করছে num কি একসাথে Even এবং 3 দিয়ে divisible কিনা,
# তারপর শুধু Even,
# তারপর 3 দিয়ে divisible Odd,
# না হলে শুধু Odd।
#
# সংক্ষেপে: dictionary comprehension দিয়ে condition ভিত্তিক key-value mapping খুব compact ভাবে তৈরি করা যায়।

# ----------------------------------------------------------------------------------------------------------------------

# --- DEMO: Combining Nested Structures with Control Flow and Comprehensions ---

# Sample data: list of user dictionaries with a list of orders for each user
users_data = [
    {"user_id": 1, "name": "Alice", "orders": [{"order_id": "A1", "amount": 150}, {"order_id": "A2", "amount": 200}]},
    {"user_id": 2, "name": "Bob", "orders": [{"order_id": "B1", "amount": 50}]},
    {"user_id": 3, "name": "Charlie", "orders": []}
]

# Calculate the total amount spent by each user using a loop
print("Total amount spent by each user (using loop):")
for user in users_data:
    total_spent = 0
    for order in user.get("orders", []):  # Use .get() for safe access
        total_spent += order.get("amount", 0)  # Use .get() for safe access
    print(f"{user.get('name', 'N/A')}: ${total_spent}")

# Get a list of all order amounts across all users using a nested comprehension
all_order_amounts = [order.get("amount", 0) for user in users_data for order in user.get("orders", [])]
print("\nAll order amounts:", all_order_amounts)

# Create a dictionary mapping user_id to the number of orders using a dictionary comprehension
orders_count_by_user = {user.get("user_id"): len(user.get("orders", [])) for user in users_data}
print("Number of orders per user:", orders_count_by_user)

print(border)

# ----------------------------------------------------------------------------------------------------------------------

# এখানে Nested data structure নিয়ে কাজ করা হয়েছে যেখানে list এর ভিতরে dictionary এবং তার ভিতরে আবার list আছে।
#
# প্রথম অংশে loop ব্যবহার করে প্রতিটি user এর total amount calculate করা হয়েছে।
# .get() method ব্যবহার করা হয়েছে safe access এর জন্য, যেন key না থাকলেও error না আসে।
#
# দ্বিতীয় অংশে nested list comprehension দিয়ে সব user এর সব order এর amount একসাথে একটি list এ নেওয়া হয়েছে।
#
# তৃতীয় অংশে dictionary comprehension দিয়ে প্রতিটি user_id এর সাথে তার মোট order সংখ্যা map করা হয়েছে।
#
# সংক্ষেপে: এখানে loop, nested comprehension এবং .get() method ব্যবহার করে complex data structure থেকে data efficiently extract করা শেখানো হয়েছে।

# ----------------------------------------------------------------------------------------------------------------------

# Exercises
#
# E2.1: From text = "Educating AI with Python", build a list of vowels using a comprehension.
# E2.2: Create a dict mapping numbers 1..5 to "odd"/"even" using a comprehension.
# Stretch: Build a set of unique lowercase letters from a sentence, excluding spaces and punctuation.

# ----------------------------------------------------------------------------------------------------------------------

text = "Educating AI with Python"

for alphabet in text:
    if alphabet in "aeiou" or alphabet in "AEIOU":
        print(alphabet)

vowels = [alphabet for alphabet in text if alphabet in "aeiouAEIOU"]
print('E2.1 Result: ', vowels)

for number in range(1, 6):
    if number % 2 == 0:
        print(number, " : even")
    elif number % 2 != 0:
        print(number, " : odd")
dictionary = {number: "even" if number % 2 == 0 else "odd" for number in range(1, 6)}
print('E2.2 Result: ', dictionary)

print(border)

# ----------------------------------------------------------------------------------------------------------------------

import numpy as np

# একটি তালিকায় ৭ জনের বেতন ২৫-৩৫ হাজারের মধ্যে, কিন্তু ১ জনের বেতন ৫ লাখ
data = [25, 27, 28, 29, 30, 31, 35, 500]  # 500 হল আউটলায়ার

print("গড় (Mean):", np.mean(data))  # Output: ~76.88
print("মধ্যমান (Median):", np.median(data))  # Output: 29.5

print(border)

# ----------------------------------------------------------------------------------------------------------------------

# এখানে আমরা numpy library ব্যবহার করে Mean এবং Median শিখছি।
#
# Mean হলো সবগুলো মান যোগ করে মোট সংখ্যা দিয়ে ভাগ করা গড় মান। Outlier থাকলে Mean অনেক বেশি পরিবর্তিত হয়।
#
# Median হলো মাঝের মান, অর্থাৎ sorted data থেকে একদম মাঝখানের সংখ্যা। Outlier থাকলেও Median খুব বেশি পরিবর্তিত হয় না।
#
# এই উদাহরণে 500 একটি outlier, তাই Mean অনেক বেড়ে গেছে, কিন্তু Median প্রায় আসল বেতনের কাছাকাছি আছে।

# ----------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

print(border)

# ----------------------------------------------------------------------------------------------------------------------

# এখানে আমরা matplotlib ব্যবহার করে একটি simple line graph আঁকছি।
#
# np.array দিয়ে x এবং y data তৈরি করা হয়েছে। তারপর plt.plot(x, y) দিয়ে graph আঁকা হয়েছে।
#
# plt.xlabel() এবং plt.ylabel() দিয়ে x-axis ও y-axis এর নাম সেট করা হয়েছে।
#
# plt.show() দিলে graph window ওপেন হয় এবং result দেখা যায়।
#
# শেষ লাইনে print(border) লিখলে error হবে, কারণ border নামে কোনো variable define করা হয়নি।

# ----------------------------------------------------------------------------------------------------------------------

lst = [1, 2, 3, 4, 5, 6]

def square(x):
    return x ** 2

lst = list(map(square, lst))

print(lst)

# ----------------------------------------------------------------------------------------------------------------------

# এখানে map() ব্যবহার করে list এর প্রতিটি element এর উপর একটি function apply করা হয়েছে।
#
# square(x) function প্রতিটি সংখ্যাকে square করে return করছে।
#
# map(square, lst) মানে lst এর প্রতিটি value square() এর মধ্যে যাবে।
#
# map() সরাসরি list return করে না, তাই list() দিয়ে convert করা হয়েছে।
#
# ফলাফল: প্রতিটি সংখ্যার square নিয়ে নতুন list তৈরি হয়েছে।

# ----------------------------------------------------------------------------------------------------------------------
