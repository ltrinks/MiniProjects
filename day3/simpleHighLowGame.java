// Lauren Trinks March 20

// A really simple game that has you try and guess a number and the game will tell you if the guess is too high or low.
// The game keeps tracks of guesses and has error handling for if the player puts in an invalid number or character.
// If the player types an invalid guess the guess will not be counted.

import java.util.Random;
import java.util.Scanner;

public class simpleHighLowGame {
    public static void main(String[] args) {

        // make instances of the classes I needed to import
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        // get the random number for the player to try and guess (between 0 and 100 exclusive)
        int number = random.nextInt(100);

        // initialize the guess and guesses
        int guess = -1;
        int guesses = 0;

        // repeat this process until the correct answer was chosen
        do {

            try{

                // prompt the user to guess, say "guess again" if it is not the first guess
                if (guesses == 0) {
                    System.out.println("Enter your guess!");
                } else {
                    System.out.println("Guess again!");
                }

                // save the response and increase the guesses number
                guess = Integer.parseInt(scanner.nextLine());
                guesses++;

                // print the hint or the congrats message based on the guess, print guesses also if correct
                if (guess > number) {
                    System.out.println("Your guess is too high!");
                } else if (guess < number) {
                    System.out.println("Your guess is too low!");
                } else {
                    System.out.println("You got it in " + guesses + " guesses!");
                }

            // if the user types something other than a number or an invalid number, tell them and do not count as guess
            } catch (NumberFormatException e) {
                System.out.println("Not a valid number.");
            }

        } while (guess != number);

    }
}
