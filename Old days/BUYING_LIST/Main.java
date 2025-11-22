import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ShoppingManager manager = new ShoppingManager();
        System.out.println("Enter your items one by one.");
        System.out.println("Type 'done' as the item name to stop entering items.\n");
        while (true) {
            String name = readString(input, "Item name : ");
            if (name.equalsIgnoreCase("done")) break;
            double price = readDouble(input, "Item price: ", 0);
            manager.addItem(name, price);
            System.out.println("Item added.\n");
        }
        if (manager.size() == 0) {
            System.out.println("Your list is empty.");
            return;
        }
        // menu
        while (true) {
            System.out.println("\n----------------------------");
            System.out.println("1) Add item");
            System.out.println("2) Edit price by name");
            System.out.println("3) Remove item by name");
            System.out.println("4) Report");
            System.out.println("5) Sort by name A -> Z");
            System.out.println("6) Sort by name Z -> A");
            System.out.println("7) Sort by price low -> high");
            System.out.println("8) Sort by price high -> low");
            System.out.println("0) Exit");
            System.out.print("Choose: ");

            int choice = readInt(input, "", 0);
            
            if (choice == 1) {
                String name = readString(input, "Item name: ");
                double price = readDouble(input, "Item price: ", 0);
                manager.addItem(name, price);
                System.out.println("Item added.");
            } else if (choice == 2) {
                String name = readString(input, "Item name to edit: ");
                double newPrice = readDouble(input, "New price: ", 0);
                int edited = manager.editPriceByName(name, newPrice);
                if (edited == 0) System.out.println("Item not found.");
                else System.out.println("Edited " + edited + " item.");
            } else if (choice == 3) {
                String name = readString(input, "Item name to remove: ");
                int removed = manager.removeByName(name);
                if (removed == 0) System.out.println("Item not found.");
                else System.out.println("Removed " + removed + " item(s).");
            } else if (choice == 4) {
                manager.printReport();
            } else if (choice == 5) {
                manager.sortByNameAscending();
                System.out.println("Sorted by name A -> Z:");
                manager.printList();
            } else if (choice == 6) {
                manager.sortByNameDescending();
                System.out.println("Sorted by name Z -> A:");
                manager.printList();
            } else if (choice == 7) {
                manager.sortByPriceAscending();
                System.out.println("Sorted by price low -> high:");
                manager.printList();
            } else if (choice == 8) {
                manager.sortByPriceDescending();
                System.out.println("Sorted by price high -> low:");
                manager.printList();
            } else if (choice == 0) {
                System.out.println("Goodbye");
                break;
            } else {
                System.out.println("Invalid choice.");
            }
        }
    }

    private static int readInt(Scanner input, String msg, int minAllowed) {
        while (true) {
            if (!msg.equals("")) System.out.print(msg);
            if (input.hasNextInt()) {
                int x = input.nextInt();
                input.nextLine();
                if (x >= minAllowed) return x;
                System.out.println("Number must be at least " + minAllowed + ".");
            } else {
                System.out.println("Please enter a valid integer.");
                input.nextLine();
            }
        }
    }
    private static double readDouble(Scanner input, String msg, double minAllowed) {
        while (true) {
            System.out.print(msg);
            if (input.hasNextDouble()) {
                double x = input.nextDouble();
                input.nextLine();
                if (x >= minAllowed) return x;
                System.out.println("Price cannot be negative.");
            } else {
                System.out.println("Please enter a valid number.");
                input.nextLine();
            }
        }
    }
    private static String readString(Scanner input, String msg) {
        while (true) {
            System.out.print(msg);
            String s = input.nextLine().trim();
            if (!s.equals("")) return s;
            System.out.println("Name cannot be empty.");
        }
    }
}