name = input("Welcome to Mini Golf! What is your name? ")
holes = int(input("Hi " + name + "! Would you like to play 3 or 6 holes today? "))

score = []
if holes == 3:
    for i in range(holes):
        score.append(int(input(f"How many putts for hole {str(i + 1)}? (Par is 3) ")))
        x = sum(score)
        par = holes * 3

        if x <= par:
            print(f"Great job {name}! Your total score was {x - par}")
        elif x == par:
            print(f"Good game {name}. Your score was 0.")
        elif x >= par:
            print(f"Nice try {name}... Your score was {x + par}")

elif holes == 6:
    for i in range(holes):
        score.append(int(input(f"How many putts for hole {str(i + 1)}? (Par is 3) ")))
        x = sum(score)
        par = holes * 3

        if x <= par:
            print(f"Great job {name}! Your total score was {x - par}")
        elif x == par:
            print(f"Good game {name}. Your score was 0.")
        elif x >= par:
            print(f"Nice try {name}... Your score was {x + par}")

else:
    print("I'm sorry, but that is not an option for this course.")





