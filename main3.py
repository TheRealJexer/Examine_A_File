# create a code that shows the number of special characters in the "sample.txt" file

specialCharacters = "=[];_.@"
count = 0

with open("sample.txt", "r") as file:
    for i in file.read():
        if i.lower() in specialCharacters:
            count += 1

print("The total number of special characters in the sample.txt file is", count) 
