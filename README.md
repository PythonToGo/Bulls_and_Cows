# Bulls_and_Cows

Bulls and Cows is a 2 player game. One player thinks of a number, while the other player tries to guess it. The number to be guessed must be a 4 digit number, using only digits from 1 - 9, each digit atmost once.


## Rules:

- The computer randomly selects three different numbers between 0 and 9.
- The user must guess the value and position of the numbers selected by the computer.
- The computer tells the user the number of strikes (S) and balls (B) for the three numbers entered by the user according to the following rules:
  - If the value and position of the number match, it's an S.
  - If the value of the number matches but the position is wrong, it's a B.
- There is no limit to the number of attempts, but the number of attempts is recorded.
- The game ends when 3S (matching all three numbers in value and position) is achieved.

## Gameplay:

1. "The computer has randomly selected three different numbers between 0 and 9 in random order." is displayed.
2. "Please enter three numbers one by one." is displayed.
3. "Enter the 1st number:" is displayed, and the user enters their input. Similarly, "Enter the 2nd number:" and "Enter the 3rd number:" are displayed, and the user enters their input for each. If the user enters a duplicate number or a number outside the range, they will be asked to input again.
4. If the user enters the three numbers correctly, "*S *B" is displayed according to the rules.
5. If 3S is not achieved, the game restarts from step 2.
6. If the user achieves 3S, "Congratulations. You have matched all three numbers in * attempts." is displayed, and the game ends.

## Functions
'generate_numbers()'

Randomly picks 3 different numbers between 0 and 9 and returns a list containing those numbers.

'take_guess()'
After repeatedly inputting 3 numbers from the user, the numbers entered by the user are organized in a list and returned.

'get_score'
This function takes two parameters.
'guesses' → a list of 3 numbers chosen by the user
'solution' → A list of 3 correct numbers selected by the computer
Compares the two lists to calculate and return the number of strikes and balls.


## Example of gameplay:

Here is a result sample.
The computer has randomly selected three different numbers between 0 and 9 in random order.

  '''
  Please enter three numbers one by one.
  Enter the 1st number: 2
  Enter the 2nd number: 2
  Duplicate number. Please enter again.
  Enter the 2nd number: 11
  Number out of range. Please enter again.
  Enter the 2nd number: 3
  Enter the 3rd number: 8
  1S 1B

  Please enter three numbers one by one.
  Enter the 1st number: 8
  Enter the 2nd number: 2
  Enter the 3rd number: 0
  1S 2B"""

  Please enter three numbers one by one.
  Enter the 1st number: 2
  Enter the 2nd number: 8
  Enter the 3rd number: 0
  3S 0B

  Congratulations. You have matched all three numbers in 3 attempts.
  '''

Enjoy!
