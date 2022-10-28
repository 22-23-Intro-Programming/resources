

def main():

    fruits = ["apples", "watermelon", "kumquat", "pluot"]

    #dictionaries are defined as a set of 'key : value' pairs

    fruits2 = { "apples" : 1.25,
                "watermelon" : 2.50,
                "kumquat" : 0.65,
                "pluot" : 0.11,
                "canteloupe" : 2.50}

    print(fruits2)

    print(fruits2.get("apples"))

    #can't get a key based on its value
    #print(fruits2.get(2.50))

    fruits2.update({"mangoes" : 5.50})
    fruits2.update({"pluot" : 2.00})

    print(fruits2.get("mangoes"))

    print(fruits2)
    
    


if __name__ == "__main__":
    main()
