package Day1;

import java.io.IOException;
import java.util.ArrayList;

public class Part2 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> numbers = InputReader.getInput("src/main/java/Day1/input.txt");
        int count = 0;
        for (int i = 1; i < numbers.size()-2; i++){
            int a = numbers.get(i-1);
            int b = numbers.get(i+2);

            if(a < b){
                count++;
            }
        }
        System.out.println(count);
    }
}
