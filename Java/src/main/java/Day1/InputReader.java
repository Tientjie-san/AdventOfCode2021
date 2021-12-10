package Day1;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class InputReader {
    static ArrayList<Integer> getInput(String file) throws IOException {
        Scanner scanner = new Scanner(Paths.get(file));
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        // we read the file until all lines have been read
        while (scanner.hasNextLine()) {
            numbers.add(Integer.parseInt(scanner.nextLine()));
        }
        return numbers;
    }
}
