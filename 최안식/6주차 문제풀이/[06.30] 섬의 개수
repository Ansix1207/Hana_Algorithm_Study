package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

// TODO: 2023/07/01 4963번 섬의 개수 (실버2) https://www.acmicpc.net/problem/4963
// TODO: 2023/07/01 !성공!
public class boj_4963_섬의개수 {
    static int node[][]; // 배열
    static int check[][]; // 방문여부 배열
    static int cnt =1;
    static ArrayList<Integer> array = new ArrayList<>(); //수를 저장
    static int w;
    static int h;
    // 기준행을 기준으로 방문하지 않은 곳이면서 1의 값을 가지는 곳을 상,하,좌,우로 살펴본다
    static void dfs(int x,int y) { // 배열에서 각 점을 인자로 전달
        check[x][y] =1; // 전달 된 인자는 방문했으므로 1저장
        // cnt변수는 초기화했기 때문에 별도의 증가는 필요없다.

        // 기준열의 오른쪽열을 확인해야 하므로 범위에서+1, 오른쪽열이 1이면서 방문하지 않았다면
        if( y<h-1 && node[x][y+1]==1 && check[x][y+1]==0) {
//            System.out.println("오른쪽 들어옴");
            dfs(x,y+1); // 오른쪽열로 이동
        }

        //기준 열의 오른쪽 위를 확인해야함으로, 범위에서 -1,+1
        if ((y < h - 1 && x  > 0) && node[x - 1][y + 1] == 1 && check[x - 1][y + 1] == 0) {
//            System.out.println("오른쪽 위 들어옴");
            dfs(x - 1, y + 1);//오른쪽 위로 이동
        }

        //기준행의 아랫쪽행을 확인해야 하므로 범위에서+1, 아랫쪽행이 1이면서 방문하지 않았다면
        if(x<w-1 && node[x+1][y]==1 && check[x+1][y]==0) {
//            System.out.println("아래 들어옴");
            dfs(x+1,y); // 아랫쪽으로 이동
        }
        //기준 열의 오른쪽 아래를 확인해야함으로, 범위에서 +1,+1
        if ((y < h - 1 && x  < w-1) && node[x + 1][y + 1] == 1 && check[x + 1][y + 1] == 0) {
//            System.out.println("오른쪽 아래 들어옴");
            dfs(x + 1, y + 1);//오른쪽 아래로 이동
        }
        //기준열의 왼쪽열을 확인해야 하므로 0보다 커야하며, 왼쪽열이 1이면서 방문하지 않았다면
        if(y>0 &&  node[x][y-1]==1&& check[x][y-1]==0) {
//            System.out.println("왼쪽 들어옴");
            dfs(x,y-1); // 왼쪽으로 이동
        }
        //기준 열의 왼쪽 위를 확인해야함으로, 범위에서 -1,-1
        if ((y > 0  && x  >0) && node[x - 1][y - 1] == 1 && check[x -1][y -1] == 0) {
//            System.out.println("왼쪽 위 들어옴");
            dfs(x - 1, y - 1);//왼쪽 위로 이동
        }
        //기준행의 윗쪽행을 확인해야 하므로 0보다 커야하며, 윗쪽행이 1이면서 방문하지 않았다면
        if(x>0 &&  node[x-1][y]==1&& check[x-1][y]==0) {
//            System.out.println("위 들어옴");
            dfs(x-1,y); // 윗쪽으로 이동
        }
        //기준 열의 왼쪽 아래를 확인해야함으로, 범위에서 +1,-1
        if ((y > 0 && x  < w-1) && node[x + 1][y - 1] == 1 && check[x + 1][y - 1] == 0) {
//            System.out.println("왼쪽 아래 들어옴");
            dfs(x + 1, y - 1); //왼쪽 아래 이동
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            h= Integer.parseInt(stk.nextToken()); // 지도의 크기 n
            w= Integer.parseInt(stk.nextToken()); // 지도의 크기 n
            if (w == 0 && h == 0) {
                break;
            }
            node = new int[w][h]; // 지도 배열
            check = new int[w][h]; // 지도 방문배열 4,5 -> 3,4
            for(int i=0;i<w;i++) {
                String[] row = br.readLine().split(" ");
                for(int j=0;j<h;j++) {
                    // char -> int 숫자로 변환 위해서 빼준다.
                    node[i][j] = row[j].charAt(0)-'0'; //- '0' =  48
                }
            }
            int cntt =0; // cnt변수 초기화
            for(int i=0;i<w;i++) {
                for(int j=0;j<h;j++) {
                    if(node[i][j] == 1 && check[i][j]==0) { // 1의값이면서 방문하지 않은 곳의 정보만 전달
                        dfs(i,j);// 지도의 (0,0)부터 전달
                        cntt++;
                    }
                }
            }
            array.add(cntt); // 어레이 리스트에 저장
        }
        for(int i=0;i<array.size();i++) {
            System.out.println(array.get(i));
        }
    }

}
