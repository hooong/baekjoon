import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 9375번 패션왕 신해빈
 */
public class Baeckjun9375 {
    public static void main(String[] args) throws IOException {
        Map<String,Integer> clothes;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        // 테스트 반복
        for (int i=0; i<t; i++) {
            clothes = new HashMap<>();
            int n = Integer.parseInt(br.readLine());

            // Map에 Key-Value 채워넣기
            for (int j=1; j<=n; j++) {
                String[] clothe = br.readLine().split( " ");
                String kindOfClothe = clothe[1];
                if (clothes.containsKey(kindOfClothe)) {
                    clothes.put(kindOfClothe,clothes.get(kindOfClothe) + 1);
                }
                else clothes.put(kindOfClothe,1);
            }

            // 경우의 수 구하기
            int answer = 1;
            for (Integer val: clothes.values()) {
                answer *= (val + 1);
            }

            System.out.println(answer-1);
        }
    }
}
