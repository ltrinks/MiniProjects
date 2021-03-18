// Lauren Trinks March 18
// program to evaluate Reverse polish Notation https://en.wikipedia.org/wiki/Reverse_Polish_notation
// Supported operands are + - * / % (integer versions of these operations)
// Input integers for numbers

import java.util.Scanner;

public class RPNEvaluator {

    // main function where the program executes
    public static void main(String[] args) {

        // print the welcome statement and get the user input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your RPN statement:");
        String input = scanner.nextLine();

        // make the stack and get the individual numbers and operands
        StackNode stack = new StackNode();
        String[] items = input.split(" ");

        // go through every item
        for (String item : items) {

            // if the item is an operand, do the operation, if it is not, add the number to the stack
            if (isOperand(item)) {

                // to use an operand there must be at least 2 items in the stack
                if (stack.size() >= 2) {

                    // get the most recent two number
                    int itemTwo = stack.pop();
                    int itemOne = stack.pop();

                    // do the operand on the numbers and push it on the stack
                    switch (item) {
                        case "+" -> stack.push(itemOne + itemTwo);
                        case "-" -> stack.push(itemOne - itemTwo);
                        case "*" -> stack.push(itemOne * itemTwo);
                        case "/" -> stack.push(itemOne / itemTwo);
                        case "%" -> stack.push(itemOne % itemTwo);
                    }
                }

            } else {
                // push the number on the stack, if it is not a number, say that there is an error but continue
                try {
                    stack.push(Integer.parseInt(item));
                } catch (NumberFormatException e) {
                    System.out.println("Error: Invalid Operator or Number Entered, Trying to Evaluate Anyways");
                }
            }
        }

        // if the evaluation is successful, there should only be one item in the stack, if there is it is the result
        if (stack.size() == 1) {
            System.out.println("The result is: " + stack.pop());
        } else {
            System.out.println("Something went wrong");
        }

    }

    // returns true if the item is an operand, otherwise it returns false
    public static boolean isOperand(String item) {
        return switch (item) {
            case "+", "-", "*", "/", "%" -> true;
            default -> false;
        };
    }
}

// the stack that the program will use to get and put values in
class StackNode {

    // the variables in a stack object
    private int value;
    private StackNode next;

    // makes an empty node
    public StackNode() {
    }

    // get the size of the stack, ignoring the first element
    public int size() {
        int size = 0;
        StackNode current = this;
        while (current != null) {
            current = current.next;
            size++;
        }
        return size - 1;
    }

    // push a new value onto the stack, takes the value you want to add
    public void push(int value) {
        StackNode current = this;
        while (current.next != null) {
            current = current.next;
        }
        current.next = new StackNode();
        current.next.value = value;
    }

    // return the most recent item and remove it from the stack
    public int pop() {
        if (this.size() == 0) {
            return Integer.MIN_VALUE;
        }
        StackNode current = this;
        StackNode previous = null;
        while (current.next != null) {
            previous = current;
            current = current.next;
        }
        previous.next = null;
        return current.value;
    }

    // a debugging function to print the contents of a stack ignoring the head
    public void walk() {
        if (this.next == null) {
            return;
        }
        StackNode current = this.next;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }
}

