print("Maryna")
print("Rymkevich")

name = 'Marina'
age = 38
height = 164
is_student = "yes"
print(name, type(name), age, type(age), height, type(height), is_student, type(is_student))

age = str(age)
height = str(height)
is_student = bool(is_student)
print(name, type(name), age, type(age), height, type(height), is_student, type(is_student))

number = 13
number_2 = 3
print(number + number_2, number / number_2, number * number_2, number % number_2, number // number_2)


current_year = 2026
user_name = input("Please enter your name: ")
user_birh_year = input("Please enter year of bith: ")
print(f"Hi, {user_name.strip()}! Your age is: {current_year - int(user_birh_year)}")


price = float(input("Please enter the price: "))
discount = float(input("Please enter discount: "))
final_price = float(price * (100 - discount) / 100)
print(f"The final price is: {final_price:.2f}")
print(f"The final price is: {round(final_price, 2)}")
print("The final price is: " + str(round(final_price, 2)))



temparature_cels = float(input("Enter the temperature: "))
print(f"F is: {round(temparature_cels * 9 / 5 + 32, 2)}")

text = "Hi, my name is Marina"
print(len(text), text.lower(), text.upper(), text.strip())


length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}, Perimeter: {perimeter}")
# If the user enters 'hello', we will have a ValueError


first_name = input("Please enter your first name: ").strip()
last_name = input("Please enter your last name: ").strip()
print(f"The full name is: {first_name} {last_name}")


text = "python programming"
print(text[0])
print(text[-1])
print(text[:6])
print(text[-11:])
print(text[::-1])

first_name = input("Enter first name: ").strip().lower()
last_name = input("Enter last name: ").strip().lower()
username = first_name[:3] + last_name[:5]
print(f"Username: {username}")


email = "marina@gmail.com"
username, domain = email.split('@')
print("Username:", username)
print("Domain:", domain)


sentence = "Java is a difficult language."
new_sentence = sentence.replace("Java", "Python")
print("Original:", sentence)
print("Changed:", new_sentence)


# Part D

text = "Python Programming"
print(text[0])       # 'P'
print(text[-1])      # 'g'
print(text[:6])      # 'Python'
print(text[7:])      # 'Programming'
print(text[2:5])     # 'tho'
print(text[-11:-1])  # 'Programmin'
print(text[::2])     # 'Pto rgamng'
print(text[::-1])    # 'gnimmargorP nohtyP'



text = 'Artificial Intelligence'
slice1 = text[:5]     # 'Artif' (from start to 5th character)
slice2 = text[5:]     # 'icial Intelligence' (from 5th character to end)
slice3 = text[2:7]    # 'tific' (from 2nd to 7th character)
slice4 = text[-12:]   # 'Intelligence' (from 12th character from the end to end)
slice5 = text[11::3]  # 'Inen' (from 11th character to end with step 3)
slice6 = text[9::-1]  # 'laicifitrA' (from 9th character back to start reversed)



text = "  user_admin_2026  "
print(text.strip().split("_"))              # ['user', 'admin', '2026']
print(text.strip())                         # 'user_admin_2026'
print(text.replace("2026", "2027"))         # '  user_admin_2027  '
print("admin" in text)                      # True


text = "Python"
# text[0] = "J"  # TypeError: 'str' object does not support item assignment
new_text = "J" + text[1:]
print(new_text)  # 'Jython'


# Part E

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
full_name = f"{first_name} {last_name}"
city = input("Enter city: ").strip()
birth_year = input("Enter year of birth: ").strip()
language = input("Enter favourite programming language: ").strip()

user_id = f"{first_name[:3].lower()}{last_name[:3].lower()}{birth_year[-2:]}"

print("SUMMARY")
print(f"Full Name: {full_name} born in {birth_year}")
print(f"User ID: {user_id}")
print(f"City: {city}")
print(f"Favourite Language: {language}")

print(f"{first_name[0].upper()}.{last_name[0].upper()}.")
print(f"{len(full_name.replace(' ', ''))}")
print(f"Favourite Language reversed: {language[::-1]}")
print(f"Approximate Age: {2026 - int(birth_year)}")
print(f"Loves Python: {"python" in language.lower()}")
print(f"is from Belarus: {"minsk" in city.lower()}")


# Part F

total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{hours}h {minutes}m {seconds}s")


number = 2345
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10
print(digit1, digit2, digit3, digit4)


word = "python"
masked_word = word[:2] + "*" * (len(word) - 4) + word[-2:]
print(masked_word)



print(int(3.9) + float("2.5"))  # Answer: 5.5
print("Developer"[1:7:2])  # Answer: 'evl'
print("Python"[-4:-1])  # Answer: 'tho'
print(27 // 5 + 27 % 5)  # Answer: 7
print("a" + "b" * 3)  # Answer: 'abbb'