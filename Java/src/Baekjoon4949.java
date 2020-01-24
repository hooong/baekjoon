import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 4949번 균형잡힌 세상
 */
public class Baekjoon4949 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] str = br.readLine().toCharArray();

        while (str[0] != '.') {

            int i = 0;
            List<Character> stack = new ArrayList<>();
            boolean isValid = true;

            while (str[i] != '.' && isValid) {
                if (str[i] == '(') stack.add('(');
                else if (str[i] == '[') stack.add('[');
                else if (str[i] == ')') {
                    if (!stack.isEmpty() && stack.get(stack.size() - 1) == '(')
                        stack.remove(stack.size()-1);
                    else isValid = false;
                }
                else if (str[i] == ']') {
                    if (!stack.isEmpty() && stack.get(stack.size()-1) == '[')
                        stack.remove(stack.size()-1);
                    else isValid = false;
                }
                i++;
            }

            if (isValid && stack.isEmpty())
                System.out.println("yes");
            else System.out.println("no");

            str = br.readLine().toCharArray();
        }
    }
}
