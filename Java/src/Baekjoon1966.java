import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 1966번 프린터 큐
 */

public class Baekjoon1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            List<Paper> queue = new ArrayList<>();
            Integer[] priority = new Integer[n];

            st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++) {
                int tmp_pri = Integer.parseInt(st.nextToken());
                queue.add(new Paper(j,tmp_pri));
                priority[j] = tmp_pri;
            }

            Arrays.sort(priority, Collections.reverseOrder());

            int count = 0;
            while (queue.size() != 0) {
                Paper front = queue.remove(0);
                if (priority[count] == front.pri) {
                    if (front.num == m) {
                        System.out.println(count+1);
                        break;
                    }
                    count++;
                } else {
                    queue.add(front);
                }
            }
        }
    }
}

class Paper{
    int num, pri;

    public Paper(int num, int pri) {
        this.num = num;
        this.pri = pri;
    }
}