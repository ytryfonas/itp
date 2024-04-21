## Assignment Chessboard

### My process

  - My thought process was creating a nested for loop (similar to the midterm project). The outer loop determines the current row and after the inner loop is done it adds a new line (\n) and increments by 1. The inner loop checks to see if the sum of i + j is even or odd, that way we can alternate between spaces and # for the current row (e.g. first loop i+j=2 so b += ' ', then j increments by 1 so i+j=3(odd) so b += '#'). When the outer loop reaches the size of the board it ends and then the board is printed. Also in the beginning I initialize the size and board variables. The size variable remains unchanged so I declared it as 'const'.   

### Troubleshooting

  - I was having trouble writing my program in javascript so I decided to do it in python and then using the resources below translate it into javascript. My python code:

  ```python
b = ''
size = 8

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            b += ' '
        else:
            b += '#'
    b += '\n'

print(b)
  ```

### Code Used/Referenced

  - https://www.w3schools.com/js/js_loop_for.asp
  - https://www.w3schools.com/js/js_const.asp
  - https://github.com/rdwrome/261sp24/tree/main/10JavaScript
  - https://eloquentjavascript.net/05_higher_order.html
