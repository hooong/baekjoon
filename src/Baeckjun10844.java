import javax.sound.sampled.AudioInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 10844번 쉬운 계단 수
 */
public class Baeckjun10844 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        long[][] dp = new long[n+1][10];

        for (int i=1; i<10; i++) {
            dp[1][i] = 1;
        }

        for (int i=2; i<=n; i++) {
            for (int j=0; j<10; j++) {
                if (j==0) dp[i][j] = dp[i-1][j+1];
                else if (j==9) dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000;
            }
        }

        long sum = 0;
        for (int i=0; i<dp[n].length; i++) {
            sum += dp[n][i];
        }

        System.out.println(sum%1000000000);

    }
}
