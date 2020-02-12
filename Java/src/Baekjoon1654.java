import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 1654번 랜선 자르기
 */
public class Baekjoon1654 {
    static int [] line;
    static List<Integer> cut;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();
        int n = sc.nextInt();

        line = new int[k];
        cut = new ArrayList<>();

        for (int i=0; i<k; i++) {
            line[i] = sc.nextInt();
        }
        Arrays.sort(line);

        binSearch(n,0,line[k-1]);

        Collections.sort(cut);
        System.out.println(cut.get(cut.size()-1));

    }

    private static void binSearch(int n, int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;

            int cnt = 0;
            for (Integer len: line ) {
                cnt += len / mid;
            }

            if (cnt >= n) {
                cut.add(mid);
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
    }
}
