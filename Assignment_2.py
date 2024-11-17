# List the all the functions available for the String data Type.
# e.g len()
string_str=input("Enter any string is:- ")
uppercase=string_str.upper()
lower_case=string_str.lower()
length=len(string_str)
capitalize=string_str.capitalize()
count=string_str.count("apple")
split=string_str.split()
print("Uppercase in the sentence is:- "+uppercase)
print("Lower case in the sentence is:- ",lower_case)
print("Capitalize in the sentence is:- ",capitalize)
print("Reapeated word count in the senetence is:- ", count)
print(split)
print(len(split))

# Replace
name = "Hi Hello, How are you Hello, You're so awesome Hello"
print(name.replace("Hello", "Hari"))

print(string_str.replace(" ", ""))
print(string_str.endswith(" fruit"))
print(string_str.find("apple"))


fruits=("Apple", "Mango", "Guva")
fruit=".".join(fruits)
print(fruit)

# Swap case
print(string_str.swapcase())