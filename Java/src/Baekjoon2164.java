import java.util.Scanner;

/**
 * 2164번 카드2
 */
public class Baekjoon2164 {
    static int[] queue;
    static int n, front = 0, back = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        if (n==1) System.out.println(1);
        else {
            queue = new int[n];

            // 짝수들만 오름차순으로 push
            for (int i = 2; i <= n; i += 2) {
                push(i);
            }

            // 홀수일경우 처음 수를 맨 뒤로 보냄
            if (n % 2 != 0) {
                push(pop());
            }

            while (size() != 1) {
                pop();
                push(pop());
            }

            System.out.println(pop());
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
