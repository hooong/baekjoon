import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 1931번 회의실배정
 */
public class Baeckjun1931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] meeting = new int[n+1][2];
        int endtime = 0;
        int count = 0;

        StringTokenizer st = null;
        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            meeting[i][0] = Integer.parseInt(st.nextToken());
            meeting[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(meeting, new Comparator<int[]>() {
            @Override
            public int compare(int[] ints, int[] t1) {
                return ints[1] - t1[1];
            }
        });

        for (int i=1; i<=n; i++) {
            if (endtime <= meeting[i][0]) {
                endtime = meeting[i][1];
                count += 1;
            }
        }

        System.out.println(count);
    }
}
