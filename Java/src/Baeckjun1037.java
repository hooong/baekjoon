import java.util.Arrays;
import java.util.Scanner;

/**
 * 1037번 약수
 */
public class Baeckjun1037 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();

        int[] realMultiple = new int[c+1];

        for (int i=1; i<=c; i++) {
            realMultiple[i] = sc.nextInt();
        }

        Arrays.sort(realMultiple);

        int n = realMultiple[1] * realMultiple[c];
        System.out.println(n);
    }
}
