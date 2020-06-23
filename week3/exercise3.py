"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("Guessing game started!")
    print("A number higher than _ ?")
    a = False
    while a == False:
      b1 = False
      while b1 != True:
        lowerBound = input("Enter a lower Bound: ")
        try:
          int(lowerBound)
          b1 = True
        except ValueError:
          print("integer only")
          b1 = False
      b2 = False
      while b2 != True:
        upperBound = input("Enter a upper Bound: ")
        if upperBound > lowerBound:
          try: 
            int(upperBound)
            a = True
            b2 = True
          except ValueError:
            print("integer only")
            upperBound = input("Enter a upper Bound: ")
            b2 = False
        else:
            print("lowerbound must be lower than upperbound")
            b2 = False
      print("cool, a number between" + str(lowerBound) + "and" + str(upperBound))

    upperBound = int(upperBound)
    lowerBound = int(lowerBound)
    actualnumber = random.randint(lowerBound, upperBound)

    guessed = False
    while not guessed:
      answer = False
      while answer != True:
        guessednumber = input("Guess a number:")
        try:
          int(guessednumber)
          answer = True
        except ValueError:
            answer = False
            print("integer only pls")
      print("You guessed {},".format(guessednumber),)
      if int(guessednumber) == actualnumber:
        print("It was {}!".format(actualnumber))
        guessed = True
      elif int(guessednumber) < actualnumber and int(guessednumber) > lowerBound:
        print("oops too small")
      elif int(guessednumber) > actualnumber and int(guessednumber) < upperBound:
        print("aha too big mate")
      elif int(guessednumber) < lowerBound:
        print("what the heck are you doing")
      elif int(guessednumber) > upperBound:
        print("what the heck are you doing")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
