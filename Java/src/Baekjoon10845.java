import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 10845번 큐
 */
public class Baekjoon10845 {
    static List<Integer> queue = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String op = st.nextToken();

            if (op.equals("push")) push(Integer.parseInt(st.nextToken()));
            else if (op.equals("pop")) System.out.println(pop());
            else if (op.equals("size")) System.out.println(size());
            else if (op.equals("empty")) {
                if (queue.isEmpty()) System.out.println(1);
                else System.out.println(0);
            }
            else if (op.equals("front")) System.out.println(front());
            else if (op.equals("back")) System.out.println(back());
        }
    }

    private static void push(int num) {
        queue.add(num);
    }

    private static int pop() {
        if (queue.isEmpty()) return -1;
        else return queue.remove(0);
    }

    private static int size() {
        return queue.size();
    }

    private static boolean empty() {
        return queue.isEmpty();
    }

    private static int front() {
        if (queue.isEmpty()) return -1;
        else return queue.get(0);
    }

    private static int back() {
        if (queue.isEmpty()) return -1;
        else return queue.get(queue.size()-1);
    }
}
