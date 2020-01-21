import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 15650번 N과 M (2)
 */
public class Baeckjun15650 {

    static int n,m;
    static StringBuffer sb = new StringBuffer();
    static boolean[] visit;
    static char[] seq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visit = new boolean[n+1];
        seq = new char[m*2];
        Arrays.fill(seq, ' ');

        back(1,0);
        System.out.println(sb.toString());
    }

    static void back(int cur,int count) {
        if (count==m) {
            sb.append(seq);
            sb.append("\n");
            return;
        }

        for (int i=cur; i<=n; i++) {
            if (visit[i]) continue;
            visit[i] = true;
            seq[count*2] = (char)(i+'0');
            back(i,count+1);
            visit[i] = false;
        }
    }
}
