import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 15651번 N과 M (3)
 */
public class Baeckjun15651 {
    static int n,m;
    static StringBuffer sb = new StringBuffer();
    static char[] seq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        seq = new char[m*2];
        Arrays.fill(seq, ' ');

        back(0);
        System.out.println(sb.toString());
    }

    static void back(int count) {
        if (count==m) {
            sb.append(seq);
            sb.append("\n");
            return;
        }

        for (int i=1; i<=n; i++) {
            seq[count*2] = (char)(i+'0');
            back(count+1);
        }
    }
}
