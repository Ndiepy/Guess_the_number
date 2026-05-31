from colorama import Style,Fore,Back,init
from random import randrange
import time 
import os
init(autoreset=True) #Desactive le changement de couleur ou de style d'un print à un autre

#fonctions
def loadings_dots(text):
    for i in range(4):
        print(f"\r{text}{'.'*i}",end=" ")
        time.sleep(0.5)
    

def rules():
    loadings_dots('Welcome to Guess the Number')
    loadings_dots("The rules of this game are very easy")
    print(
        """
 First,the bot chooses a random number in a specific interval.
 Next ,you'll have to try to find this number several attempts.
 if you run out of attempts before finding the answer , you lose .Otherwise ,you win.

        """
    )
    
    time.sleep(0.5)
    print("Nice Play")

#classe du jeu
class Game():
    def __init__(self,player):
        self.level=1
        self.player=player
        self.attempts=0
        self.bot_number=0
        self.max_attempts=0
        self.score=0
        
    def interval(self) :
        if self.level==1:
            a=1
            b=10
        elif self.level==2:
            a=1
            b=25
        elif self.level==3:
            a=1
            b=50
        elif self.level==4:
            a=1
            b=100
        elif self.level==5:
            a=1
            b=500  
        return [a,b] 
    def set_attempts(self):
        if self.level==1:
            self.attempts=3
            self.max_attempts=3
        elif self.level==2:
            self.attempts=5
            self.max_attempts=5
        elif self.level==3:
            self.attempts=7
            self.max_attempts=7
        elif self.level==4:
            self.attempts=10
            self.max_attempts=10
        elif self.level==5:  
            self.attempts=15  
            self.max_attempts=15
       
    def get_number(self):
        interval=self.interval()
        a=interval[0]
        b=interval[1]
        self.bot_number=randrange(a,b+1)

    def message_box(self):
        greetings=[f"Welcome {self.player}",f"Ready to play,{self.player}?",f"{self.player}, let's get started !"]
        number_is_lower=["Too high! Try a smaller number.","Nope , go lower!","The number is less than that.Try again!"]
        number_is_higher=["Too low! Try a bigger number.","Nope , go higher!","The number is greater than that.Try again!"]
        attempts=[f" You have {self.attempts}",f"{self.attempts} turn left",f"Only {self.attempts} turns to go"]
        victory=["Congratulations! You won!","Awesome! You're the Strongest ."," Great ! You did it ."]
        defeat=[f"Sorry, You lose the secret number was {self.bot_number} . ",f"Game over ! The number was {self.bot_number} .",f"Defeat ! I chose {self.bot_number} and you couldn't find it."]
        messages= [greetings,number_is_higher,number_is_lower,attempts,victory,defeat]
        return messages
    
    def spawn_message(self,message):
            messages=self.message_box()
            message_dict={
                'greetings': 0 ,
                'number_is_higher': 1,
                'number_is_lower' : 2,
                'attempts' : 3,
                'victory' : 4,
                'defeat' : 5
            }
            lst=messages[message_dict[message]]
            return lst[randrange(len(lst))]
    def level_loop(self,choice) :  
        #Boucle du jeu pour un niveau specifique
        while True:     
            self.level=choice
            interval=self.interval()
            self.set_attempts()
            print(self.spawn_message('greetings'))
            loadings_dots(Fore.BLUE+"Bot "+Fore.RESET+ ": Please wait I'm Choosing my Number ")
            self.get_number()
            print(Fore.BLUE+"\nBot "+Fore.RESET+": Finished ")
            
            
            while True:  
                try:
                    choice_number= int(input(f"\nEnter a number between {interval[0]} and {interval[1]} : ")) 
                except ValueError:
                    print("Enter an integer!!!") 
                else:  
                    if choice_number== self.bot_number:
                        print(Fore.BLUE+"Bot"+Fore.GREEN+Style.BRIGHT+ ": " +self.spawn_message('victory'))
                        self.score=int(self.attempts*1000/self.max_attempts)
                        print(Fore.LIGHTCYAN_EX+f"YOUR SCORE : {self.score}")
                        break 
                        
                        
                    elif choice_number > self.bot_number:
                        self.attempts-=1
                        print(Fore.BLUE+"Bot"+Fore.CYAN+": " +self.spawn_message('number_is_lower')) 
                        if self.attempts>0:
                            print(Fore.BLUE+"Bot"+Fore.LIGHTRED_EX+": " +self.spawn_message('attempts'))
                    elif choice_number < self.bot_number:
                        self.attempts-=1
                        print(Fore.BLUE+"Bot"+Fore.MAGENTA+": " +self.spawn_message('number_is_higher'))
                        if self.attempts>0:
                            print(Fore.BLUE+"Bot"+Fore.LIGHTRED_EX+": " +self.spawn_message('attempts'))    
                    if self.attempts == 0:
                        print(Fore.BLUE+"Bot "+Fore.RED+Style.BRIGHT+": " + self.spawn_message('defeat'))  
                        break
            replay= input("restart this level [o/n]? : ")
            if replay.lower() !='o':
                break        

#Menu principal

print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+ "Guess The Number".center(34,'='))
name= input("Enter your name : ")

#boucle du jeu
while True :
    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+
    """
    1. Rules 
    2. Play
    3. Exit
    """
    )
    choice=input("Make choice : ")
    if choice == '1' :
        time.sleep(1)
        rules()
        
    elif choice == '2' :
        game=Game(name)
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+
            """
            1. Level 1
            2. Level 2
            3. Level 3
            4. Level 4
            5. Level 5
            6. Exit 
            """
        )
        choice= input("Make a choice : ")
        if choice == '1':
            game.level_loop(1)  
        elif choice == '2':
            game.level_loop(2)
        elif choice == '3':
            game.level_loop(3)
        elif choice == '4':
            game.level_loop(4)
        elif choice == '5':
            game.level_loop(5)
        elif choice == '6':
           print(Style.BRIGHT+Fore.CYAN+"Thanks For Playing")
           time.sleep(2)
           os.system('cls' if os.name=='nt' else 'clear')
           break
        else:
            print(Fore.RED+"Enter a correct choice")
                           
    elif choice == '3':
        print(Style.BRIGHT+Fore.CYAN+"Thanks For Playing")
        time.sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
        break

    else:
        print(Fore.RED+"Enter a correct choice")




