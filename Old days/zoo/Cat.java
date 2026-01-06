package zoo;
public class Cat extends Animal {
    public Cat(String name, int age, double weight) {
        super(name, age, weight);
    }

    public String sound() {
        return "Meow";
    }

    public String special() {
        return "Scratch";
    }
    public double Food() {
        if (age < 2)
            return 200;
        return 350;
    }
}