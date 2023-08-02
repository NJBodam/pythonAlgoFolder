
# Question 5:
# Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

# Write your code here

# HINT: create a dictionary from flowers.txt

def flowers():
    flowerdict = {}
    with open("flowers.txt") as f:
        for line in f:
            flower = line.strip().split(": ")
            flowerdict[flower[0]] = flower[1]
    return flowerdict

# HINT: create a function to ask for user's first and last name
def main():
    flowerdict = flowers()
    fullname = input("Enter your First [space] Last name only: ")
    firstname = fullname[0]
    firstname = firstname.capitalize()
    print("Unique flower name with the first letter: {}".format(flowerdict[firstname]))

if __name__ == '__main__':
    main()
# print the desired output

