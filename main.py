#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("This is a Python Password Generator!")
py_letters= int(input("How many letters would you like in your password?\n")) 
py_symbols = int(input(f"How many symbols would you like?\n"))
py_numbers = int(input(f"How many numbers would you like?\n"))

password = []




for character in range(1, py_letters+1): 
  password += random.choice(letters)


for character in range(1,py_symbols+1):
  password += random.choice(symbols)
  

for character in range(1, py_numbers+1):
  password += random.choice(numbers)

  
  random.shuffle(password)
  join_pass = ''.join(map(str,password))
print(f"The randomly generated password is: {join_pass}")



