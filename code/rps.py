import random


def cpu():
  x = random.randint(0,2)
  if x == 0:
    cpu = "rock"
  elif x == 1:
    cpu = "paper"
  elif x == 2:
    cpu = "scissors"
  print (cpu)  
  return (cpu)
 
def compare(choice,cpu):
    if choice == "rock" and cpu == "scissors":
      print("You won.")
    elif choice == "rock" and cpu == "rock":
      print("You tied.")  
    elif choice == "paper" and cpu == "rock":
      print("You won.")
    elif choice == "paper" and cpu == "paper":
      print("You tied.")
    elif choice == "scissors" and cpu == "paper":
      print("You won.")
    elif choice == "scissors" and cpu == "scissors":
      print("You tied.")
    else:
      print("CPU won.")

  
def main():
  choice = input("Rock, Paper, Scissors? ")
  print(choice)
  cu = cpu()
  compare(choice,cu)
  
if __name__== "__main__":
  main()
