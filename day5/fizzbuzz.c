#include <stdio.h>
#include <string.h>

int  main() {
	char* fizz = "Fizz";
	char* buzz = "Buzz";
	

	for (int i = 1; i <= 100; i++) {

		char* output = "";

		if (i % 3 == 0) {
			printf("%s", fizz);
		}

		if (i % 5 == 0) {
			printf("%s", buzz);
		}

		if (!(i % 3 == 0 || i % 5 == 0)) {
			printf("%d\n", i);
		} else {
			printf("\n");
		}

	}
}
