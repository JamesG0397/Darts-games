def onePlayer(score):
  while score == 0:
    score = int(input("Please input the starting score"))

  #validCheck0 = False

  print("Your score is: " + str(score) + "\n" )
  while score > 0:
    #while validCheck0 == False:
      dart = int(input("Please input the score of your dart"))
      score = score - dart

      if score > 1:
        print(str(score) + " remaining\n")
      else:
        if score == 0:
          validCheck1 = False

          while validCheck1 == False:
            double = input("Was the last dart a double? (y/n)")
            if double == "y":
              print("Congratulations, you have checked out! \nWell played!\n")
              validCheck2 = False

              while validCheck2 == False:
                restart = input("would you like to play again? (y/n)")
                if restart == "y":
                  startup()

                elif restart == "n":
                  exitScreen()

                else:
                  print("Please enter a valid input(y/n)")


            elif double == "n":
              score = score + dart
              print("---Your last dart must be a double to check out.---\n")
              onePlayer(score)

            else:
              print("Please enter a valid input(y/n)")

        else:
          print("---You have gone bust.---\n")
          score = score + dart
          onePlayer(score)


def startup():
  print("Welcome to dartscore!")
  playerCount = input("Are there one or two players? ")

  if playerCount == str(1) or playerCount == "one":
    print("One player mode selected")
    onePlayer(0)

  elif playerCount == str(2) or playerCount == "two":
  #  print("Two player mode selected")
  #  twoPlayer()
    print("Unfortunatly the two player mode is still being developed. \n \n")
    startup()


  else:
    print("This program only supports one or two players. Please enter a suitable number \n \n")
    startup()

def exitScreen():
  print("Thank you for using dartscore, see you again.")
  print("[END]")
  quit()

startup()
