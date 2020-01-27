import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 18258번 큐 2
 * 시간초
 */
public class Baekjoon18258 {
    static int[] queue;
    static int front = 0, back = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        queue = new int[n];

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String op = st.nextToken();

            switch (op) {
                case "push":
                    queue[(++back) % n] = Integer.parseInt(st.nextToken());
                    break;
                case "pop":
                    if (front == back) System.out.println(-1);
                    else System.out.println(queue[(++front) % n]);
                    break;
                case "size":
                    System.out.println(Math.abs(front - back));
                    break;
                case "empty":
                    if (front == back) System.out.println(1);
                    else System.out.println(0);
                    break;
                case "front":
                    if (front == back) System.out.println(-1);
                    else System.out.println(queue[front + 1]);
                    break;
                case "back":
                    if (front == back) System.out.println(-1);
                    else System.out.println(queue[back]);
                    break;
            }

        }
    }
}
