import java.util.Scanner;

/**
 * 14681번 사분면 고르기
 */
public class Baekjoon14681 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();
        int n;

        if (x * y > 0) {
            n = (x > 0) ? 1 : 3;
        } else {
            n = (x > 0) ? 4 : 2;
        }

        System.out.println(n);
    }
}
