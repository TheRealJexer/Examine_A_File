# create a code that counts the total number of vowels in the "sample.txt" file

vowels = "aeiou"
count = 0

with open("sample.txt", "r") as file:
    for i in file.read():
        if i.lower() in vowels:
            count += 1

print("The number of vowels in the sample.txt file is", count)