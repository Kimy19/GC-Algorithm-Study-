import java.util.*;

class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            String[] ans = Integer.toString(sc.nextInt()).split("");
            int time = sc.nextInt();
            int len = ans.length;

            Queue<Num> ansL = new LinkedList<>();
            ansL.add(new Num(ans, 0, 0));

            boolean end = false;

            while(!end) {
                int size = ansL.size();
                for(int i=0; i<size; i++) {
                    Num x = ansL.poll();
                    List<Integer> maxL = x.getMaxIdxList();
                    for(int max : maxL) {
                        if(x.loc == max) {
                            x.loc++;
                            ansL.add(x);
                            break;
                        }
                        String[] tmp = x.numArray.clone();
                        swap(tmp, x.loc, max);
                        Num n = new Num(tmp, x.loc+1, x.cnt+1);
                        ansL.add(n);
                    }
                }
                end = ansL.stream().allMatch(x -> x.isEnd(len, time));
            }

            //남은 교환 횟수
            if(ansL.stream().mapToInt(x -> toInteger(x.numArray)).allMatch(new HashSet<>()::add))
                ansL.stream()
                        .filter(x -> x.loc == len && (time - x.cnt) % 2 != 0)
                        .forEach(x -> swap(x.numArray, len-1, len -2));

            //후보 중 최대값
            int answer = ansL.stream()
                    .mapToInt(n -> toInteger(n.numArray))
                    .max()
                    .orElse(-1);

            System.out.println("#" + test_case + " " + answer);

        }
    }
    public static void swap(String[] arr, int x, int y) {
        String tmp = arr[x];
        arr[x] = arr[y];
        arr[y] = tmp;
    }
    public static List<Integer> getMaxIdxList(String[] arr, int first) {
        List<Integer> maxL = new ArrayList<>();
        int max = first;
        maxL.add(max);
        for (int i = first + 1; i < arr.length; i++) {
            int cmp = arr[max].compareTo(arr[i]);
            if (cmp < 0) {
                max = i;
                maxL.clear();
                maxL.add(i);
            } else if (cmp == 0) maxL.add(i);
        }
        return maxL;
    }
    public static int toInteger(String[] arr) {
        StringBuilder sb = new StringBuilder();
        for (String x : arr) sb.append(x);
        return Integer.parseInt(sb.toString());
    }
    private static class Num {
        String[] numArray;
        int loc;
        int cnt;

        Num(String[] numArray, int loc, int cnt) {
            this.numArray = numArray.clone();
            this.loc = loc;
            this.cnt = cnt;
        }
        boolean isEnd(int len, int time) {
            return (len <= loc) || (time <= cnt);
        }
        List<Integer> getMaxIdxList() {
            List<Integer> maxL = new ArrayList<>();
            int max = loc;
            for (int i = loc + 1; i < numArray.length; i++) {
                int cmp = numArray[max].compareTo(numArray[i]);
                if (cmp < 0) {
                    max = i;
                    maxL.clear();
                    maxL.add(i);
                }
                else if (cmp == 0) maxL.add(i);
            }
            if(maxL.size() == 0) maxL.add(loc);
            return maxL;
        }
    }
}
