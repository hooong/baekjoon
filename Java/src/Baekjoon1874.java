import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * 1874번 스택 수열
 */
public class Baekjoon1874 {
    static List<Integer> stack = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Character> result = new ArrayList<>();

        int n = sc.nextInt();

        int[] seq = new int[n+1];

        for (int i=1; i<=n; i++) {
            seq[i] = sc.nextInt();
        }

        int seqIndex = 1;
        for (int i=1; i<=n; i++) {
            // 우선 i를 push하고 본다.
            push(i);
            result.add('+');

            // i와 현재 인덱스의 수열과 같으면 pop
            if (i == seq[seqIndex]) {
                pop();
                result.add('-');
                seqIndex++;
            }

            // stack이 비어있지않고 top값이 수열과 같으면 pop
            while (!stack.isEmpty() && top() == seq[seqIndex]) {
                pop();
                result.add('-');
                seqIndex++;
            }
        }

        // stack이 비어있다면 수열 완성
        if (stack.isEmpty()) {
            for (Character op: result) {
                System.out.println(op);
            }
        } else System.out.println("NO");


    }

    private static void push(int num) {
        stack.add(num);
    }

    private static void pop() {
        if (stack.isEmpty()) {
            System.out.println("Error");
            System.exit(-1);
        } else {
            stack.remove(stack.size()-1);
        }
    }

    private static int top() {
        if (stack.isEmpty()) {
            System.out.println("Error");
            System.exit(-1);
        }
        return stack.get(stack.size()-1);
    }
}
