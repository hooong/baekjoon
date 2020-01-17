import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 5086번 배수와 약수
 */
public class Baeckjun5086 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int first, second;
        String result;

        while (true) {
            st = new StringTokenizer(br.readLine());

            first = Integer.parseInt(st.nextToken());
            second = Integer.parseInt(st.nextToken());

            if (first==0 && second==0) break;

            if (first%second == 0 && first/second != 0) result = "multiple";
            else if (second%first == 0 && second/first != 0) result = "factor";
            else result = "neither";

            System.out.println(result);
        }
    }
}
