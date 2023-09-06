package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

// TODO: 2023/08/01 2146번 다리만들기 (골드3) https://www.acmicpc.net/problem/2146 
// TODO: 2023/08/01 성공 
public class boj_2146_다리만들기 {
    static int[][] arr;
    static boolean[][] visit;
    static Queue<int[]> q;
    static int n;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n + 1][n + 1];
        visit = new boolean[n + 1][n + 1];
        q = new LinkedList<>();

        for (int i = 1; i < n + 1; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            for (int j = 1; j < n + 1; j++) {
                arr[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        //첫 단계는 각 섬의 값들이 같으니, 섬들의 값을 다르게 하여 섬을 구분해준다.
        landCount();
        //두번째 단계 섬과 섬사이 최단거리를 구한다.
        int min = Integer.MAX_VALUE;
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                //모든 섬에 대해서 bfs 섬과 섬사이 거리 구하기를 시도한다.
                if (arr[i][j] > 0) {
                    // 매 시도마다 visit 을 초기화해주고 내부 로직에서는 현재 내 섬의 값 num
                    // 과 같지 않은 값들만 즉, 내 섬이면 큐에 값을 추가하지 않아서 진행하지 않게한다.
                    // 0(바다) 이면 큐에 넣고, 0(바다)가 아니면서 num(땅 번호)가 지금 bfs 대상과 다른경우는
                    // 다른 섬에 도착했음을 알려주고 현재까지의 거리 값을 반환한다.
                    // 탐색에 실패했을 경우는 -1을 반환해서 계속 진행한다.
                    visit = new boolean[n + 1][n + 1];
                    int res = bridge(i,j);
                    if(res == -1 )continue;
                    if (min > res) {
                        min = res;
                    }
                }
            }
        }
        System.out.println(min-1);
    }

    static int bridge(int x, int y) {
        q = new LinkedList<>();

        int num = arr[x][y];
        visit[x][y] = true;
        q.add(new int[]{x,y,0});

        while (!q.isEmpty()) {
            int[] pos = q.poll();
            int px = pos[0];
            int py = pos[1];
            int bridge = pos[2];

            if (arr[px][py] != 0 && arr[px][py] != num) {
                return bridge;
            }

            for (int i = 0; i < 4; i++) {
                int nx = px + dx[i];
                int ny = py + dy[i];

                if(nx<1 || nx>n || ny <1 || ny>n) continue;
                if(visit[nx][ny] ||arr[nx][ny] == num) continue;

                visit[nx][ny] = true;
                q.add(new int[]{nx, ny, bridge + 1});
            }
        }
        return -1;
    }
    static void landCount() {
        int idx = 2;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (!visit[i][j] && arr[i][j] != 0) {
                    arr[i][j] = idx;
                    visit[i][j] = true;
                    q.add(new int[]{i,j});

                    while (!q.isEmpty()) {
                        int[] pos = q.poll();
                        int px = pos[0];
                        int py = pos[1];

                        for (int p = 0; p < 4; p++) {
                            int nx = px + dx[p];
                            int ny = py + dy[p];

                            if (nx < 1 || nx > n || ny < 1 || ny > n) continue;
                            if (visit[nx][ny]) continue;

                            if (arr[nx][ny] == 1) {
                                visit[nx][ny] = true;
                                arr[nx][ny] = idx;
                                q.add(new int[]{nx, ny});
                            }
                        }
                    }
                    idx++;
                }
            }
        }
    }

}
