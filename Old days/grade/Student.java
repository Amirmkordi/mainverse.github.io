public class Student {
    private String name;
    private double[] grade;
    public Student(String name, int n) {
        this.name = name;
        grade = new double[n];
    }
    public String getname() {
        return name;
    }
    public void setgrade(int i, double v) {
        if (i < 0 || i >= grade.length) return;
        if (v < 0) v = 0;
        if (v > 20) v = 20;
        grade[i] = v;
    }
    public double avg() {
        double s = 0;
        for (double x : grade) s += x;
        return grade.length == 0 ? 0 : s / grade.length;
    }
}
