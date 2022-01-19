# Lauren Trinks March 19

# A game to see how well you know you know your trendy words!

# Scrapes the homepage of Urban Dictionary for the trending terms, randomly chooses one, uses the rapidAPI Urban
# Dictionary API (https://rapidapi.com/community/api/urban-dictionary/endpoints) to search the term and get the top ten
# results, then it randomly chooses two and prints the example section of the entries. The user then guesses which
# example came from the entry with more thumbs up. The program then says if the guess was right and shows how many
# thumbs up each entry had.

import requests
import random

# Go to urban dictionary and get the trending words of the day
urlUD = "https://www.urbandictionary.com/"
response = requests.get(urlUD)
preParsedWords = str(response.content).split("trending-link")
trending = []
for i in range(len(preParsedWords) - 1):
    term = preParsedWords[i + 1][preParsedWords[i + 1].index(">") + 1: preParsedWords[i + 1].index("<")]
    formattedTerm = ""
    for char in term:
        if not (char == "\\"):
            formattedTerm = formattedTerm + char
    trending.append(formattedTerm)

# Set the search term to be a trending word of the day
search = random.choice(trending)

# The website that we want to send our queries to
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

# Formats the search term for use with the API
querystring = {"term": search}

# Information needed for the API to know we are allowed to use it, just needs my account key
headers = {
    'x-rapidapi-key': "6955b18af8mshe3b23372648a206p1b3ca3jsn807f73b809f0"
}

# Send the information to the API and record the response
response = requests.request("GET", url, headers=headers, params=querystring)

# Grab two random entries for the search term to use as choices
randomOptions = random.sample(response.json()['list'], 2)

# Remove the brackets from the examples so they are more readable
firstOptionExample = ""
secondOptionExample = ""
for char in randomOptions[0]['example']:
    if not (char == '[' or char == ']'):
        firstOptionExample = firstOptionExample + char
for char in randomOptions[1]['example']:
    if not (char == '[' or char == ']'):
        secondOptionExample = secondOptionExample + char

# Print the choices
print("Choice 1:")
print(firstOptionExample + '\n')
print("Choice 2:")
print(secondOptionExample + '\n')

# Prompt for the answer and get the response
print("Which choice (1 or 2) came from the better definition of " + search + "?")
guess = -1
try:
    guess = int(input("Your guess: "))
    if not (guess == 1 or guess == 2):
        print("Invalid guess.")
except ValueError:
    print("Invalid guess.")
print()

# Figure out if the guess was right by comparing the number of thumbs up
oneGuesses = randomOptions[0]['thumbs_up']
twoGuesses = randomOptions[1]['thumbs_up']
answer = 3
if oneGuesses > twoGuesses:
    answer = 1
elif twoGuesses > oneGuesses:
    answer = 2
else:
    answer = 3

# Set the correct response based on the answer
correct = False
if not (answer == 3):
    correct = (answer == guess)
else:
    correct = True

# Print if the guess was right and the ratings for each of the choices
print("Your guess was " + str(correct).lower() + "!")
print("Choice 1 had " + str(oneGuesses) + " thumbs up, and Choice 2 had " + str(twoGuesses) + " thumbs up.")