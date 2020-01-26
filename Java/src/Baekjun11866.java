import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * 11866번 요세푸스 문제 0
 */
public class Baekjun11866 {
    static int[] queue;
    static int n, front = 0, back = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> result = new ArrayList<>();
        n = sc.nextInt();
        int k = sc.nextInt();
        queue = new int[n];

        // 1 ~ n push
        for (int i=1; i<=n; i++) {
            push(i);
        }

        // 요세푸스 순열 만들기
        while (size() != 0) {
            for (int i=0; i<k-1; i++) {
                push(pop());
            }
            result.add(pop());
        }

        // 결과 출력
        if (n==1) {
            System.out.print('<');
            System.out.print(result.get(0));
            System.out.print('>');
        } else {
            for (int i = 0; i < result.size(); i++) {
                if (i == 0) {
                    System.out.print('<');
                    System.out.print(result.get(i));
                    System.out.print(", ");
                } else if (i == result.size() - 1) {
                    System.out.print(result.get(i));
                    System.out.print('>');
                } else {
                    System.out.print(result.get(i));
                    System.out.print(", ");
                }
            }
        }
    }

    // Queue
    private static void push(int num) {
        queue[(++back)%n] = num;
    }

    private static int pop() {
        return queue[(++front)%n];
    }

    private static int size() {
        return Math.abs(front-back);
    }

    private static boolean empty() {
        return front == back;
    }
}
