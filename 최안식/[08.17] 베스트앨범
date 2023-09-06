package Programmers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class pgm_베스트앨범 {

    public static void main(String[] args) throws IOException {
        Solution s = new Solution();
        s.solution(new String[]{"classic", "pop", "classic", "classic", "pop"},
                new int[]{500, 600, 150, 800, 2500});
    }
   static class Solution {
        public int[] solution(String[] genres, int[] plays) {
            HashMap<String, Integer> num = new HashMap<>(); //장르별 총 개수
            //장르에 속하는 노래 및 재생횟수
            HashMap<String, HashMap<Integer, Integer>> music = new HashMap<>();
            for (int i = 0; i < genres.length; i++) {
                if (!num.containsKey(genres[i])) {
                    HashMap<Integer, Integer> map = new HashMap<>();
                    map.put(i, plays[i]);
                    music.put(genres[i], map);
                    num.put(genres[i], plays[i]);
                } else{
                    music.get(genres[i]).put(i, plays[i]);
                    num.put(genres[i], num.get(genres[i]) + plays[i]);
                }
            }
            List<String> keySet = new ArrayList(num.keySet());
            Collections.sort(keySet, (s1, s2) -> num.get(s2) - num.get(s1));

            ArrayList<Integer> answer = new ArrayList();
            for (String s : keySet) {
                HashMap<Integer, Integer> tempMap = music.get(s);
                ArrayList<Integer> key = new ArrayList<>(tempMap.keySet());
                Collections.sort(key, (s1, s2) -> tempMap.get(s2) - tempMap.get(s1));

                //문제에서는 가장 많이 실행된 횟수로 정렬된 상태에서
                //고유번호 (idx) 을 원했기 때문에 키값만 출력
                answer.add(key.get(0));
                if (key.size() > 1) {
                    answer.add(key.get(1));
                }
            }

            return answer.stream().mapToInt(Integer::intValue).toArray();
        }
    }
}
