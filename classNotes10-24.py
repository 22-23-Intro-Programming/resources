'''class Person:

    def __init__(self, hairColor, height, weight, name):
        self.hairColor = hairColor
        self.height = height
        self.weight = weight
        self.name = name
        self.alive = True

    #skill value 0-10
    def playSoccer(self, skill):
        if skill > 5:
            print("Wow, he scored!")
        elif skill > 1:
            print("Wow, he missed!")
        else:
            self.alive = False

    def getAlive(self):
        return self.alive'''

def main():

     '''mrC = Person("blonde", "6 feet", "200 lbs", "Mr. Considine")
     mrC.playSoccer(7)
     mrC.playSoccer(3)
     print(mrC.alive)
     mrC.playSoccer(1)
     print(mrC.alive)'''

     myS = ""
     print(myS)

     #concatenate
     newS = "Mr. " + "Considine"
     print(newS)

     #for loop - repeat code . i starts at 0 and goes to 4
     for i in range(5):
         #print(i)
         myS = myS + "python "

     print(myS)

     '''for i in range(len(newS)):
         print(newS[i])'''
         #can error
         #if newS[i] == " ":

             #newS = "Mr. Philips"

     i = 0
     while (i < 11):

         if newS[i] == " ":
             newS = newS.replace(newS[i], "-") 
         i = i+1

     print(newS)












     
     

if __name__ == "__main__":
    main()
