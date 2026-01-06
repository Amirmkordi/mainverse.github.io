package zoo;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Zoo zoo = new Zoo();
        int choice = 0;
        while(choice!=8){
            System.out.println("1. add bird");
            System.out.println("2. show all");
            System.out.println("3. total food of animals");
            System.out.println("4. average of weight of animals");
            System.out.println("5. average of age of animals");
            System.out.println("6. Sort the animals by weight");
            System.out.println("7. Sort the animals by age");
            System.out.println("8. exit");

            choice = in.nextInt();
            if (choice == 1) {

                System.out.print("Enter animal type (dog / cat / bird / lion): ");
                String type = in.next().toLowerCase();
                System.out.print("Name: ");
                String name = in.next();
                System.out.print("Age: ");
                int age = in.nextInt();
                System.out.print("Weight: ");
                double weight = in.nextDouble();

                if (type.equals("dog")) {
                    zoo.addAnimal(new Dog(name, age, weight));
                }
                else if (type.equals("cat")) {
                    zoo.addAnimal(new Cat(name, age, weight));
                }
                else if (type.equals("bird")) {
                    zoo.addAnimal(new Bird(name, age, weight));
                }
                else if (type.equals("lion")) {
                    zoo.addAnimal(new Lion(name, age, weight));
                }
                else {
                    System.out.println("Invalid");
                    continue;
                }
                System.out.println("Animal added");
            }
            else if (choice == 2) {
                zoo.printAnimals();
            }
            else if (choice == 3) {
                zoo.totalFood();
            }
            else if (choice == 4) {
                zoo.avgweight();
            }
            else if (choice == 5) {
                zoo.avgage();
            }
            else if (choice == 6) {
                zoo.sortW();
                System.out.println("sorted !");
            }
            else if (choice == 7) {
                zoo.sortage();
                System.out.println("sorted !");
            }
            else if (choice == 8) {
                System.out.println("good bye");
            }
        }
    }
}