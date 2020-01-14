import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 12865번 평범한 배낭
 */
public class Baeckjun12865 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] bags = new int[n+1][2];
        int[][] dp = new int[k+1][n+1];

        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            bags[i][0] = Integer.parseInt(st.nextToken());
            bags[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i=1; i<=k; i++) {
            for (int j=1; j<=n; j++) {
                if ( i >= bags[j][0]) {
                    dp[i][j] = Math.max(dp[i][j-1], dp[i-bags[j][0]][j-1] + bags[j][1]);
                } else dp[i][j] = dp[i][j-1];
            }
        }

        System.out.println(dp[k][n]);
    }
}
