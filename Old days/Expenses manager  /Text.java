import java.time.LocalDate;
import java.util.Scanner;
import java.util.*;
import java.io.IOException;
import java.nio.file.*;



public class Text {
    static Scanner input = new Scanner(System.in);
    private Path file;
    public Text(String fileName) throws IOException {
        this.file = Paths.get(fileName);
        if(!Files.exists(file)) {
            Files.createFile(file);
        }
    }

    public void addexpense(){
        System.out.println("Enter date (yyyy-mm-dd): ");
        LocalDate date = LocalDate.parse(input.nextLine());

        System.out.println("Enter title: ");
        String title = input.nextLine();

        System.out.println("Enter amount: ");
        long amount = Long.parseLong(input.nextLine());

        System.out.println("Enter category: ");
        String category = input.nextLine();

        Daily d = new Daily(date,title,amount,category);
        try{
            Files.write(
                    file,
                    List.of(d.toLine()),
                    StandardOpenOption.APPEND, StandardOpenOption.CREATE
            );
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void showall(){
        List<Daily> list = readall();
        for(int i = 0 ; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }

    public void report(){
        System.out.println("dar hal sakht");
    }

    public void search(){
        List<Daily> list = readall();
        String til = input.nextLine();
        for(Daily d : list){
            if(d.getTitle().equals(til)){
                System.out.println(d);
            }
        }
    }

    public void editdelete(){
        List<Daily> list = readall();
        showall();
        int cho = input.nextInt();
        cho--;
        System.out.println("edit: 1");
        System.out.println("delete: 2");
        int c = input.nextInt();
        if(c==1){
            Daily d = list.get(cho);
            int newamount = input.nextInt();
            list.set(cho,new Daily(d.getDate(),d.getTitle(),newamount,d.getCategory()));
        }
        else if(c==2){
            list.remove(cho);
        }
        else {
            System.out.println("invalid choice");
        }
        writeAll(list);
    }

    private List<Daily> readall(){
        List<Daily> list = new ArrayList<>();
        try {
            List<String> lines = Files.readAllLines(file);
            for(String l : lines)
                list.add(Daily.fromline(l));
        } catch (IOException e) {
            System.out.println("read error");
        }
        return list;
    }
    private void writeAll(List<Daily> list){
        try {
            List<String> lines = new ArrayList<>();
            for(Daily d : list)
                lines.add(d.toLine());
            Files.write(file, lines);
        } catch (IOException e) {
            System.out.println("write error");
        }
    }
}
