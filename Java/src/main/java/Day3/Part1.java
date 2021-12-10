package Day3;

import java.io.IOException;
import java.util.ArrayList;

public class Part1 {
    public static void main(String[] args) throws IOException {
        ArrayList<String> puzzle_input = InputReader.getInput("src/main/java/Day3/input.txt");
        int binary_length = puzzle_input.get(0).length();
        String gamma = "";
        for ( int i = 0; i < binary_length; i++) {
            gamma += most_occured_bit(i, puzzle_input);
        }
        String epsilon =  inverse(gamma);
        System.out.println(Integer.parseInt(epsilon, 2)*Integer.parseInt(gamma, 2));


    }
    static String inverse(String s){
        String inversed = "";
        for( char c: s.toCharArray()){
            if(c == '1') {
                inversed += "0";
            } else{
                inversed += "1";
            }
        }
        return inversed;
    }
    static String most_occured_bit(int pos , ArrayList<String> puzzle){
        int count = 0;
        for (String s : puzzle) {
            if (s.charAt(pos) == '1') {
                count += 1;
            } else {
                count -= 1;
            }
        }
        return count >= 0 ? "1" : "0";
    }
}
