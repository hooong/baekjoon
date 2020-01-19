import java.util.Scanner;

/**
 * 1676번 팩토리얼 0의 개수
 */
public class Baeckjun1676 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int count = 0;

        for (int i = 1; i <= n; i++) {
            if (i % 5 == 0) {
                int j = i;
                while (j % 5 == 0) {
                    count++;
                    j = j / 5;
                }
            }
        }

        System.out.println(count);
    }
}
