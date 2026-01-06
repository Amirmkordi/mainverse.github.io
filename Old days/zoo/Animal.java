package zoo;

public abstract class Animal {
    protected String name;
    protected int age;
    protected double weight;
    public Animal(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }
    public int getAge(){
        return age;
    }
    public double getWeight(){
        return weight;
    }

    public void move(){
        System.out.println(name +" is moving");
    }
    public void sleep(){
        System.out.println(name +" is sleeping");
    }

    public double Food() {
        return 0;
    }

    public String special() {
        return null;
    }

    public String sound() {
        return null;
    }

    public void showinfo() {
        System.out.println();
        System.out.println(name);
        System.out.println(age);
        System.out.println(weight);
        System.out.println(Food());
        System.out.println(special());
        System.out.println(sound());
    }

}
