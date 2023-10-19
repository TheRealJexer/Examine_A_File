# create a code that sums the numbers together in a file
myFile = "C:\\Users\\jexer\\OneDrive\\Desktop\\Object Oriented Programming\\1019-main\\sample.txt"
num = 0
with open(myFile) as fh:
    for n in fh:
        n = n.strip()
        nums = n.split()
        for ns in nums:
            sum = sum + int(ns)


print(f"The sum of the numbers in the sample.ini file is: {sum}")