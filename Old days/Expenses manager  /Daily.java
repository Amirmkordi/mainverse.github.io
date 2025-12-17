import java.time.LocalDate;

public class Daily {
    private LocalDate date;
    private String title;
    private long amount;
    private String category;

    public Daily(LocalDate date, String title, long amount, String category) {
        this.date = date;
        this.title = title;
        this.amount = amount;
        this.category = category;
    }

    public LocalDate getDate() {return date;}
    public String getTitle() {return title;}
    public long getAmount() {return amount;}
    public String getCategory() {return category;}

    public String toLine() {
        return date + " | " + title + " | " + amount + " " + category;
    }
    public static Daily fromline(String line){
        String[] p = line.split("\\|");
        return new Daily(
                LocalDate.parse(p[0].trim()),
                p[1].trim(),
                Long.parseLong(p[2].trim()),
                p[3].trim()
        );
    }
}
