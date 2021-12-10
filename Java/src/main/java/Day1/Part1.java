package Day1;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class Part1 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> numbers = InputReader.getInput("src/main/java/Day1/input.txt");
        int count = 0;
        for (int i = 1; i < numbers.size(); i++){
            if(numbers.get(i - 1) < numbers.get(i)){
                count++;
            }
        }
        System.out.println(count);
    }
}
