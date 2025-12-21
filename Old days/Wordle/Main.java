import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        randomword selector;
        Scanner in = new Scanner(System.in);
        try {
            selector = new randomword();
        } catch (IOException e) {
            System.out.println("cant load file");
            return;
        }
        String secret = selector.randomw();
        System.out.println("\nWordle");
        boolean Win = false;

        for (int i = 1; i <= 6; i++) {
            String guess = "";
            boolean valid = false;
            while (!valid) {
                System.out.print("Guess " + i + " :");
                guess = in.nextLine().trim().toLowerCase();
                if (guess.length() == 5) {
                    valid = true;
                } else {
                    System.out.println("it should be 5 letters long");
                }
            }
            if (guess.equals(secret)) {
                Win = true;
                System.out.println("You guessed correctly!");
                System.out.println("the word is: " + secret);
                break;
            }
            char[] result = new char[5];
            boolean[] used = new boolean[5];
            int j = 0;
            while (j<5) {
                result[j] = 'X';
                used[j] = false;
                j++;
            }
            j=0;
            while (j<5) {
                if (guess.charAt(j) == secret.charAt(j)) {
                    result[j] = 'O';
                    used[j] = true;
                }
                j++;
            }
            j=0;
            while (j<5) {
                if (result[j] != 'O') {
                    char c = guess.charAt(j);
                    int k = 0;
                    while (k<5) {
                        if (!used[k] && c == secret.charAt(k)) {
                            result[j] = 'W';
                            used[k] = true;
                            break;
                        }else {
                            k++;
                        }
                    }
                }
                j++;
            }
            System.out.println("result is : " + new String(result));
        }
        if (!Win) {
            System.out.println("you lost");
            System.out.println("the word is: " + secret);
        }
    }
}