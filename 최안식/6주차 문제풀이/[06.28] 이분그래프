package BaekJoon;

import java.io.*;
import java.util.*;

/**
 * 성장했구나 나 이거 풀었다 1시간 넘게 걸렸네 ㅋ..
 * */
// TODO: 2023/06/29 1701번 이분그래프 https://www.acmicpc.net/problem/1707
// TODO: 2023/06/29 !!성공!!
public class boj_1701_이분그래프 {
    static int k,v,e;
    static int[][] graph;
    static boolean[] visit;
    static int[] rb;
    static ArrayList<Integer>[] list;
    static ArrayList<Boolean>  andList;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        k = Integer.parseInt(stk.nextToken());
        for (int i = 1; i < k+1; i++) { //k번 체크할거임
            stk = new StringTokenizer(br.readLine());
            v = Integer.parseInt(stk.nextToken()); //정점의 개수
            e = Integer.parseInt(stk.nextToken()); //간선의 개수
            list = new ArrayList[v+1];
            visit = new boolean[v + 1];
            rb = new int[v + 1];
            andList = new ArrayList<>();
            for (int j = 1; j < v + 1; j++) { //정점의 개수만큼 만들어주고
                list[j] = new ArrayList<>();
            }
            for (int j = 1; j < e + 1; j++) { // 간선의 개수만큼 넣어준다.
                stk = new StringTokenizer(br.readLine());
                int x =Integer.parseInt(stk.nextToken());
                int y =Integer.parseInt(stk.nextToken());
                list[x].add(y);
                list[y].add(x);
            }
            for (int s = 1; s <v+1; s++) {
                if(visit[s]!=true){
                    boolean b = bfs(s);
                    andList.add(b);
                }
            }
            boolean result = true;
            for (Boolean aBoolean : andList) {
                result = result & aBoolean;
            }
            if (result) {
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }

    }

    static boolean bfs(int start) {
        Queue<Integer> q = new LinkedList();
        //bfs 큐에 먼저 start 값을 넣어준다.
        //시작하는 start 값에 대하여 방문처리를 해준다.
        q.add(start);
        visit[start] = true;
        rb[start] = 1;
        boolean flag = false;
        if (list[start].size() == 0) {
            return true;
        }
        while (!q.isEmpty()) { //큐에 들어간걸 꺼내서 쓸껀데 큐가 비지 않았으면 반복
            start = q.poll(); // 큐에 들어간걸 꺼내서 방문을 시작한다.
//            System.out.print(start + " ");
            for (Integer integer : list[start]) {
                if(!visit[integer]){
                    if(rb[start]==1){//부모가 1이면, 자식은 반대인 2 이다.
                        rb[integer] = 2;
                    } else{
                        rb[integer] = 1;
                    }
                    visit[integer] = true;
                    q.add(integer);
                }
                if(rb[integer]!=0){ //rb 어떤거든 선택 됐으면
                    if(rb[integer]==rb[start]){//지금 자신이랑, 부모랑 체크
//                        System.out.println("NO");
                        return false;
                    }else{
                        flag = true;
                    }
                }
            }
        }
        /**
         * 1
         * 5 3
         * 2 4          2 --- 4
         *                    ㅣ
         * 3 5          3 --- 5
         * 4 5   <-- 반례
         * */
        if (flag == true) {
//            System.out.println("YES");
            return true;
        }else{
            return false;
        }
    }
}
