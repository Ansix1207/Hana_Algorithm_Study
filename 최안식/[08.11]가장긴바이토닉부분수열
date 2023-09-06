package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// TODO: 2023/08/12 11054번 가장 긴 바이토닉 부분 수열 (골드4, DP) https://www.acmicpc.net/problem/11054
// TODO: 2023/08/12 어렵네.. 아이디어 생각하기가 이해함 
public class boj_11054_가장긴바이토닉부분수열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n + 1];
        int[][] dp = new int[2][n + 1];
        StringTokenizer stk = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }



        //왼쪽부터 LIS
        for (int i = 1; i < n+1; i++) {
            dp[0][i] = 1;
            for (int j = 1; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[0][i] = Math.max(dp[0][j]+1, dp[0][i]);
                }
            }
        }
        //오른쪽 부터 LIS
        for (int i = n; i >1; i--) {
            dp[1][i] = 1;
            for (int j = n; j > i; j--) {
                if (arr[i] > arr[j]) {
                    dp[1][i] = Math.max(dp[1][j]+1, dp[1][i]);
                }
            }
        }
        int max = 0;
        for (int i = 1; i < n + 1; i++) {
            max = Math.max(max, dp[1][i] + dp[0][i]);
        }
        System.out.println(max-1);
    }


}
