import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 2580번 스도쿠
 */
public class Baeckjun2580 {

    static int N = 9;
    static int[][] panel;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        panel = new int[N][N];

        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                panel[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        sdoku(0,0);

    }

    static void print() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                System.out.print(panel[i][j]);
                System.out.print(' ');
            }
            System.out.println();
        }
        // 여러 경우가 print될 경우를 대비하기 위해 한번 출력하면 프로그램 종료!
        System.exit(0);
    }

    static void sdoku(int r, int c) {
        if (panel[r][c]==0) {
            for (int num=1; num<=9; num++) {
                panel[r][c] = num;
                if (promising(r, c)) {
                    if (r==N-1 && c==N-1) print();
                    else if (r == N - 1) sdoku(r, c + 1);
                    else if (c == N - 1) sdoku(r + 1, 0);
                    else sdoku(r, c + 1);
                }
                panel[r][c] = 0;
            }
        } else {
            if (r==N-1 && c==N-1) print();
            else if (r == N - 1) sdoku(r, c + 1);
            else if (c == N - 1) sdoku(r + 1, 0);
            else sdoku(r, c + 1);
        }
    }

    static boolean promising(int r, int c) {
        // 세로
        for (int i=0; i<N; i++) {
            if (i==r) continue;
            if (panel[r][c] == panel[i][c]) return false;
        }
        // 가로
        for (int i=0; i<N; i++) {
            if (i==c) continue;
            if (panel[r][c] == panel[r][i]) return false;
        }
        // 3*3
        for (int i=(r/3)*3; i<(r/3)*3+3; i++) {
            for (int j=(c/3)*3; j<(c/3)*3+3; j++) {
                if (i==r && j==c) continue;
                if (panel[r][c] == panel[i][j]) return false;
            }
        }
        return true;
    }

}
