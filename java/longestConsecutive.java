import java.util.*;

class longestConsecutive {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);

        int best = 0;
        for (int x : set) {
            if (!set.contains(x - 1)) {        // start of a sequence
                int y = x;
                int len = 1;
                while (set.contains(y + 1)) {
                    y++;
                    len++;
                }
                best = Math.max(best, len);
            }
        }
        return best;
    }
}
