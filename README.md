# DailyProjects

My goal is to make a new program everyday. When I do not have an assignemnt to complete my goal I will write a program here. These projects will usually be short (at most a few hundred lines) and be ideas of my own or suggestions from the internet.

## Projects

### Day 2 Urban Dictionary Game (March 19)
I wanted to make a program that involved web-scraping because it is something that I have never done before.
I decided to make a game based on Urban Dictionary because I thought it would bea fun way to learn. For those of you who do not know, Urban Dictionary is a website where people go to uplaod definitions and examples of current slang.
It is often innapropriate so be careful if you are not okay with swearing and other explicit content. What I made is a game that will give two examples for a trending word of the day and have you guess which example came from the better rated definition. What was challenging was learning how to use the API, and learning how to do simple web-scraping. The API that I found (link here: https://rapidapi.com/community/api/urban-dictionary/endpoints) takes a term and returns the top 10 entries for the term. I wanted the game to come up with its own terms to search and there was no way to do that through the API. What I came up with is using the requests package to get the HTML for the homepage of Urban Dictionary, I then found the pattern and location for where the trending terms are and I wrote a loop that grabs all 30 terms and puts them in a list. I am really proud of myself because this is the first time that I got information from a website without using an API. I wrote this program in python.

### Day 1 RPN Evaluation (March 18)
 I learned about RPN (Reverse Polish Notation) from my Java class. 
It is a way to evaluate functions with multiple operands in a simple manner. 
The way it works is with stacks. 
The program goes through every item in the function and if it gets a number it puts it on the stack, if it is an operand, it does the operation on the last two items in the stack and pushes the result on the stack. 
The final result is when there is one item on the stack.
I made my own stack structure (which I have never done before) and got more familiar with switch statements.
The program will tell you if you put an item that is not a number or operator.
It will only not print a result and say "Something went wrong" when there is more than one item one the stack when done evaluating.
For more information on how to write RPN statements visit the wikipedia page: https://en.wikipedia.org/wiki/Reverse_Polish_notation . I wrote this program in java.


