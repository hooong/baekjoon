import java.util.Scanner;

/**
 * 9663번 N-Queen
 */
public class Baeckjun9663 {
    static int[] visit;
    static int n;
    static int count = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        visit = new int[n+1];

        nQueen(1);

        System.out.println(count);
    }

    static void nQueen(int r) {
        for (int c=1; c<=n; c++) {
            if (check(r,c)) {
                visit[r] = c;
                if (r == n) {
                    count++;
                } else nQueen(r + 1);
            }
        }
    }

    static boolean check(int r, int c) {
        for (int i=1; i<r; i++) {
            if (visit[i] == c || r-i == Math.abs(visit[i]-c)) {
                return false;
            }
        }
        return true;
    }

    // 시간 초과
//    static boolean[][] visit;
//    static int n;
//    static int count = 0;
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        n = sc.nextInt();
//        visit = new boolean[n+1][n+1];
//
//        nqueen(1);
//
//        System.out.println(count);
//    }
//
//    static void nqueen(int r) {
//        for (int c=1; c<=n; c++) {
//            if (confirm(r, c)) {
//                visit[r][c] = true;
//                if (r==n) {
//                    count++;
//                } else nqueen(r + 1);
//            }
//            visit[r][c] = false;
//        }
//    }
//
//    static boolean confirm(int r, int c) {
//        if (r==1) {
//            return true;
//        }
//        else {
//            for (int i=1; i<r; i++) {
//                // 왼쪽 대각선
//                for (int j=1; j<c; j++) {
//                    if (r - c == i - j) {
//                        if (visit[i][j]) return false;
//                    }
//                }
//                // 같은 열
//                if (visit[i][c]) return false;
//                // 오른쪽 대각선
//                for (int j=c+1; j<=n; j++) {
//                    if ((r+c) == (i+j)) {
//                        if (visit[i][j]) return false;
//                    }
//                }
//            }
//            return true;
//        }
//    }
}
