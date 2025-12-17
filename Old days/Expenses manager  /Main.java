import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        Text daily = new Text("expenses.txt");

        while(true) {
            System.out.println("1. add expense");
            System.out.println("2. show all expenses");
            System.out.println("3. report all expenses");
            System.out.println("4. search expense");
            System.out.println("5 delete or edit expense");
            System.out.println("6. exit");
            int choice = sc.nextInt();
            if(choice == 1) {
                daily.addexpense();
            }
            else  if(choice == 2) {
                daily.showall();
            }
            else if(choice == 3) {
                daily.report();
            }
            else if(choice == 4) {
                daily.search();
            }
            else if(choice == 5) {
                daily.editdelete();
            }
            else if(choice == 6) {
                System.out.println("bye bye");
                break;
            }
            else  {
                System.out.println("invalid choice");
            }
        }
    }
}
