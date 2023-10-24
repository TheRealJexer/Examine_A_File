# create a code that shows the number of j's and d's in the "sample.txt" file

JD = "jd"
count = 0

with open("sample.txt", "r") as file:
    for i in file.read():
        if i.lower() in JD:
            count += 1

print("The number of J's and D's in the sample.txt file is", count)