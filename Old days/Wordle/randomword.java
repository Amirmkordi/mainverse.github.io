import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class randomword {
    private final String[] words = new String[5757];
    private final Random random = new Random();
    public randomword() throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("words.txt"));
        for (int i = 0; i < 5757; i++) {
            words[i] = lines.get(i);
        }

    }
    public String randomw() {
        int i = random.nextInt(5757);
        return words[i];
    }
}
