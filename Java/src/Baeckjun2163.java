import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 2163번 초콜릿 자르기
 */
public class Baeckjun2163 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] dp = new int[n+1][m+1];

        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                if (i==1) dp[i][j] = j-1;
                else if (j==1) dp[i][j] = i-1;
                else dp[i][j] = dp[i][j/2] + dp[i][j-j/2] + 1;

            }
        }
        System.out.println(dp[n][m]);
    }
}
