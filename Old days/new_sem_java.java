import java.util.Scanner;
public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int choice;
        System.out.println("Welcome :)");
        while (true) {
            System.out.println("1. Basic (+, -, *, /, ^, √)");
            System.out.println("2. Average of numbers");
            System.out.println("3. Positive or Negative or Zero check");
            System.out.println("4. Even or Odd");
            System.out.println("5. Print from 0 to n");
            System.out.println("6. Check if a number is Prime");
            System.out.println("0. Exit");
            System.out.print("Pick one: ");
            choice = in.nextInt();
            if (choice == 0) {
                System.out.println("Goodbye!");
                break;
            }
            switch (choice) {
                case 1:
                    System.out.print("Enter first number: ");
                    double a = in.nextDouble();
                    System.out.print("Enter operator (+, -, *, /, ^, √): ");
                    char op = in.next().charAt(0);
                    double b = 0;
                    if (op != '√') {
                        System.out.print("Enter second number: ");
                        b = in.nextDouble();
                    }
                    if (op == '+') {
                        System.out.println("Result: " + (a + b));
                    } else if (op == '-') {
                        System.out.println("Result: " + (a - b));
                    } else if (op == '*') {
                        System.out.println("Result: " + (a * b));
                    } else if (op == '/') {
                        if (b == 0) System.out.println("Can't divide by zero");
                        else System.out.println("Result: " + (a / b));
                    } else if (op == '^') {
                        System.out.println("Result: " + Math.pow(a, b));
                    } else if (op == '√') {
                        if (a < 0) System.out.println("Can't take square root of a negative number");
                        else System.out.println("Result: " + Math.sqrt(a));
                    } else {
                        System.out.println("Unknown operator");
                    }
                    break;
                case 2:
                    System.out.print("How many numbers do you have? ");
                    int count = in.nextInt();
                    double total = 0;
                    for (int i = 1; i <= count; i++) {
                        System.out.print("Number " + i + ": ");
                        total += in.nextDouble();
                    }
                    System.out.println("Average: " + (total / count));
                    break;
                case 3:
                    System.out.print("Enter a number: ");
                    double num = in.nextDouble();
                    if (num > 0) System.out.println("Thats positive.");
                    else if (num < 0) System.out.println("Thats negative.");
                    else System.out.println("Its zero.");
                    break;
                case 4:
                    System.out.print("Enter an number: ");
                    int n = in.nextInt();
                    if (n % 2 == 0) System.out.println("Even");
                    else System.out.println("Odd");
                    break;
                case 5:
                    System.out.print("Enter a number (n): ");
                    int limit = in.nextInt();
                    System.out.println("Counting up to the  " + limit + "...");
                    for (int i = 0; i <= limit; i++) {
                        System.out.print(i + " ");
                    }
                    System.out.println();
                    break;
                case 6:
                    System.out.print("Enter a number to check if its prime: ");
                    int primeCheck = in.nextInt();
                    if (primeCheck <= 1) {
                        System.out.println("not prime.");
                    } else {
                        boolean isPrime = true;
                        for (int i = 2; i <= Math.sqrt(primeCheck); i++) {
                            if (primeCheck % i == 0) {
                                isPrime = false;
                                break;
                            }
                        }
                        if (isPrime)
                            System.out.println(primeCheck + " is a prime number");
                        else
                            System.out.println(primeCheck + " is not prime");
                    }
                    break;
                default:
                    System.out.println("Wrong input");
            }
        }
        in.close();
    }
}
