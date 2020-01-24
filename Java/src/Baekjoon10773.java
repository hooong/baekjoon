import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * 10773번 제로
 */
public class Baekjoon10773 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> stack = new ArrayList<>();

        int k = sc.nextInt();

        for (int i=0; i<k; i++) {
            int num = sc.nextInt();

            if (num == 0) {
                stack.remove(stack.size()-1);
            } else {
                stack.add(num);
            }
        }

        int sum = 0;
        for (Integer n : stack) {
            sum += n;
        }

        System.out.println(sum);
    }
}