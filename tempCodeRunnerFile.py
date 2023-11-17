numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
number = input("Enter a positive number: ")

num = int(number)

if num < 10:
    print(numbers[num - 1])