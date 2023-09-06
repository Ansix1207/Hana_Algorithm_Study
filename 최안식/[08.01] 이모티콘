package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// TODO: 2023/08/01 14226번 이모티콘(골드4) https://www.acmicpc.net/problem/14226
// TODO: 2023/08/01 !!성공!!


public class boj_14226_이모티콘 {

    public static class Step {
        int emoticon_num;
        int clipboard_num;
        int time;

        public Step(int emoticon_num, int clipboard_num, int time) {
            this.emoticon_num = emoticon_num;
            this.clipboard_num = clipboard_num;
            this.time = time;
        }
    }

    static boolean[][] visit;
    static int v;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        v = Integer.parseInt(br.readLine());
        //행 : 화면 이모티콘의 개수
        //열 : 클립보드 이모티콘 개수
        visit = new boolean[2001][2001];
        bfs();
    }

    public static void bfs() {
        Queue<Step> queue = new LinkedList<>();
        queue.add(new Step(1, 0, 0));

        while (!queue.isEmpty()) {
            Step now = queue.poll();

            int emotion_num = now.emoticon_num;
            int clipboard_num = now.clipboard_num;
            int time = now.time;

            if (emotion_num == v) {
                System.out.println(time);
                return;
            }

            if (emotion_num > 0 && emotion_num < 2000) {
                //n번째 에서 복사하는 경우
                //행 : 화면 이모티콘의 개수
                //열 : 클립보드 이모티콘 개수
                if (!visit[emotion_num][emotion_num]) {
                    visit[emotion_num][emotion_num] = true;
                    queue.offer(new Step(emotion_num, emotion_num, time + 1));
                }
                //화면에서 하나 삭제한 경우
                //행 : 화면 이모티콘의 개수
                //열 : 클립보드 이모티콘 개수
                if (!visit[emotion_num - 1][clipboard_num]) {
                    visit[emotion_num - 1][clipboard_num] = true;
                    queue.offer(new Step(emotion_num - 1, clipboard_num, time + 1));
                }
            }
            //이모티콘 붙여넣는 경우
            if (clipboard_num > 0 && emotion_num + clipboard_num < 2000) {
                if (!visit[emotion_num + clipboard_num][clipboard_num]) {
                    visit[emotion_num + clipboard_num][clipboard_num] = true;
                    queue.offer(new Step(emotion_num + clipboard_num, clipboard_num, time + 1));
                }
            }
        }
    }
}
