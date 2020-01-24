import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 9012번 괄호
 */
public class Baekjoon9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            int countLeft = 0;
            char[] ps = br.readLine().toCharArray();

            int j = 0;
            boolean isValid = true;
            while(j<ps.length && isValid) {
                if (ps[j] == '(') countLeft++;
                else {
                    if (countLeft == 0) isValid = false;
                    else countLeft--;
                }
                j++;
            }

            if (isValid && countLeft==0) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}
