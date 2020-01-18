import java.util.Scanner;

/**
 * 2609번 최대공약수와 최소공배수
 */
public class Baeckjun2609 {
    static int gcf, lcm, x, y;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // x가 y보다 커야 최대공약수를 구할 수 있다.
        if (a>b) {
            x = a;
            y = b;
        } else {
            x = b;
            y = a;
        }

        // 최대공약수
        findGcf();

        // 최소공배수
        lcm = (a * b) / gcf;

        System.out.println(gcf);
        System.out.println(lcm);
    }

    private static void findGcf() {
        while (y!=0) {
            int tmp = x;
            x = y;
            y = tmp % y;
        }
        gcf = x;
    }
}
