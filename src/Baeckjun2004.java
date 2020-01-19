import java.util.Scanner;

/**
 * 2004번 조합 0의 개수
 */
public class Baeckjun2004 {
    static long five = 0;
    static long two = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long m = sc.nextLong();

        // n 팩토리얼
        countFive(n,'+');
        countTwo(n,'+');

        // m 팩토리
        countFive(m,'-');
        countTwo(m,'-');

        // (n-m) 팩토리얼
        countFive((n-m),'-');
        countTwo((n-m),'-');


        System.out.println(Math.min(five, two));

    }

    private static void countFive(long n, char op) {
        for (long i=5; i<=n; i*=5) {
            if (op == '+')
                five += n/i;
            else
                five -= n/i;
        }
    }

    private static void countTwo(long n, char op) {
        for (long i=2; i<=n; i*=2) {
            if (op == '+')
                two += n/i;
            else
                two -= n/i;
        }
    }
}
