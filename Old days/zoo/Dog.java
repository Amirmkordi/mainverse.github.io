package zoo;
public class Dog extends Animal {
    public Dog(String name, int age, double weight) {
        super(name, age, weight);
    }

    public String sound() {
        return "Woof";
    }

    public String special() {
        return "Fetch ball";
    }

    public double Food() {
        if (age < 2)
            return 400;
        return 600;
    }
}