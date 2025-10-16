import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] res = twoSum(nums, target);
        System.out.println("Indices: " + res[0] + ", " + res[1]); // 0, 1
    }

    // O(n) time, O(n) space
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> idx = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];
            if (idx.containsKey(need)) return new int[]{idx.get(need), i};
            idx.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
