#include <stdio.h>
#include <stdlib.h>

// Lauren Trinks March 31

// A program that takes a number of bytes to fill and makes a text file of that size

int main(int argc, char *argv[]) {
	// open the output file
	FILE *output = fopen(argv[1], "w");
	

	// for every byte the user wants to fill print a char to the file
	for (long int i = 0; i < atoi(argv[2]); i++) {
		fputc((i & 255), output);
	}

	// close the file
	fclose(output);

	return 0;
}
