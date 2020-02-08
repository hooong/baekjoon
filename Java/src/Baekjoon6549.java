import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 6549번 히스토그램에서 가장 큰 직사각형
 */
public class Baekjoon6549 {
    static int[] tree;
    static int[] histo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            if (n==0) {
                break;
            }

            histo = new int[n];
            for (int i = 0; i < n; i++) {
                histo[i] = Integer.parseInt(st.nextToken());
            }

            int h = (int)(Math.ceil(Math.log(n) / Math.log(2)));
            int t_size = (int) Math.pow(2, h) * 2;
            tree = new int[t_size];

            init(1,0,n-1);

            System.out.println(getMaxArea(0,n-1));

        }
    }

    private static void init(int node, int start, int end) {
        if (start == end) {
            tree[node] = start;
        } else {
            int mid = (start + end) / 2;
            init(node*2, start, mid);
            init(node*2+1, mid+1, end);
            if (histo[tree[node*2]] <= histo[tree[node*2+1]])
                tree[node] = tree[node*2];
            else tree [node] = tree[node*2+1];
        }
    }

    private static int query(int node, int start, int end, int left, int right) {
        if (right < start || left > end)
            return -1;
        if (left <= start && end <= right)
            return tree[node];

        int mid = (start + end) / 2;
        int l = query(node*2, start, mid, left, right);
        int r = query(node*2+1, mid+1, end, left, right);
        if (l == -1) return r;
        else if (r == -1) return l;
        else {
            if (histo[l] < histo[r]) return l;
            else return r;
        }
    }

    private static int getMaxArea(int left, int right) {
        int min = query(1,0, histo.length-1,left,right);
        int area = (right - left + 1) * histo[min];

        if (left <= min-1) {
            int tmp_area = getMaxArea(left,min-1);
            if (tmp_area > area) area = tmp_area;
        }
        if (min+1 <= right) {
            int tmp_area = getMaxArea(min+1,right);
            if (tmp_area > area) area = tmp_area;
        }
        return area;
    }
}
