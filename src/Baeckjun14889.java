import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 14889번 스타트와 링크
 */
public class Baeckjun14889 {
    static boolean[] player;
    static int[] start;
    static int[] link;
    static int n;
    static int[][] status;
    static int min = 2000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        player = new boolean[n+1];
        start = new int[n/2+1];
        link = new int[n/2+1];

        status = new int[n+1][n+1];

        StringTokenizer st = null;
        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=1; j<=n; j++) {
                status[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        devide(1,0);

        System.out.println(min);
    }

    static void devide(int num, int depth) {
        if (depth == n/2) {
            addStatus();
            return;
        }
        for (int i=num+1; i<=n; i++) {
            if (!player[i]) {
                player[i] = true;
                devide(i,depth+1);
                player[i] = false;
            }
        }
    }

    static void addStatus() {
        int startAllStatus = 0;
        int linkAllStatus = 0;

        for (int i=1; i<=n; i++) {
            for (int j=i+1; j<=n; j++) {
                if(player[i] && player[j])
                    startAllStatus += (status[i][j] + status[j][i]);
                else if(!player[i] && !player[j])
                    linkAllStatus += (status[i][j] + status[j][i]);
            }
        }

        int diff = Math.abs(startAllStatus-linkAllStatus);
        if (min > diff) min = diff;
    }
}
