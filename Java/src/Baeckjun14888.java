import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 14888번 연산자 끼워넣기
 */
public class Baeckjun14888 {
    static int n;
    static int[] num;
    static int[][] op;
    static int min = 1000000000;
    static int max = -1000000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        num = new int[n];
        op = new int[n-1][2];

        StringTokenizer st = null;
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }

        int l = 0;
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<4; i++) {
            int j = Integer.parseInt(st.nextToken());
            for (int k=0; k<j; k++) {
                op[l][0] = i;
                l++;
            }
        }

        insertOp(0, num[0]);

        System.out.println(max);
        System.out.println(min);
    }

    static void insertOp(int index, int result) {
        if (index == n-1) {
            if (result < min) min = result;
            if (result > max) max = result;
            return;
        }
        for (int i=0; i<n-1; i++) {
            if (op[i][1] != 1) {
                op[i][1] = 1;
                if (op[i][0] == 0) insertOp(index + 1, result + num[index + 1]);
                else if (op[i][0] == 1) insertOp(index + 1, result - num[index + 1]);
                else if (op[i][0] == 2) insertOp(index + 1, result * num[index + 1]);
                else if (op[i][0] == 3) {
                    if (result >= 0) insertOp(index + 1, result / num[index + 1]);
                    else insertOp(index + 1, -((-result) / num[index + 1]));
                }
                op[i][1] = 0;
            }

        }
    }
}
