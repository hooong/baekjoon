import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 10828번 스택
 */
public class Baekjoon10828 {
    static List<Integer> stack = new ArrayList<>();
    static StringTokenizer st = null;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());

            String op = st.nextToken();

            if (op.equals("push")) push(Integer.parseInt(st.nextToken()));
            else if (op.equals("pop")) System.out.println(pop());
            else if (op.equals("size")) System.out.println(sizeOf());
            else if (op.equals("empty")) {
                if (isEmpty()) System.out.println(1);
                else System.out.println(0);
            }
            else if (op.equals("top")) System.out.println(top());
            else System.out.println("Error");
        }

    }

    private static void push(int num) {
        stack.add(num);
    }

    private static int pop() {
        if (isEmpty()) return -1;
        else return stack.remove(stack.size() - 1);
    }

    private static int sizeOf() {
        return stack.size();
    }

    private static Boolean isEmpty() {
        return stack.isEmpty();
    }

    private static int top() {
        if (isEmpty()) return -1;
        else return (stack.get(stack.size()-1));
    }
}
