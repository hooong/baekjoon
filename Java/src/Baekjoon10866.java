import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 10866번 덱
 */
public class Baekjoon10866 {
    static List<Integer> deque = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String op = st.nextToken();

            if (op.equals("push_front")) {
                push_front(Integer.parseInt(st.nextToken()));
            } else if (op.equals("push_back")) {
                push_back(Integer.parseInt(st.nextToken()));
            } else if (op.equals("pop_front")) {
                System.out.println(pop_front());
            } else if (op.equals("pop_back")) {
                System.out.println(pop_back());
            } else if (op.equals("size")) {
                System.out.println(size());
            } else if (op.equals("empty")) {
                if (empty()) System.out.println(1);
                else System.out.println(0);
            } else if (op.equals("front")) {
                System.out.println(front());
            } else if (op.equals("back")) {
                System.out.println(back());
            }
        }
    }

    private static void push_front(int num) {
        deque.add(0,num);
    }

    private static void push_back(int num) {
        deque.add(num);
    }

    private static int pop_front() {
        if (deque.isEmpty()) return -1;
        else return deque.remove(0);
    }

    private static int pop_back() {
        if (deque.isEmpty()) return -1;
        else return deque.remove(deque.size()-1);
    }

    private static int size() {
        return deque.size();
    }

    private static boolean empty() {
        return deque.isEmpty();
    }

    private static int front() {
        if (deque.isEmpty()) return -1;
        else return deque.get(0);
    }

    private static int back() {
        if (deque.isEmpty()) return -1;
        else return deque.get(deque.size()-1);
    }
}
