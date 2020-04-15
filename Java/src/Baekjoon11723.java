import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 11723번 집합
 */
public class Baekjoon11723 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int m, num;
        String command;
        boolean[] s = new boolean[21];

        m = Integer.parseInt(br.readLine());

        for (int i=0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            command = st.nextToken();

            if (command.equals("all") || command.equals("empty")) {
                if (command.equals("all")) {
                    Arrays.fill(s,true);
                } else {
                    Arrays.fill(s,false);
                }
            } else {
                num = Integer.parseInt(st.nextToken());

                if (command.equals("add")) {
                    s[num] = true;
                }
                else if (command.equals("remove")) {
                    s[num] = false;
                }
                else if (command.equals("check")) {
                    if (s[num]) System.out.println(1);
                    else System.out.println(0);
                }
                else if (command.equals("toggle")) {
                    s[num] = !s[num];
                }
            }
        }
    }
}
