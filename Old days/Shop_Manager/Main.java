import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        Product[] a = new Product[n];
        for (int i = 0; i < n; i++) {
            String name = in.nextLine();
            int price = in.nextInt();
            int qty = in.nextInt();
            in.nextLine();
            a[i] = new Product(name, price, qty);
        }
        Product.maxP(a);
        Product.minP(a);
        Product.sumV(a);
    }
}