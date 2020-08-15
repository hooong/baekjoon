import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 1002번 터렛
 */
public class Baekjoon1002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        // 테스트 케이스 반복
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            Long x1 = Long.parseLong(st.nextToken());
            Long y1 = Long.parseLong(st.nextToken());
            Long r1 = Long.parseLong(st.nextToken());
            Long x2 = Long.parseLong(st.nextToken());
            Long y2 = Long.parseLong(st.nextToken());
            Long r2 = Long.parseLong(st.nextToken());

            // 두 원의 중심의 거리
            Long dx = x1 - x2;
            Long dy = y1 - y2;
            Long d = dx*dx + dy*dy;

            // r1과 r2의 합과 차
            Long add = (r1+r2) * (r1+r2);
            Long sub = (r1-r2) * (r1-r2);

            if (sub < d && d < add) {
                System.out.println(2);
            }
            else if (add.equals(d) || (sub.equals(d) && d != 0)) {
                System.out.println(1);
            }
            else if (add < d || sub > d) {
                System.out.println(0);
            }
            else if (d == 0) {
                if (r1.equals(r2)) {
                    System.out.println(-1);
                } else {
                    System.out.println(0);
                }
            }
        }
    }
}
