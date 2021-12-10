package Day3;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class InputReader {
    static ArrayList<String> getInput(String file) throws IOException {
        Scanner scanner = new Scanner(Paths.get(file));
        ArrayList<String> bytes = new ArrayList<String>();

        // we read the file until all lines have been read
        while (scanner.hasNextLine()) {
            bytes.add(scanner.nextLine());
        }
        return bytes;
    }
}

