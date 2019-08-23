# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
# numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


### I copied the concept form the solution 

import random

a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*+_"
k = int(input("Enter the length of the password. Usually 8 to 10: "))

pass_gen = random.sample(a, k)
final_pass = "".join(pass_gen)

print(final_pass)







