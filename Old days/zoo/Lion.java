package zoo;
public class Lion extends Animal {
    public Lion(String name, int age, double weight) {
        super(name, age, weight);
    }
    public String sound() {
        return "Roar";
    }
    public String special() {
        return "Hunt";
    }
    public double dailyF() {
        return weight * 0.08 * 1000;
    }
}