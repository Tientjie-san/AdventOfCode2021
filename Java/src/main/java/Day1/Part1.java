package Day1;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class Part1 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> numbers = getInput("src/main/java/Day1/input.txt");
        int count = 0;
        for (int i = 1; i < numbers.size(); i++){
            if(numbers.get(i - 1) < numbers.get(i)){
                count++;
            }
        }
        System.out.println(count);

    }
    static ArrayList<Integer> getInput(String file) throws IOException{
        Scanner scanner = new Scanner(Paths.get(file));
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        // we read the file until all lines have been read
        while (scanner.hasNextLine()) {
            numbers.add(Integer.parseInt(scanner.nextLine()));
        }
        return numbers;
    }
}
