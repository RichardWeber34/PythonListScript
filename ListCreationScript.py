import MakeRandomList
import QuickSortList

""" This asks for user inputs for a range and an amount and then creates a random list and prints it.
    it will then sort that list and print it again and give some random information about the list"""

lower = int(input("Please enter an integer for the lower bound for the generated numbers: "))

print("Thanks\n")

upper = int(input("Please enter a larger integer to be the upper bound: "))

while lower >= upper:
    print("\nThe lower bound isn't actually any lower than the upper.\nPlease sort it out and try again\n")
    end = int(input("Please enter a larger integer to be the upper bound: "))

print("Nice one\n")

num = int(input("How long do you want the list to be? "))

while num < 1:
    print("\nYou must be joking... This isn't going to work if the length is less than 1.\n")
    num = int(input("How long do you want the list to be? "))

informationString = "| Producing a " + str(num) + " integer long list, whose elements range in value from " + str(lower) + " to " + str(upper) + " |"

print("\n" + len(informationString) * "=")
print(informationString)
print(len(informationString) * "=" + "\n")


generatedList = MakeRandomList.Rand(lower, upper, num)
print("Ite, it's done:")
print(generatedList)

QuickSortList.quickSort(generatedList, 0, num-1)

print("\nand this is it after a quick QuickSort:")

print(generatedList)

largest = lower
smallest = upper

total = 0

for i in generatedList:
    total += i

    if i > largest:
        largest = i
    
    if i < smallest:
        smallest = i

if num % 2 == 0:
    median = generatedList[num/2]
else:
    median = (generatedList[num//2] + generatedList[(num//2)+1]) / 2

print("\nNumbers add up to a total of: " + str(total))

average = total/len(generatedList)

print("\nWith an average of: " + str(average))

print("\nThe largest number is " + str(largest) + "...")
print("... and the smallest is " + str(smallest))

print("\nand your median is " + str(median))

print("\nPeace, bredda. I'm out.")
    