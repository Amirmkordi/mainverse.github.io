public class Product {
    String name;
    private int price;
    private int qty;
    public Product(String n, int p, int q) {
        name = n;
        price = p;
        qty = q;
    }
    public String getname() {
        return name;
    }
    public int getprice() {
        return price;
    }
    public int getqty() {
        return qty;
    }
    public static void maxP(Product[] a) {
        Product x = a[0];
        for (int i = 1; i < a.length; i++) {
            if (a[i].getprice() > x.getprice()) {
                x = a[i];
            }
        }
        System.out.println(x.getname() + "  " + x.getprice());
    }
    public static void minP(Product[] a) {
        Product x = null;
        for (int i = 0; i < a.length; i++) {
            if (a[i].getqty() > 0) {
                if (x == null || a[i].getprice() < x.getprice()) {
                    x = a[i];
                }
            }
        }
        if (x == null) {
            System.out.println("not available");
        } else {
            System.out.println(x.getname() + "  " + x.getprice());
        }
    }
    public static void sumV(Product[] a) {
        int s = 0;
        for (int i = 0; i < a.length; i++) {
            s += a[i].getprice() * a[i].getqty();
        }
        System.out.println(s);
    }
}