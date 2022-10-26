
def main():

    myList = ["Brad", "Pierre", "Rowan", "Victor", "Jackson", "Richard", "Ryan", "Asa"]

    myList.insert(3, "Evan")
    print(myList)

    print(myList.pop(6))

    #access elements in a list
    #positions! just like characters in a string

    '''first = myList[0]
    print(first)
    second = myList[1]
    last = myList[-1]
    last = myList[len(myList) - 1]

    print(second, last)'''

    for i in range(len(myList)):
        print(myList[i])

    print(" ---- ")

    myList.append("Thomas")
    myList.remove("Rowan")

    for name in myList:
        if "o" in name:
            print("Wow, " + name + " has an 'o'")
        if len(name) < 4:
            print("small name! " + name)
     

if __name__ == "__main__":
    main()
