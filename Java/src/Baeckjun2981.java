import java.util.Arrays;
import java.util.Scanner;

/**
 * 2981번 검문
 */
public class Baeckjun2981 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] nums = new int[n+1];
        for (int i=1; i<=n; i++) {
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);

        int gcd = nums[2] - nums[1];
        for (int i=3; i<=n; i++) {
            gcd = findGcd(Math.max(gcd, nums[i] - nums[i-1]), Math.min(gcd, nums[i] - nums[i-1]));
        }

        for (int i=2; i<=gcd; i++) {
            if (gcd % i == 0) {
                System.out.print(i);
                System.out.print(' ');
            }
        }
    }

    private static int findGcd(int a, int b) {
        while(b != 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }

    // 시간초과
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//
//        int[] nums = new int[n+1];
//        for (int i=1; i<=n; i++) {
//            nums[i] = sc.nextInt();
//        }
//
//        Arrays.sort(nums);
//
//        for (int i=2; i<=nums[2]; i++) {
//            int remainder = nums[1] % i;
//            if (remainder > nums[1]) continue;
//
//            boolean isSame = true;
//            for (int j=2; j<nums.length; j++) {
//                if (remainder != nums[j] % i) {
//                    isSame = false;
//                    break;
//                }
//            }
//
//            if (isSame) {
//                System.out.print(i);
//                System.out.print(' ');
//            }
//        }
//    }
}
