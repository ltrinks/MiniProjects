#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	FILE *input = fopen(argv[1], "r");
	printf("Opened File\n"); //DEBUG
	if (input == NULL) {
		printf("File not found");
		return 1;
	}
	
	char *longestWord = NULL;
	long int wordCount = 0;

	char *currentWord = NULL;
	printf("Made vairables\n"); //DEBUG
	while(fscanf(input, "%s", currentWord)!= EOF) {
		printf("On Word: %s\n", currentWord); //DEBUG
		wordCount++;
		if (strlen(currentWord) > strlen(longestWord)) {
			free(longestWord);
			longestWord = strcpy(malloc(sizeof(char) * strlen(currentWord) + 1), currentWord);
		}
	}

	printf("Word Count: %ld\n Longest Word: %s\n", wordCount, longestWord);
	if (strcmp(longestWord, "") != 0) {
		free(longestWord);
	}
	fclose(input);
}
