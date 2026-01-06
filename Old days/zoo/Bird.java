package zoo;
public class Bird extends Animal {
    public Bird(String name, int age, double weight) {
        super(name, age, weight);
    }
    public String sound() {
        return "jik jik";
    }
    public String special() {
        return "Fly";
    }
    public double Food() {
        return 100;
    }
}