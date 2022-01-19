#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Lauren Trinks March 28, 29

// A program that reads a text file and tells statistics about the content of the file

int main(int argc, char *argv[]) {

	// open the file and exit if it does not exist
	FILE *input = fopen(argv[1], "r");
	if (input == NULL) {
	    printf("File not found");
	    return 1;
	}
	
	// initialize variables to be used in the loop
	char *longestWord = malloc(sizeof(char) * 2);
	longestWord[0] = '\0';
    
	long int wordCount = 0;
    	long int totalCharCount = 0;
   	long int wordCharCount = 0;

	char *currentWord = malloc(sizeof(char) * 2);
	currentWord[0] = '\0';
    
    	char c;
    	char strc[2];
    	strc[1] = '\0';
    
	// go through every character in the file
	while((c = fgetc(input)) != EOF) {
        	strc[0] = c;
        	totalCharCount++;

		// if the character is not one of these, add it on to the current word and free the old memory block
		if (c != ' ' && c != '\n' && c != '.' && c != ',' && c != ';' && c != '!' && c != '?') {
            		wordCharCount++;
            		char *newWord = strcpy(malloc(sizeof(char) * (strlen(currentWord) + 2)), currentWord);
            		newWord = strcat(newWord, strc);
            		free(currentWord);
            		currentWord = newWord;

		// if the character is one of those characters, only add the to the word count if the word is longer than 2 letters or is a variation of 'a' or 'i' or is a digit
        	} else {
            
            		if ((strlen(currentWord) > 1) || currentWord[0] == 'I' || currentWord[0] == 'i' || \
                		currentWord[0] == 'A' || currentWord[0] == 'a' || \
                		(currentWord[0] >= '0' && currentWord[0] <= '9')) {
           			wordCount++;
            		}

			// if the word is longer than the longest word, save it and free the old word
            		if (strlen(currentWord) > strlen(longestWord)) {
				free(longestWord);
				longestWord = strcpy(malloc(sizeof(char) * strlen(currentWord) + 1), currentWord);
	    		}

            		free(currentWord);
            		currentWord = malloc(sizeof(char) * 2);
            		currentWord[0] = '\0';
		}	
    }

    // print out information for the stats and then free the remaining blocks and exit
    printf("\nWord Count: %ld\nCharacter Count: %ld, Ignoring Whitespace and Punctuation: %ld\nLongest Word: %s\n\n", wordCount, totalCharCount, wordCharCount, longestWord);
    free(currentWord);
    free(longestWord);
    fclose(input);
}
