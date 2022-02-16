# Wordle Game
import random
import os
import csv

def recurse(tries=6):
    
    # with open(r"C:\Users\jiwoo\Documents\words.txt") as word_file:
    #     words = word_file.readline().split() #This splits by whitespace, if you used some other delimiter specify the delimiter here as an argument.
    #     word = random.choice(words)
    word = "TOUGH"
    word = word.upper()
    
    count = 0


    while count != 6:
        guessedWords = input("please enter a word: ")
        length = len(guessedWords)
        if length != 5:
            print("\nError please enter a 5 letter word\n")
            recurse(tries = tries)

        guessedWord = guessedWords.upper()


        answerLetters = []

        for place in word:
            answerLetters += place

        guessedLetters = []

        for letter in guessedWord:
            guessedLetters += letter

        neededLetters = []

        for x in guessedLetters:
            if x in answerLetters:
                neededLetters += x

        for i in neededLetters:
            index = guessedLetters.index(i)
            if i in answerLetters:
                indexA = answerLetters.index(i)
            if index == indexA:
                guessedLetters[index] = i+"!"
            else:
                guessedLetters[index] = i+"?"

        for i in guessedLetters:
            for x in i:
                if x == "!":
                    count += 1

        
    
        
        print("\n")
        print(guessedLetters)
        tries -= 1
        print("\n")
        print("Tries left: {}".format(tries))
        if tries == 0:
            print("Out of tries! The word was {}".format(word))
            exit()
        if count == 6:
            print("Congrats you got the word: {}".format(word))
        else:
            count = 0


if __name__=="__main__":
    recurse()
