# create a code that does all three functions that main.py, main2.py, and main3.py do in one

vowels = "aeiou"
count = 0

def numberOfVowels(count):
    """This function calculates the amount of vowels in the sample.txt file"""
    with open("sample.txt", "r") as file:
        for i in file.read():
            if i in vowels:
                count += 1
    return count

totalVowels = numberOfVowels(count)

JD = "jd"
count = 0

def numberOfJandD(count):
    """This function counts how many J's and D's there are in the sample.txt file"""
    with open("sample.txt", "r") as file:
        for i in file.read():
            if i in JD:
                count += 1
    return count

totalJandD = numberOfJandD(count)

specialCharacters = "=[];_.@"
count = 0

def numberOfSpecialCharacters(count):
    """This function counts how many special charachets there are in the sample.txt file"""
    with open("sample.txt", "r") as file:
        for i in file.read():
            if i in specialCharacters:
                count += 1
    return count

totalSpecialCharacters = numberOfSpecialCharacters(count)

# these print commands display the results
print(f"The number of vowels in sample.txt is {totalVowels}")
print(f"The number of J's and D's in sample.txt is {totalJandD}")
print(f"The number of special characters in sample.txt is {totalSpecialCharacters}")
