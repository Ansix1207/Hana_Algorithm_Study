package BaekJoon;

// TODO: 2023/08/02 14002번 가장 긴 증가하는 부분 수열 4 https://www.acmicpc.net/problem/14002
// TODO: 2023/08/03 특성 객체를 이용하여 풀다가 역추적 부분에서 애를 먹고 배열을 통한 역추적 코드보고 이해함
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_14002_가장긴증가하는부분수열4 {
    public static class Step{
        int dt_v;
        LinkedList<Integer> q;
        public Step(int dt_v, LinkedList<Integer> q) {
            this.dt_v = dt_v;
            this.q = q;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        int[] arr = new int[n+1];
        StringTokenizer stk = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            arr[i] = Integer.parseInt(stk.nextToken());
        }
//        if(n==1){
//            System.out.println(1);
//            System.out.printf("%d",arr[n-1]);
//            return;
//        }
        dp[0] = 0;
        ArrayList<Step> resq = new ArrayList<>();
        int result = 0;
        //dp 배열 만들기
        for (int i = 1; i < n + 1; i++) {
            //고정할 배열부터, 이번 모든 값들을 비교한다.
            for (int j = 0; j < i; j++) {
                if(arr[i]>arr[j]){
                    //비교한 값의 dp값 + 1, 기존 dp 값을 비교하여 가장 큰 값을 저장한다.
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    // 최장 길이인 정답을 구하기 위해서 result에
                    // 지금까지 구한 dp값 중 가장 큰 값을 저장한다.
                    result = Math.max(result,dp[i]);
                }
            }
        }
        //최장길이 먼저 출력 해주고
        System.out.println(result);

        //역추적을 위해서 최장 길이 수열의 가장 마지막 값
        int value = result;
        Stack<Integer> stack = new Stack<>();

        for (int i = n; i >= 1; i--) {
            //현재 찾는 길이와 같은 경우에
            if (value == dp[i]) {
                //stack에 실제 값을 push 한다.
                stack.push(arr[i]);
                //찾는 길이를 찾았으므로 -1을 해주어 다음에 찾을 길이를 설정해서 한다..
                value--;
            }
        }

        while (!stack.isEmpty()) {
            System.out.print(stack.pop()+" ");
        }
//        for (int i = 1; i < n; i++) {
//            LinkedList<Integer> q = new LinkedList<>();
//            dp[i]=1;
//            for (int j = 0; j < i; j++) {
//                //dp 식은...
//                //lts 였나
//                if (arr[i] > arr[j]) {
//                    dp[i] = Math.max(dp[i], dp[j] + 1);
//                    if(!q.contains(arr[j])){
//                            q.add(arr[j]);
//                    }
//                }
//            }
//            if(!q.contains(arr[i]))
//                q.add(arr[i]);
//            resq.add(new Step(dp[i], q));
//        }
//
//        int max = 0;
//        Step max_step = null;
//        for (Step i : resq) {
//            if (i.dt_v > max) {
//                max_step = i;
//            }
//        }
//        Collections.sort(max_step.q);
//        if (max_step != null) {
//            System.out.println(max_step.dt_v);
//            while (!max_step.q.isEmpty()) {
//                System.out.print(max_step.q.poll()+" ");
//            }
//        }
//        Step step = resq.get();
//        for (Integer integer : step.q) {
//            System.out.print(integer+ " ");
//        }
//        System.out.println(dt[step.size]);
    }
}
