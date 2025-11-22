import java.util.ArrayList;
public class ShoppingManager {
    private ArrayList<String> names = new ArrayList<String>();
    private ArrayList<Double> prices = new ArrayList<Double>();
    public int size() {
        return names.size();
    }
    public void addItem(String name, double price) {
        names.add(name);
        prices.add(price);
    }
    public int editPriceByName(String name, double newPrice) {
        int count = 0;
        for (int i = 0; i < names.size(); i++) {
            if (names.get(i).equalsIgnoreCase(name)) {
                prices.set(i, newPrice);
                count++;
            }
        }
        return count;
    }
    public int removeByName(String name) {
        int removed = 0;
        for (int i = 0; i < names.size(); i++) {
            if (names.get(i).equalsIgnoreCase(name)) {
                names.remove(i);
                prices.remove(i);
                removed++;
                i--; 
            }
        }
        return removed;
    }
    public double getTotal() {
        double sum = 0;
        for (int i = 0; i < prices.size(); i++) {
            sum += prices.get(i);
        }
        return sum;
    }
    private double getMaxValue() {
        double max = prices.get(0);
        for (int i = 1; i < prices.size(); i++) {
            if (prices.get(i) > max) max = prices.get(i);
        }
        return max;
    }
    private double getMinValue() {
        double min = prices.get(0);
        for (int i = 1; i < prices.size(); i++) {
            if (prices.get(i) < min) min = prices.get(i);
        }
        return min;
    }
    public void sortByNameAscending() {
        for (int i = 0; i < names.size(); i++) {
            for (int j = i + 1; j < names.size(); j++) {
                if (names.get(i).compareToIgnoreCase(names.get(j)) > 0) {
                    swap(i, j);
                }
            }
        }
    }
    public void sortByNameDescending() {
        for (int i = 0; i < names.size(); i++) {
            for (int j = i + 1; j < names.size(); j++) {
                if (names.get(i).compareToIgnoreCase(names.get(j)) < 0) {
                    swap(i, j);
                }
            }
        }
    }
    public void sortByPriceAscending() {
        for (int i = 0; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                if (prices.get(i) > prices.get(j)) {
                    swap(i, j);
                }
            }
        }
    }
    public void sortByPriceDescending() {
        for (int i = 0; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                if (prices.get(i) < prices.get(j)) {
                    swap(i, j);
                }
            }
        }
    }
    private void swap(int i, int j) {
        String tempName = names.get(i);
        names.set(i, names.get(j));
        names.set(j, tempName);

        double tempPrice = prices.get(i);
        prices.set(i, prices.get(j));
        prices.set(j, tempPrice);
    }
    public void printList() {
        for (int i = 0; i < names.size(); i++) {
            System.out.println(names.get(i) + " : " + prices.get(i));
        }
    }
    public void printReport() {
        System.out.println("Number of items: " + names.size());
        System.out.println("Total cost: " + getTotal());
        double max = getMaxValue();
        double min = getMinValue();
        System.out.println("\nMost expensive item:");
        for (int i = 0; i < names.size(); i++) {
            if (prices.get(i) == max) {
                System.out.println("- " + names.get(i) + " : " + prices.get(i));
            }
        }
        System.out.println("\nCheapest item:");
        for (int i = 0; i < names.size(); i++) {
            if (prices.get(i) == min) {
                System.out.println("- " + names.get(i) + " : " + prices.get(i));
            }
        }
        System.out.println("\nCurrent list:");
        printList();
    }
}
