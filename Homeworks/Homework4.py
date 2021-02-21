import random as rnd
word=[]
class Hangman():
    
    def __init__(self):
        print("-----HANGMAN GAME-----")

    def RndWord(self):
        words=["peace","faith","funny","success","health","luck","friendship"]
        i=rnd.randint(0,6)
        RWord=[]
        RWord[:0]=words[i]
        return RWord
   
    def First_Print(self, w):
        print("\t")
        for i in range(len(w)):
            word.append("__")
            print(word[i],end=" ")
        print()

    def Control(self,w):
        for i in range(3):
            letter=input("guess a letter! : ")  
            letter=letter.strip()
            for j in range(len(w)):            
                 if letter==w[j]:
                      word[j]=letter
                 else:continue
            self.Print(w)
            selected=input("Do you want to guess the word?(y/n)")
            if(selected=="y" or selected=="Y"):
                self.Guess(w)
                break
            else:continue
        print("Game Over!")
    
    def Guess(self,w):
        str=""
        str=str.join(w)
        guess=input("Enter your guess: ")
        guess=guess.strip()
        if guess==str:
            print("\tYou guess it right! Congrets!")

        else:
            print(f"\tYou guess it wrong.The word was '{str}'")
    def Print(self,w):
        print("\t")
        for i in range(len(w)):
            print(word[i],end=" ")
        print()
        
game=Hangman()
rndword=game.RndWord()
game.First_Print(rndword)
game.Control(rndword)

