#question 1
print("question 1")
number_item = int(input("Enter the number of items you want to purchase: "))
discount = "Discount applied" if number_item > 3 else "No discount"
print(discount)

#question 2
print("\n\nquestion 2")
def get_expensive(prices):
    expensive_items = [price for price in prices if price > 100]
    return expensive_items

prices = [120, 45, 300, 85, 150]
print(get_expensive(prices))

#question 3
print("\n\nquestion 3")
with open("week2_exercises/log.txt", "a") as file:
    file.write("User logged in\n")
with open("log.txt", "r") as file:
    log_history = file.read()
    print(log_history)

#question 4
print("\n\nquestion 4")
def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"
grades = {'Ab': 'A', 'Ac': 'B', 'Ad': 'C'}
print(get_grade(grades, 'Ab'))
print(get_grade(grades, 'Ae'))

#question 5 & 6
print("\n\nquestion 5 & 6")
list_of_sales = []
try:
    with open("week2_exercises/sales.txt", "r") as file:
        for line in file:
            try:
                sale = int(line.strip())
                list_of_sales.append(sale)
            except ValueError:
                continue
    print(sum(list_of_sales))
except FileNotFoundError:
    print("File not found.")

#question 7
print("\n\nquestion 7")
number7 = int(input("Enter a number: "))
output_list = []
for i in range(1, number7 + 1):
    if i % 3 == 0 and i % 5 == 0:
        output_list.append("FizzBuzz")
    elif i % 3 == 0:
        output_list.append("Fizz")
    elif i % 5 == 0:
        output_list.append("Buzz")
    else:
        output_list.append(str(i))
print(output_list)

#question 8
print("\n\nquestion 8")
nums8 = [0, 1, 0, 3, 12]
pointer = 0

for current in range(len(nums8)):
    if nums8[current] != 0:
        nums8[pointer] = nums8[current]
        pointer += 1

for i in range(pointer, len(nums8)):
    nums8[i] = 0

print(nums8)

#question 9
print("\n\nquestion 9")
nums9 = [2, 7, 11, 15]
target = 9
num_dict = {}
for i, num in enumerate(nums9):
    complement = target - num
    if complement in num_dict:
        print([num_dict[complement], i])
        break
    num_dict[num] = i

#question 10
print("\n\nquestion 10")
number10 = input("Enter a number: ")
is_palindrome = number10 == number10[::-1]
print(is_palindrome)

#question 11
print("\n\nquestion 11")
number11 = int(input("Enter a number: "))
sqrt = 0
while sqrt * sqrt <= number11:
    sqrt += 1
sqrt -= 1
print(sqrt)

#question 12
print("\n\nquestion 12")
total = 0
try:
    with open("week2_exercises/numbers.txt", "r") as file:
        for line in file:
            try:
                number = int(line.strip())
                total += number
            except ValueError:
                continue
    print(total)
except FileNotFoundError:
    print("File not found.")

#question 13
print("\n\nquestion 13")
try:
    with open("week2_exercises/message.txt", "r") as file:
        content = file.read()
    print(content.upper()) 
except FileNotFoundError:
    print("File not found.")

#question 14
print("\n\nquestion 14")
scores = {"John": 85, "Sara": 92, "Fraol": 78}
student_name = input("Enter the student's name: ")
try:
    score = scores[student_name.capitalize()]
    print(score)
except KeyError:
    print("Student not found!")

#question 15
print("\n\nquestion 15")
from collections import Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
counter_dict = Counter(words)
print(dict(counter_dict))

#question 16
print("\n\nquestion 16")
original_dictionary = {"John": "A", "Sara": "B", "Musa": "A"}
updated_dictionary = {}
for key, value in original_dictionary.items():
    if value not in updated_dictionary:
        updated_dictionary[value] = [key]
    else:
        updated_dictionary[value].append(key)
print(updated_dictionary)

