from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    print("3 different numbers between 0 and 9 were drawn in random order.\n")
    return numbers

def take_guess():
    print("Enter 3 numbers one by one.")
    new_guess = []

    while len(new_guess) < 3:
        print("Enter the {}th number: ".format(int(len(new_guess)+1)))
        num = int(input())
        
        if num < 0 or num > 9:
            print("Out of range. Please enter agian.")
        elif num in new_guess:
            print("Already picked. Please enter again.")
        else:
            new_guess.append(num)
        
    return new_guess

def get_score(guesses, solution):
    position = 0
    strike_count = 0
    ball_count = 0
    
    for position in range(3):
        if guesses[position] == solution[position]:
            strike_count += 1
        elif guesses[position] in solution:
            ball_count += 1
    return strike_count, ball_count



# Game Start
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s_count, b_count = get_score(user_guess, ANSWER)
    s = int(s_count)
    b = int(b_count)
    tries += 1
    print("{}S {}B\n".format(s, b))
    
    if s == 3:
        break;


print("Congratulations! You matched the values and locations of all 3 numbers in {}.".format(tries))
