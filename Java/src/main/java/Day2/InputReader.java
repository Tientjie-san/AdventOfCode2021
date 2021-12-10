package Day2;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class InputReader {
    static ArrayList<ArrayList<String>> getInput(String file) throws IOException {
        Scanner scanner = new Scanner(Paths.get(file));
        ArrayList<ArrayList<String>> numbers = new ArrayList<ArrayList<String>>();

        // we read the file until all lines have been read
        while (scanner.hasNextLine()) {
            numbers.add(new ArrayList<String>(Arrays.asList(scanner.nextLine().split(" "))));
        }
        return numbers;
    }
}
