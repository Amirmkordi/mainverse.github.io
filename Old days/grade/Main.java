import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int num2 = in.nextInt();
        in.nextLine();
        Student[] st = new Student[num];
        for (int i = 0; i < num; i++) {
            String name = in.nextLine().trim();
            st[i] = new Student(name, num2);
            for (int j = 0; j < num2; j++) {
                st[i].setgrade(j, in.nextDouble());
            }
        }
        for (Student s : st) {
            System.out.printf("%s %.2f%n", s.getname(), s.avg());
        }
        for (Student s : st) {
            if (s.avg() > 15) System.out.println(s.getname());
        }
        Student best = st[0];
        for (int i = 1; i < st.length; i++) {
            if (st[i].avg() > best.avg()) best = st[i];
        }
        System.out.println(best.getname());
    }
}
