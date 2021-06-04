# create a function that writes to a file, that prints the receipt
def filetowrite(file_name, user_results):
  with open(file_name, 'w') as f:
    
    f.write("This is your receipt :D: ")
    if user_results[0] == '1':
      f.write("You are watching Call of Jury Duty")
    elif user_results[0] == '2':
      f.write("You are watching Monkey vs Geico Lizard")
    elif user_results[0] == '3':
      f.write("You are watching The Adventures of Deez Nutty Squirrels")
    elif user_results[0] == '4':
      f.write("You are watching Zoomer to Boomer : Chris")
    elif user_results[0] == '5':
      f.write("You watching The Last Caprisun")
    # now check the show time
    if user_results[1] == '1':
      f.write("You are watching at 1:20pm")
    elif user_results[1] == '2':
      f.write("You are watching at 2:20pm")
    elif user_results[1] == '3':
      f.write("You are watching at 3:20pm")
    elif user_results[1] == '4':
      f.write("You are watching at 4:20pm")
    elif user_results[1] == '5':
      f.write("You are watching at 5:20pm")
    # now write the price they are paying
    f.write("total cost:" + str(user_results[2]))

# create a function that asks user what movie they wanna see, what time, and wealth people seat or cheap seat
def userinputs():
  user_results = []
  # first item: movie
  # second item: movie time
  # third item: seat chosen
  # 4th is cost
  
  print(
    "1. Call of Jury Duty.\n" +
    "2. Monkey vs Geico Lizard\n" +
    "3. The Adventures of Deez Nutty Squirrels\n" +
    "4. Zoomer to Boomer : Chris\n" +
    "5. The Last Caprisun \n"
  )
  # ask for input
  movieinput = input("Cuh what movie you wanna watch?")
  user_results.append(movieinput)
  print(
    "1. First Show: 1:20pm\n" +
    "2. Second Show: 2:20pm\n" +
    "3. Third Show: 3:20pm\n" +
    "4. Fourth Show: 4:20pm\n" +
    "5. Fifth Show: 5:20pm\n"
  )
  timeinput = input("Bro what time you tryna watch at?")
  user_results.append(timeinput)

  print(
    "1. $10\n" +
    "2. $50\n" +
    "3. $100\n" +
    "4. $1000\n" +
    "5. $96024\n"
  )

  # you gotta do something, if they type 1-5
  racksinput = input("Bestie how much money you tryna feed me?")
  if racksinput == "1":
    racksinput = 10
  elif racksinput == "2":
    racksinput = 50
  elif racksinput == "3":
    racksinput = 100
  elif racksinput == "4":
    racksinput = 1000
  elif racksinput == "5":
    racksinput = 96024

  user_results.append(taco_bell(racksinput))
  return user_results

  # within this function, calculate the costs, and return the 3 things they chose, as well as the total costs.
def taco_bell(racksinput):
  taxamount = 0.10 * racksinput
  return(taxamount + racksinput) #returning the total_amount

## main
user_results = userinputs()
filetowrite("new_receipt.txt", user_results)
