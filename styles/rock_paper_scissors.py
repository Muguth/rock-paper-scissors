import random

random = random.randrange(1,4)
move = int(input("Enter your move (1 for rock , 2 for paper or 3 for scissors)\n"))
player_move = ""
bot_move = ""

wins = 0
bot_wins = 0
draws = 0

if move == 1:
    player_move = "rock"
elif move == 2:
    player_move = "paper"
elif move == 3:
    player_move = "scissors"

if random == 1:
    bot_move = "rock"
elif random == 2:
    bot_move = "paper"
elif random == 3:
    bot_move = "scissors"

print(f"Player played {player_move}")
print(f"Computer played {bot_move}")

if player_move == bot_move:
    print("draw")
    draw =+ 1
elif player_move == "rock" and bot_move == "scissors":
        wins =+ 1
        print("player wins")
elif player_move =="paper" and bot_move == "rock":
        wins =+ 1
        print("player wins")
elif player_move =="scissors" and bot_move == "paper":
        wins =+ 1
        print("player wins")
elif bot_move == "rock" and player_move == "scissors":
        bot_wins =+ 1
        print("bot wins")
elif bot_move =="paper" and player_move == "rock":
        bot_wins =+ 1
        print("bot wins")
elif bot_move =="scissors" and player_move == "paper":
        bot_wins =+ 1
        print("bot wins")

