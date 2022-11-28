def palindrome():
    answer = input("Write something you think is a palindrome\n")

    last = len(answer)-1
    start = answer[0]

    i = 0 
    for char in answer:
        if (answer[0+i] != answer[last-i]):
            return False
        i = i + 1
        
    return True
        
        

def main():

    print(palindrome())


if __name__ == "__main__":
    main()
