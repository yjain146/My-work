import random
import mysql.connector


''' We are creating a program where a user can play multiple mini games such as:
1) hangman
2) dice guessing game
3) number guessing game

Apart from these, we also have bingo card and housie board generators

The user will also be awarded points for every game they win'''

#creating a global variable points to keep track of a user's points
points=0


#This is the use of mysql connectivity
'''In this, They will create there account with details and will always login to play any game
In this we are planning to put information about the people if they ever want to save their progress 
and their points. They can carry on with the points as they go along.'''
#this is the start

#Mysql connectivity includes storing all the account details in a tabular form in a database specifically
# for this purpose. It will contain all the info about the players and there points. 


def mkdatabase():
    #to create a database in which all the data will be stored

    db=mysql.connector.connect(host="localhost",user="root",passwd="")
    cursor=db.cursor()
    cursor.execute("create database GameLab")

def mktable():       
    #Creating the table for information

    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")
    cursor=db.cursor()
    cursor.execute("create table Gamers(roll int primary key, nm char(20), srnm char(20),"
    "dob date, points int default 0, usernm varchar(20) not null, passwd varchar(20) not null)")

def roll():      
    #this is to assign them roll numbers which will be their unique identity

    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")
    cursor=db.cursor()
    cursor.execute("select roll from Gamers")
    roll=0

    for i in cursor:
        roll+=1
    return roll+1

def info():       
    #taking all the information from the user

    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")

    a=roll()
    b=input("Enter your First Name: ")
    c=input("Enter your Last Name: ")
    d=input("Enter your date of birth(in YYYY-MM-DD format): ")
    

    def username():
        e=input("Enter the username you would like to play with: ")
        a=roll()
        
        
        if a!=1:
            db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")
            cursor=db.cursor()
            cursor.execute("select usernm from Gamers")
            
            for i in cursor:
                while e in i:
                    print("This username already exists")
                    e=input("Enter another username: ")
                    continue

                else:
                    return e
            #to check if the usernm already exists or not
    e=username()

    f=input("Enter the password: ")
    g=input("Confirm password: ")

    if f==g:
        global points
        p=points
        
        data=(a,b,c,d,p,e,f)
        
        cursor=db.cursor()
        cursor.execute("insert into Gamers value(%s,%s,%s,%s,%s,%s,%s)",data)    
        
        #inserting all the information in the table
        
        db.commit()
        print(cursor.rowcount,"records inserted")


def sign():
    print("Before entering the game, you have to login in to view your points and save them")
    print("So you have 3 options: \n"
        "1) Sign in to your existing account \n"
        "2) Sign up to make a new account \n"
        "3) Play as guest (your points will not be saved) ")
    
    
    def signin():
        a=input("Enter your username: ")
        b=input("Enter your password ")
        user=(a,b)
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")
        cursor=db.cursor()
        cursor.execute("select usernm,passwd from Gamers")
        
        for i in cursor:
            if i==user:
                print("Welcome",a)
                return a
                break
        else:
            print("Either incorrect username or password!!")
            print("enter again!")
            signin()

    ch=int(input("What do you want to do: "))

    if ch==1:
        a=signin()
        return a

    elif ch==2:
        info()
        print("Welcome to our community of Gamers!! ")
        print("Sign in to continue: ")
        signin()
    
    elif ch==3:
        print("You are entering as a guest so your points will not be saved!!")
        return "guest"

a=sign()

def save():
    global a
    global points
    if a!="guest":
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")
        cursor=db.cursor()
        cursor.execute('update gamers set points=points+ %i where usernm="%s"' %(points,a))
        db.commit()
        print("Points updated, now exiting!!")
    else:
        print("You are logged in as Guest. Your points cannot be saved!")
        ch=input("Do you still want to exit? (y/n): ")
        if ch in ("yY"):
            print("Good bye see you soon!!")
            quit()
        else:
            main()

#this will print all the code numbers for different games
def inst():
    global a
    print('WELCOME TO THE FUN WORLD!! Mr.',a)
    print('following are the codes for different games:\n'
        '1 for hangman \n'
        '2 for dice guessing game \n'
        '3 for card guessing game')
    print('4 for bingo card generator \n'
        '5 for housie generator')
    print('6 for saving prgress and exiting the game \n'
        '7 for exiting without saving your progress \n'
        '8 for exiting \n'
        '9 for viewing your current points')

