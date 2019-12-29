import java.util.Scanner;

/**
 * 1463번 1로 만들기
 */

public class Baeckjun1463 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        int dp[] = new int[x+1];

        for(int i = 2; i <= x; i++) {
            dp[i] = dp[i-1] + 1;    // 1을 빼는 경우에 해당
            if(i % 2 == 0) {
                dp[i] = Math.min(dp[i],dp[i/2]+1);  // 2로 나누는 경우에 해당
            }
            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i],dp[i/3]+1);  // 3으로 나누는 경우에 해당
            }
        }
        System.out.println(dp[x]);
        sc.close();
    }
}
