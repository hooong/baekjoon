import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * 11653번 소인수분해
 */
public class Baeckjun11653 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> result = new ArrayList<>();

        for (int i=2; i<=n; i++) {
            while (n % i == 0) {
                n /= i;
                result.add(i);
            }
        }

        for (Integer i : result) {
            System.out.println(i);
        }
    }
}
