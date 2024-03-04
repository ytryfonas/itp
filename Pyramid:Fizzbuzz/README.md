## Pyramid HW

### Process:

   To achieve the result of the pyramid, I noticed that at each row, there are always ten characters, some spaces, and some '#'. The spaces are incrementing by -1 character per row while the '#' is incrementing by 1 each row, keeping the total character count per row 10. That gave me the idea to create a 'for' loop with a range determined by the user (1-8). In that loop, there are two variables, one for the count of spaces and one for the count of '#', that are either incrementing by 1 or -1, respectively. The variables multiplied by either '#' or space are printed before their values are changed for the loop. If the user inputs any number outside 1-8, the program prints 'stack has to be between 1-8'.

### Troubleshooting:

- I initialized variables after the for loop so the code wouldn't run.

- I had my variables the other way around in the for loop so the pyramid was on the left.

## FizzBuzz HW

### Process:

   For this assignment, I created a for loop from 1 to 100 (by having a range of 1, 101). Inside the loop I put an if statement that looks if the current value of i is divisible by both 3 and 5. This had to be first to prevent printing only 'Fizz' or 'Buzz'. Then using two elif statements I look if i is divisible by 3 or 5 respectively. If all of those conditions are not met then the program just prints the current value of i and then increments by 1.

### Troubleshooting:

- I tried writing the program with range(100) and having a different variable that increments by one with each repetition, but I realised I can just make the range from 1-101 and use the i as my variable for comparisons and printing.

## Code used

- All the code I used was from the controlflow README.md file from the class github page, mostly the 'For' and 'For with range' section.
