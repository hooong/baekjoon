import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

/**
 * 2164번 카드2
 * 시간초과
 */
public class Baekjoon2164 {
    static List<Integer> queue = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i=1; i<=n; i++) {
            push(i);
        }

        while (size() != 1) {
            pop();
            push(pop());
        }

        System.out.println(pop());
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
