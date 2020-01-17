import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * 1541번 일어버린 괄호
 */
public class Baeckjun1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] exp = br.readLine().split("\\-");

        int result = 0;
        for (int i=0; i<exp.length; i++) {
            int num = plus(exp[i]);

            if (i==0) result = num;
            else result -= num;
        }

        System.out.println(result);
    }

    private static int plus(String str) {
        String[] expPlus = str.split("\\+");
        int result = 0;

        for (String num : expPlus) {
            result += Integer.parseInt(num);
        }
        return result;
    }
}
