## Phase 4

### My process

   For phase 4 I had to break down the problem on paper. I made a grid with round numbers and different cell sizes and figured out that to make the grid, I had to divide the x and y by the number of cells to find the size of a single cell. Also, for the scaling, I figured out that by checking the ratio of the height of the cell divided by the height of the drawing, I knew that the outcome was the percentage that my drawing needed to shrink/expand. But If I only took into account the height ratio, my drawing could possibly be larger than the cell size it is supposed to fit in and overlap. That is why I must compare the height and width ratios and store the smaller one.

   After figuring this out, I made a new processing sketch with a really simple rectangle and an easy size to start writing this. I made a drawObject function for the rectangle, and then I added two variables that would determine how many cells the grid would have. I used those variables to divide the width and height of the canvas to find the cell size. Then I implemented the method I mentioned above with an if else statement to find the smallest ratio that will be used as the scale variable. I figured out that to traverse the grid, I would have to use a nested loop. I added two more variables, one for the x-axis and one for the y-axis, and I initialized them. The first loop has a range of grid x (the number of cells on the x-axis), and the nested loop has a range of grid y (the number of cells on the y-axis). The loop works by printing a column of cats with the same x value but all the y values and then resetting the y value and incrementing the x value by the size of a cell.

   Once the program was working as intended, I moved on to adding the code I wrote to the phase 3 program. Instead of having two variables for the x and y grid values, I made the phase 4 code into a function that takes two variables that have the same function to make the program neater.


### Troubleshooting

  - Divisions in processing did not work as expected. They output integers instead of float so I had to fix that.

  - When I was figuring out how to make the nested loops, I wasted around two-three hours because of a mistake in my drawObject function. I had forgotten to add push and pop to my simple program and even though the rest of my code was correct the result was not as expected. I added print functions in for all my variables in different places to check what was wrong but everything was printing as expected. I restarted, made a new sketch but nothing seemed to work, until I figured out what was missing.

### Code used

  - The reference documentation of processing.

  - Control flow markdown file on github repository.
  
