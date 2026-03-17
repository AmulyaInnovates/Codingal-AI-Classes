import random

print("Hey Hi how are you doing? Enter your name :- ")
name = input("Enter your name: ")
if name == "":
    name = "Friend"
print("Welcome user " + name)

age = input("How old are you? ")
if age.isdigit():
    age_int = int(age)
    if age_int < 13:
        print("You're a bright young mind!")
    elif age_int < 30:
        print("Great age to learn new things!")
    else:
        print("Age is just a number; keep exploring!")
else:
    print("Age can be tricky; no worries!")

print("How are you? good/bad? ")
response = input().lower()
if response == "good":
    print("Wow thats good to hear! Great going , lets connect later!")
elif response == "bad":
    print("Ohh sad to hear that , please try stress removal methods and I am here to help you always!")
else:
    print("Ohh its hard to put feelings away easily, so I understand completely!")

jokes = [
    "Why did the computer show up at work late? It had a hard drive.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the math book sad? It had too many problems."
]

facts = [
    "A group of flamingos is called a flamboyance.",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than a year on Venus."
]

while True:
    print("What would you like to do?")
    print("1) Hear a joke")
    print("2) Add two numbers")
    print("3) Tell me your hobby")
    print("4) Random fun fact")
    print("0) Exit")
    choice = input("Enter your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        print(random.choice(jokes))
    elif choice == "2":
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        if a.isdigit() and b.isdigit():
            print("Sum is", int(a) + int(b))
        else:
            print("I could not add those, try numbers.")
    elif choice == "3":
        hobby = input("What is your hobby? ")
        if hobby:
            print("Nice! " + hobby + " sounds fun.")
        else:
            print("No hobby? That's okay, everyone has different things they like.")
    elif choice == "4":
        print(random.choice(facts))
    else:
        print("I didn't understand that choice.")

print("Bye for right now, lets meet later !!!")
