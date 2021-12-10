package Day2;

import java.io.IOException;
import java.util.ArrayList;

public class Part2 {
    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList<String>> puzzle_input = InputReader.getInput("src/main/java/Day2/input.txt");
        int horizontal_pos = 0;
        int depth = 0;
        int aim = 0;
        for (ArrayList<String> line: puzzle_input){
            String command = line.get(0);
            int amount = Integer.parseInt(line.get(1));
            if (command.equals("forward")){
                horizontal_pos += amount;
                depth += amount * aim;
            } else if (command.equals("up")) {
                aim -= amount;
            } else{
                aim += amount;
            }
        }
        System.out.println(depth*horizontal_pos);
    }
}
