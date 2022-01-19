# MiniProjects

When I am feeling creative or have not worked on code for a while I will do a mini project. With mini projects I am hoping to learn new tools or increase my confidence by doing something I thought I couldn't do before.

## Projects

### Fill Memory (March 31)
This is a program that is probably the opposite of what someone would want to use. This program takes a filename and a number and then makes a file that takes up that number of bytes. I wrote this to become more familiar with file ouputs in C and variable type data sizes. A char is 1 byte, which is 8 bits. I initially planned to control the size by bits, but most storage is seen by bytes so I ended up doing that. Plus, printing text seemed more straightforward than printing to a binary file. I wrote this program in C.

### Hate Crime Data Analysis (March 30)
I wanted to become more familiar with analyzing data in pandas for python. I am in a class that uses pandas but the way the assignments work is that they tell us how to do the analysis and to get the same results they reached. I wanted to see if I could find my own statistics from a set I found myself. I learned a bit about how to handle multiple variables for finding one outcome. Although I could not find a specific measure that effects the rate of hate crimes, I ruled that it must be a combination of things that is more than wealth inequality and high school education. I wrote this using pandas in python.

### File Stats (March 28, 29)
I wanted to get used to reading from files in C so I decided to write a program that goes through a file and will record information about it. It will record the word count, the character count with and without characters that are not in words. Also, this program will record the longest word in the file. To make sure this program is completely error free, I ran it through valgrind and found that there are no memory leaks. This program took me two days becuase I was having a lot of issues reading the file information in. I decided to stop using the fscanf function and used fgetc instead. This worked much better and made the character count information much easier to obtain. I wrote this program in C.

### FizzBuzz (March 24)
I heard about this problem from a few people saying that it is a way that businesses test if you actually know how to code when interviewing you. I thought I would try the problem in a language I am not super comfortable in. The program counts from 1 to 100, if the number is divisible by 3 print "Fizz", if it is divisible by 5 print "Buzz", if it is divisible by 3 and 5 print "FizzBuzz", otherwise print the number. This seems easy, but if you do not know what you are doing it can be very challenging and be a spaghetti of conditional statements. I feel like my code is clean and compact and I did well for a language I am not great in. I wrote this program in C.

### Unix Rollover Prediction (March 21)
I got this idea when reading the book "Humble Pi" by Matt Parker. In the book, there was a section about Unix time, the gregorian calendar, and countless rollover bugs from limited storage with a given number of bits. The book talked about how 32-bit systems will rollover in 2038 and 64-bit systems will rollover probably after the Earth is gone. I decided to write a program that will tell you when a machine with a given number of bits to store Unix time will rollover. The output of the program is the month and year the rollover will happen. This program took a lot of reading and not instantly obvious math to solve. I learned about interesting rules for leap years and that for computers time starts in 1970. I feel like my code, especially for finding the month, was really messy. In the future maybe I will fix this and add a feature to find the day as well. I am really hapy with how I was able to optimize it. In the first loop I wrote to find the year, it took several seconds to run for high bits, I was able to make it almost the same runtime for all numbers of bits. I wrote this program in python.

### Simple High Low Game (March 20)
This was one of the first programs I attempted to make in middle school. I was not successful and it put me off from coding for a long time. I decided to revisit it. I was able to complete the program very fast and add a few features that I did not think of before. To play the game will generate a random number between 0 and 100 and will have you guess what the number is. The game will tell you if the guess was too high or low. The game ends when you guess the correct number. I added error handling for invalid guesses and a counter to track how many tries it took to get right. A guess will not be counted if it invalid. This was a pretty easy project but it is nice to be able to do something that I wasn't able to before. I wrote this program in java.

### Urban Dictionary Game (March 19)
I wanted to make a program that involved web-scraping because it is something that I have never done before.
I decided to make a game based on Urban Dictionary because I thought it would bea fun way to learn. For those of you who do not know, Urban Dictionary is a website where people go to uplaod definitions and examples of current slang.
It is often innapropriate so be careful if you are not okay with swearing and other explicit content. What I made is a game that will give two examples for a trending word of the day and have you guess which example came from the better rated definition. What was challenging was learning how to use the API, and learning how to do simple web-scraping. The API that I found (link here: https://rapidapi.com/community/api/urban-dictionary/endpoints) takes a term and returns the top 10 entries for the term. I wanted the game to come up with its own terms to search and there was no way to do that through the API. What I came up with is using the requests package to get the HTML for the homepage of Urban Dictionary, I then found the pattern and location for where the trending terms are and I wrote a loop that grabs all 30 terms and puts them in a list. I am really proud of myself because this is the first time that I got information from a website without using an API. I wrote this program in python.

### RPN Evaluation (March 18)
 I learned about RPN (Reverse Polish Notation) from my Java class. 
It is a way to evaluate functions with multiple operands in a simple manner. 
The way it works is with stacks. 
The program goes through every item in the function and if it gets a number it puts it on the stack, if it is an operand, it does the operation on the last two items in the stack and pushes the result on the stack. 
The final result is when there is one item on the stack.
I made my own stack structure (which I have never done before) and got more familiar with switch statements.
The program will tell you if you put an item that is not a number or operator.
It will only not print a result and say "Something went wrong" when there is more than one item one the stack when done evaluating.
For more information on how to write RPN statements visit the wikipedia page: https://en.wikipedia.org/wiki/Reverse_Polish_notation . I wrote this program in java.


