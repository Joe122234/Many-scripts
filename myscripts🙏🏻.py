#import pandas as pd
#from pandas import *
#import time

"""
mydataset = {'cars': ['BMW', "Volvo", "Ford"],
             'passings': [3,7,2]}

myvar = pd.DataFrame(mydataset)
print(myvar)

#Series
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

#DataFrame 2 diemnsional sturcutre
data = {
    "calories": [420, 380, 390],
    "duration" : [50, 40, 45]
}
df = pd.DataFrame(data)
df["calories"] = df["calories"].apply(lambda x : f"{x} calories")
df["duration"] = df["duration"].apply(lambda x : f"{x} minutes")
print(df)

#Locate row with loc
data = {
    "calories": [420, 380, 390],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data)
print(df.loc[[0,1]])

#Named Indexes and locate index
data = {
    "calories": [420, 380, 390],
    "duration" : [50, 40, 45]
}
df = pd.DataFrame(data, index = ["Day 1: ", "Day 2: ", "Day 3: "])
print(df.loc["Day 2: "])

#To put file into a "df" use the function read_csv(*The file name*)
#To change the file into a string use the function "to_string" in the print line of df


df = pd.read_csv('nyc_taxis.csv')
print(df.head(10))

#Data cleaning
#Empty cells
df = pd.read_csv('nyc_taxis.csv')
new_df  =df.dropna()
print(new_df.to_string())

#Remove all rows with NULL values
df = pd.read_csv('nyc_taxis.csv')
df.dropna(inplace=True)
print(df.to_string())

#Get time function
def slow():
    values = []
    for x in range(10):
        values.append(x)
    

def fast():
    values = [x for x in range(10)] 
    print(values)

# Always have this code to test performance
def get_time(func: callable, *args: any) -> None:
    start_time: float = time.perf_counter()
    func(*args)
    end_time: float = time.perf_counter()
    print(f'"{func.__name__}()" took: {end_time - start_time:.5f} seconds')

def main():
    get_time(slow)
    get_time(fast)
    

if __name__ == "__main__":
    main()

import sys
from time import sleep

words = "This is just a test :P"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

#   MAP FUNCTION
words = ["Hi", "My ", "Name ", "Is ", "Henry "]
length = map(lambda x: "L" + x , words)
print(*list(length))

#   FILTER FUNCTION
words = ["Hi", "My ", "Name ", "Is ", "Henry "]
filtered = filter(lambda x: len(x)> 4, words)
print(list(filtered))

#   SORTED FUNCTION 
people = [
    {"Name" : "Alice", "Age": 24},
    {"Name" : "Bob", "Age" : 20},
    {"Name" : "Dhar", "Age": 19}
    ]
sorted_function = sorted(people, key=lambda people: people["Age"]) #reverse=True
print(sorted_function)

#   Enumerate Function
tasks = ["Write Report", "Finish English", "Write Script", "Science Project"]
for index, task  in enumerate(tasks):
    print(f"{index + 1}. {task}")
        
#   Zip function
names = ["Alice", "Bob", "Tom", "Joe", "Tim"]
ages = [13, 12, 34, 50]

combined = list(zip(names, ages))
for name, ages in combined:
    print(f"{name} is {ages} years old", end = " | ")
    
#   Open Function
with open("test.txt", "w") as file:
    file.write("Hello World")
    
#Palindrome Checker
def palindrome_check(word: str):
    if word == word[::-1].replace(" ", ""):
        print(f"{word} is a palindrome👍🏻")
    else:
        print(f"{word} is not a palindrome👎🏻")

palindrome_check("racecar")

#Fizzbuzz - multiples of 3 = Fizz, of 5 = Buzz, of both = FizzBuzz
def fizzbuzz():
    for i in range(1, 50):
        if i%3 == 0 or i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()

#Dictionary word count
def char_count(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict
print(char_count("Hello"))

#Anagram
def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if sorted(str1) == sorted(str2):
        print(f"{str1} is an anagram of {str2}")
    else:
        print(f"{str1} is not an anagram of {str2}")

anagram("listen", "silent")
anagram("evil", "vile")
anagram("hello", "world")

#Remove duplicates from a list and sort them 
def remove_dup(lst):
    seen  = set()
    x = [item for item in lst if item not in seen and not seen.add(item)]
    print(sorted(x))

remove_dup([1, 1, 3, 5, 4, 4])

love : str = "Katherine"
for i, index in enumerate(range(50)):
    print(f"{index}. I love you {love}")

from typing import List

fruits: List[str] = ["apple", "orange", "cherry", "banana"]

for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit} is my #{index+1} favorite fruit")

    """
    


s  : str = " hello world, welcome to the universe.  "
#Strip
s = s.strip()
#Convert to higher case
s = s.title()
#Replace words
s = s.replace("Universe", "Galaxy")
print(s)
#Check if the string ends with world
print(s.endswith("world"))
 