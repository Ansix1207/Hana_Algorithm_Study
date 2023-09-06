package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// TODO: 2023/07/26 11052번 카드 구매하기(실버1, DP 문제) https://www.acmicpc.net/problem/11052
// TODO: 2023/07/26  답변 참고

    /**
     * p1 = 1, p2 = 5, p3 = 6, p4 = 7 일때
     * dp[1] = 1개인거 선택 = 1 (가지)
     *  dp[2] = dp[1] + p[1](1인거) = 2
     *  ...   = p[2](2개 들어있는거)  =5 (O)<-이거 선택된다. max 이용해서
     *
     *  dp[3] = dp[1] + p[2] = 6   for문 두개를 돌아야 하는데 i , j
     *        = dp[2] + p[1] = 6    for 1~n 까지 i
     *        = p[3]         = 6        for 1~i 까지 j
     *                           식은 ->   dp[i]  =  MAX ( dp[i-j] + t[j], dp[i] )
     *                                      i=3, j=1 일때 dp[3-1] + t[1], dp[1]
     *                                      i=3 , j=2 일때 do[3-2] + t[2] , dp[2]
     *
     */
public class boj_11052_카드구매하기 {
    private static String[] sarr;
    static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];
        int[] dt = new int[n + 1];
        sarr = br.readLine().split(" ");
        for (int i = 1; i < n + 1; i++) {
            dt[i] = Integer.parseInt(sarr[i - 1]);
        }


        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.max(dp[i - j] + dt[j], dp[i]);
            }
        }
        System.out.println(dp[n]);
    }
}
