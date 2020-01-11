import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 2565번 전깃줄
 */
public class Baeckjun2565 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int [][] link = new int[n+1][2];
        int [] dp = new int[n+1];

        StringTokenizer st = null;
        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            link[i][0] = Integer.parseInt(st.nextToken());
            link[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(link, new Comparator<int[]>() {
            @Override
            public int compare(int[] t1, int[] t2) {
                return t1[0] - t2[0];
            }
        });

        int answer = 1;
        for (int i=1; i<n+1; i++) {
            dp[i] = 1;
            for (int j=1; j<i; j++) {
                if (link[i][1] > link[j][1]) {
                    dp[i] = Math.max(dp[i],dp[j]+1);
                }
            }
            answer = Math.max(dp[i], answer);
        }

        System.out.println(n - answer);
    }
}
