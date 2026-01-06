package zoo;
import java.util.*;

public class Zoo {
    private final ArrayList <Animal> animals = new ArrayList<>();
    public void addAnimal(Animal a){
        animals.add(a);
    }
    public void printAnimals(){
        for ( Animal a : animals){
            a.showinfo();
        }
    }
    public void totalFood(){
        double total = 0;
        for ( Animal a : animals){
            total +=a.Food();
        }
        System.out.println(total);
    }
    public void avgweight(){
        double total = 0;
        for ( Animal a : animals){
            total +=a.getWeight();
        }
        System.out.println(total);
    }
    public void avgage(){
        double total = 0;
        for ( Animal a : animals){
            total +=a.getAge();
        }
        System.out.println(total);
    }
    public void sortW(){
        for ( int i = 0; i < animals.size() -1 ; i++){
            for(int j = i+1; j < animals.size(); j++){
                if(animals.get(j).getWeight() > animals.get(i).getWeight()){
                    Animal temp = animals.get(i);
                    animals.set(i, animals.get(j));
                    animals.set(j, temp);
                }
            }
        }
    }
    public void sortage(){
        for ( int i = 0; i < animals.size() -1 ; i++){
            for(int j = i+1; j < animals.size(); j++){
                if(animals.get(j).getAge() > animals.get(i).getAge()){
                    Animal temp = animals.get(i);
                    animals.set(i, animals.get(j));
                    animals.set(j, temp);
                }
            }
        }
    }
}
