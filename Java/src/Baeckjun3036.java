import java.util.Scanner;

/**
 * 3036번 링
 */
public class Baeckjun3036 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] ring = new int[n+1];
        for (int i=1; i<=n; i++) {
            ring[i] = sc.nextInt();
        }

        for (int i=2; i<=n; i++) {
            int gcd = findGcd(Math.max(ring[1],ring[i]), Math.min(ring[1],ring[i]));
            System.out.print(ring[1]/gcd);
            System.out.print('/');
            System.out.println(ring[i]/gcd);
        }
    }

    private static int findGcd(int a, int b) {
        while (b != 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }
}
