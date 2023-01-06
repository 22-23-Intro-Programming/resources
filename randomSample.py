import random


def main():

    x = random.randint(1, 10)
    print(x)

    L = ["Pierre", "Jackson", "Brad", "Asa", "Evan", "Ryan", "Jacob", "Rowan"]
    
    choice = random.choice(L)
    print(choice)

if __name__ == "__main__":
    main()
