def startup():
  print("Welcome to dartscore!")
  playerCount = input("Are there one or two players?")

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

def scorer(score):
  for i in range(3):
    dart = int(input("Dart " + str(i) + ":"))
    score = score - dart
    if score < 1:
      checkoutCheck(score, dart)







def onePlayer(score):
  while score == 0:
    score = int(input("Please input the starting score"))
    print(score)
    scorer(score)







startup()
