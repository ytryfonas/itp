## Final Project

### My process

  - To make the Proficiency Training program I first made some lists that contain all the different elements asked in each level. Then using those lists I used nested for loops to combine them into a new list for each question that contains all the possible combinations of questions. That way when I ask a question, I can remove it from the list afterwards.

  - After I was done making my data sets, I made the main logic of the program, which is a while that keeps looping until I get the input 'stop'. Inside the while are a bunch of if else statements that check the level (1-4) that was input and then give out questions randomly. Using the random module it takes 1-3 random values depending on the question and then removes them from each list.

  - Also, one of the statements resets the lists if clear is input. It bassically redoes what the program did in the beginning to build the new lists that have all the new possibilities.

### Troubleshooting

  - One of the first problems I encountered was deleting two entries from a list. In the beginning I was doing removing [r] from the list and then [r+1] to remove two consecutive values. That is wrong because when you remove [r] from the list, the value next to it takes its place, so deleting [r] two times is what deletes two consecutive items from the list. If I had used del [r+1] after del [r] then I am removing [r] and then removing [r+2] from the original list.  

  - I had trouble getting a both string and int from the same input. The way I solved this was using .isdigit() which is a solution I read about on stackoverflow.

  - Most of my problems stemmed from keeping track of all the lists and variables. Because a lot of my lists have similar names I made some spelling errors that were pretty frustrating to find and fix.

  - I tried making a ui using turtle but I scrapped it and restarted using tkinter but due to time contains I had to scrap that too and go back to printing in the conslole.

### Code Used/ Referenced

  - https://github.com/rdwrome/261sp24/tree/main/04ControlFlow
  - https://greenteapress.com/thinkpython2/html/thinkpython2011.html
  - https://greenteapress.com/thinkpython2/html/thinkpython2005.html
  - https://stackoverflow.com/questions/50213230/how-to-make-a-user-input-both-a-string-and-integer