#for taking input of a game code number
def main():

    inst()
    
    while True:
        ch=int(input("enter a game code number: "))

        #for checking if the game code is correct or not
        if((ch>=1)and(ch<=9)):
            print('OK!')

            #for entering a specific game
            if ch==1:
                print('you are now going to enter the world of hangman!!')
                #insert game code here
                import random
                from word import word_list


                def get_word():
                    word = random.choice(word_list)
                    return word.upper()


                def play(word):
                    word_completion = "_" * len(word)
                    guessed = False
                    guessed_letters = []
                    guessed_words = []
                    tries = 6

                    print("Let's play Hangman! and you also enter words like , : and space")
                    print(display_hangman(tries))
                    print(word_completion)
                    print("\n")

                    while not guessed and tries > 0:
                        guess = input("Please guess a letter or word: ").upper()

                        if len(guess) == 1:

                            if guess in guessed_letters:
                                print("You already guessed the letter", guess)

                            elif guess not in word:
                                print(guess, "is not in the word.")
                                tries -= 1
                                guessed_letters.append(guess)

                            else:
                                print("Good job,", guess, "is in the word!")
                                guessed_letters.append(guess)
                                word_as_list = list(word_completion)
                                indices = [i for i, letter in enumerate(word) if letter == guess]

                                for index in indices:
                                    word_as_list[index] = guess
                                word_completion = "".join(word_as_list)

                                if "_" not in word_completion:
                                    guessed = True

                        elif len(guess) == len(word) and guess.isalpha():

                            if guess in guessed_words:
                                print("You already guessed the word", guess)

                            elif guess != word:
                                print(guess, "is not the word.")
                                tries -= 1
                                guessed_words.append(guess)

                            else:
                                guessed = True
                                word_completion = word

                        else:
                            print("Not a valid guess.")
                        print(display_hangman(tries))
                        print(word_completion)
                        print("\n")
                        
                    if guessed:
                        print("Congrats, you guessed the word! You win!")
                        print("You got 500 points!!")
                        global points
                        points+=500
                        
                    else:
                        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


                def display_hangman(tries):
                    stages = [  # final state: head, torso, both arms, and both legs
                                """
                                   --------
                                   |      |
                                   |      O
                                   |     \\|/
                                   |      |
                                   |     / \\
                                    -
                                """,
                                # head, torso, both arms, and one leg
                                """
                                   --------
                                   |      |
                                   |      O
                                   |     \\|/
                                   |      |
                                   |     / 
                                    -
                                """,
                                # head, torso, and both arms
                                """
                                   --------
                                   |      |
                                   |      O
                                   |     \\|/
                                   |      |
                                   |      
                                    -
                                """,
                                # head, torso, and one arm
                                """
                                   --------
                                   |      |
                                   |      O
                                   |     \\|
                                   |      |
                                   |     
                                    -
                                """,
                                # head and torso
                                """
                                   --------
                                   |      |
                                   |      O
                                   |      |
                                   |      |
                                   |     
                                    -
                                """,
                                # head
                                """
                                   --------
                                   |      |
                                   |      O
                                   |    
                                   |      
                                   |     
                                    -
                                """,
                                # initial empty state
                                """
                                   --------
                                   |      |
                                   |      
                                   |    
                                   |      
                                   |     
                                    -
                                """
                    ]
                    return stages[tries]


                def main():
                    word = get_word()
                    play(word)

                    while input("Play Again? (Y/N) ").upper() == "Y":
                        word = get_word()
                        play(word)


                if __name__ == "__main__":
                    main()

            

            elif ch==2:
                global a
                import random

                print('you will now be playing the dice guessing game!! Mr. ',a)
                print("We will generate a number from a dice and you need to to guess what will come \n"
                    "If you guess correctly you will be awarded points each time!")
                
                def ran(x=1):
                    c=0
                    for i in range(x):
                        d=random.randint(1,6)
                        c+=d
                    print("the number is: ",c)
                   
                    return c   
                    #this is to generate numbers which will later be guessed by the user.

                def game():
                    global points    #because this is ouside the definition
                    print("You can also select the number of dices you want. \n")
                    print("In case you're wondering now you have to guess the sum of the dices not individual numbers")
                    g=input("Do you want to select the number of dices (y/n): ")

                    if g in ("yY"):
                        f=int(input("Enter the number of dices you want: "))

                        d=int(input("Type the number you guess is right---> "))

                        c=ran(f)   
                        #calling the function with a variable to give the dice numbers                
                        
                        if d==c:
                            print("You were correct. Congratulations!!!!!!")
                            z=100*f
                            print("You have achieved %i points!" %z)
                            points+=z
                            #This is to be added to the points of the person as a result of the users
                            # hardwork.
                    
                        else:
                            print("You were wrong!")
                            print("Better luck next time!")

                    else:    
                        d=int(input("Type the number you guess is right---> "))
                        c=ran()  
                        #calling the function which we created to generate numbers

                        if d==c:
                            print("You were correct. Congratulations!!!!!!")
                            print("You have achieved 100 points!")
                            points+=100     
                            #This is to be added to the points of the person as a result of the users
                            # hardwork.
                    
                        else:
                            print("You were wrong!")
                            print("Better luck next time!")

                b=input("you have chosen the option of dice guessing game. \n"
                    "Are you sure you want to play or do you want to choose again? (y/n)---> ")
                
                while b in "Yy":
                    game()
                    
                    b=input("Do you want to try your luck again?(y/n)---> ")
                    
                    if b not in ("Yy"):
                        continue

            elif ch==3:
                print('you will now be playing the card guessing game!!')

                print("In this game we will generate one card and you have to guess which card will come next.\n"
                    "If you guess correctly you will be awarded 500 points as a prize.")
                import random

                def ran():
                    c=random.randint(1,13)
                    d=["spades","diamond","hearts","clubs"]
                    e=random.choice(d)
                    print("the card is: ",c," of",e)
                   
                    return c,e
                    #this is to generate cards which will later be guessed by the user.

                def game():
                    
                    d=int(input("Type the card number guess will come---> "))
                    f=input("Type the card suit you think will come---> ")
                    c,e=ran()
                    #calling the function which we created to generate cards
                    
                    if d==c and f.lower()==e:
                        print("You were correct. Congratulations!!!!!!")
                        print("You have achieved 500 points!")
                        global points    #because this is ouside the definition
                        points+=500     
                        #This is to be added to the points of the person as a result of the users
                        # hardwork.
                
                    else:
                        print("You were wrong!")
                        print("Better luck next time!")

                b=input("you have chosen the option of card guessing game. \n"
                    "Are you sure you want to play or do you want to choose again? (y/n)---> ")
                
                while b in "Yy":
                    game()
                    b=input("Do you want to try your luck again?(y/n)---> ")
                    
                    if b not in ("Yy"):
                        continue

            elif ch==4:
                print('Welcome to the bingo card generator!!')
                import random

                gridSize = 5
                minNum = 1
                maxNum = 50
                cards = int(input('enter the number of cards:'))

                for h in range(cards):
                    card = []
                    randRange = range(minNum, maxNum)
                    card = random.sample(randRange, gridSize * gridSize)

                    for i in range(gridSize):
                        string = ""
                        for j in range(gridSize):
                            string +=  str(card[i + j * gridSize]) + "  "
                        print(string)  

                    print('\n')                

            elif ch==5:
                print('Welcome to the housie board generator')
                #creating an empty list to store the numbers
                housienum=[]
                import random

                ''' creating a function for housie numbers
                and importing random to generate random numbers'''
                def tambola():
                    
                    num1=random.randint(1, 90)
                    housienum.append(num1)
                    print(num1, "is the first number")
                    n=1
                    while(n<=91):
                        num2=random.randint(1, 90)
                        if num2 in housienum:
                            if n==90:
                                print("done")
                                break
                            else:
                                continue

                        elif n==90:
                            break

                        else:
                            ch=input("Ready for the next number?(enter): ")
                            if ch==" ":
                                print(num2)
                                housienum.append(num2)
                    
                            else:
                                print(num2)
                                housienum.append(num2)
                        n+=1

                            
                tambola()
                print(len(housienum))
                print(housienum)
                continue
            
            elif ch==6:
                save()
                break
            
            elif ch==7:
                print("You are exiting without saving your progress")
                b=input("Do you want to continue? (y/n): ")

                while b in ("yY"):
                    quit()

                else:
                    c=input("Do you wish to save your progress and exit or play on? (play/save): ")
                    c=c.lower()

                    if c==("play"):
                        continue

                    elif c=="save":
                        save()

                    else:
                        for i in range(5):
                            while c not in ("play,save"):
                                if i==4:
                                    i="last"
                                print("This is your %s chance." %i)
                                c=input("Give a valid input: ")
                                break
                        print("You've exceeded the number of times you could input. \n"
                            "Now you have been kicked out of the game and your points are not saved!!")
                        quit()
            
            elif ch==8:
                print("See you next time!!!!!")
                quit()
                
            elif ch==9:
                if a!="guest":
                    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="GameLab")
                    cursor=db.cursor()
                    cursor.execute('select points from gamers where usernm="%s"' %a)

                    for i in cursor:
                        b=i[0]
                    global points
                    points+=b
                    print("Your points are: %i, Mr %s " %(points,a))

                else:
                    print("Your points are %i" %points)
                    print("This will not be saved because you're logged in as guest.")                    

        else:
            print('Invalid game code \n'
                'Enter a valid game code this time')
            continue
            #this takes the cursor to the beginning of the loop

main()        
#this starts the game