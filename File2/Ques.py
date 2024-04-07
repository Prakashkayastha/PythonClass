# a) Create a file Myself.txt and store information about yourself received through terminal
information = input("Enter information about yourself: ")
with open("Myself.txt", "w") as file:
    file.write(information)

# b) Copy the content of Myself.txt to backup.txt
with open("Myself.txt", "r") as file:
    data = file.read()
    with open("backup.txt", "w") as backup_file:
        backup_file.write(data)

# c) Read the contents of Myself.txt and reverse it and store it in the Myself.txt
with open("Myself.txt", "r+") as file:
    content = file.read()
    reversed_content = content[::-1]
    file.seek(0)
    file.write(reversed_content)

# d) Read the contents of Myself.txt and compare it with the content of backup.txt to find palindrome strings
with open("Myself.txt", "r") as myself_file:
    myself_data = myself_file.read().split()

with open("backup.txt", "r") as backup_file:
    backup_data = backup_file.read().split()

palindromes = [word for word in myself_data if word == word[::-1] and len(word) > 1]

if palindromes:
    print("Palindromes found:", ", ".join(palindromes))
else:
    print("No palindromes found.")

# e) Delete the file backup.txt in python
import os
os.remove("backup.txt")
print("backup.txt deleted.")
