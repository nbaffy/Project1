import random
# from re import A

attempts_list = []
def show_score ():

  if len(attempts_list) <= 0:
    print("There is currently no high score")
    
  else:
    print("The current highscore is {} attempts". format(min(attempts_list)))

def start_game():
    random_number= int(random.randint(1,10))
    print("Welcome to the game of guesses")

    player_name = input("What is your name?")

    wanna_play = input ("Hi, {}, would you like to play? (Enter Y/N)".format(player_name))

    attempts = 0

    show_score()

    while wanna_play.lower() == "y":
       
        try:
            guess = input("Pick a number between 1 and 10")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the range")

                if int(guess) == random_number:
                    print("You got it!")

                    attempts += 1
                    attempts_list.append(attempts)

                    print("It took you {} attempts".format(attempts))

                    play_again = input("Would you like to play again? (Enter Y/N)")

                    attempts = 0

                    show_score()

                    random_number = int(random.randint(1,10))

                    if play_again.lower() =="n":

                        print("Come back soon")

                        break

                    elif int(guess) > random_number:
                        print("It's lower")

                        attempts += 1

                    elif int(guess) < random_number:
                            print("It's higher")
                       
                            attempts += 1

        except ValueError as err:
             print("That is not a valid value. Try again...")

             print("({})".format(err))
                            
        else:
             print("Come back soon")

if __name__ == '__main__':

       start_game()
