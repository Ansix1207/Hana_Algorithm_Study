package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// TODO: 2023/08/07 2225번 합분해 (골드5, DP) https://www.acmicpc.net/problem/2225
public class boj_2225_합분해 {
    /**
     * 0~N 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램.
     *
     * 덧셈의 순서가 바뀐 경우는 다른 겨웅로 센다.
     * (1+2, 2+1 은 서로 다른 경우)
     *
     *  k=2, n=3일 경우, 2개의 숫자로 3을 만드는 경우이다. 예시는
     *   0+3, 1+2, 2+1, 3+0 이다.
     *
     *   1. N=1일때
     *
     * K=1인경우 : 1가지 (1)
     * K=2인경우 : 2가지 (1+0, 0+1)
     * K=3인경우 : 3가지 (0+1+1, 1+0+1, 1+1+0)
     * 2. N=2일때
     *
     * K=1인경우 : 1가지 (2)
     * K=2인경우 : 3가지 (2+0, 0+2, 1+1)
     * K=3인경우 : 6가지 (2+0+0, 0+2+0, 0+0+2, 0+1+1, 1+0+1, 1+1+0)
     * 2. N=3일때
     *
     * K=1인경우 : 1가지 (3)
     * K=2인경우 : 4가지 (2+1, 1+2, 3+0, 0+3)
     * K=3인경우 : 10가지 (3+0+0, 0+3+0, 0+0+3, 1+1+1, 2+0+1, 1+0+2, 0+1+2, 0+2+1, 1+2+0, 2+1+0)
     *
     *    n     0   1   2   3   4   5   6
     *  k   1   1   1   1   1   1   1   1
     *      2   1  (k-1) + (n-1)
     *      3   1
     *      4   1
     *      5   1
     * */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int k = Integer.parseInt(stk.nextToken());
        long dp[][] = new long[k+1][n + 1];
        Arrays.fill(dp[1], 1);
        for(int i = 1; i<= k;i++) dp[i][0] = 1;

        for (int i = 2; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                dp[i][j]%=1000000000;
            }
        }

        System.out.println(dp[k][n]);
    }
}
