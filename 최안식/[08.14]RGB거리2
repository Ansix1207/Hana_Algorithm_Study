package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// TODO: 2023/08/14 17404번 RGB거리2 (골드 4) https://www.acmicpc.net/problem/17404
// TODO: 2023/08/14 어렵다 참고하고 이해함
public class boj_17404_RGB거리2 {
    static int[][] dp2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n + 1][n + 1];
        int[][] dp = new int[n + 1][n + 1];
        dp2 = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            for (int j = 1; j <= 3; j++) {
                arr[i][j] = Integer.parseInt(stk.nextToken());
            }
        }
        int min = Integer.MAX_VALUE;

        for (int k = 1; k < 4; k++) {//어떤 집의 색을 칠할지
            for (int i = 1; i <= 3; i++) {
                if(i==k)//해당하는 집만 칠하고
                    dp[1][i] = arr[1][i];
                else//나머지 색상은 선택해도 답이 아니도록
                    dp[1][i] = 1000000;
            }

            for (int i = 2; i < n+1; i++) {
                dp[i][1] = Math.min(dp[i - 1][2] , dp[i - 1][3]) + arr[i][1];
                dp[i][2] = Math.min(dp[i - 1][1] , dp[i - 1][3]) + arr[i][2];
                dp[i][3] = Math.min(dp[i - 1][2] , dp[i - 1][1]) + arr[i][3];
            }

            for (int i = 1; i < 4; i++) {
                if (i != k) {//i==k, 즉 첫번째 고른 집이 아닌것들중에서 가장 최소값 계속 업데이트
                    min = Math.min(dp[n][i], min);
                }
            }

        }
        System.out.println(min);
    }
}
