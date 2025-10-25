public class MaxSubarray {
    public static void main(String[] args) {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

        System.out.println("Kadane O(n): " + maxSubArrayKadane(nums));
        System.out.println("Brute Force O(n^2): " + maxSubArrayBruteForce(nums));
        System.out.println("Divide & Conquer O(n log n): " + maxSubArrayDivideConquer(nums));
    }

    // ---------- O(n): Kadane's Algorithm ----------
    public static int maxSubArrayKadane(int[] nums) {
        int maxSoFar = nums[0];
        int current = nums[0];
        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            maxSoFar = Math.max(maxSoFar, current);
        }
        return maxSoFar;
    }

    // ---------- O(n^2): Brute force with running sum ----------
    // For each left index, extend rightwards and keep a running sum.
    public static int maxSubArrayBruteForce(int[] nums) {
        int n = nums.length;
        int best = nums[0];
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum > best) best = sum;
            }
        }
        return best;
    }

    // ---------- O(n log n): Divide & Conquer ----------
    public static int maxSubArrayDivideConquer(int[] nums) {
        return dc(nums, 0, nums.length - 1);
    }

    private static int dc(int[] a, int l, int r) {
        if (l == r) return a[l];
        int m = (l + r) >>> 1;

        int leftBest = dc(a, l, m);
        int rightBest = dc(a, m + 1, r);

        // Best crossing sum (must include a[m] and a[m+1])
        int sum = 0, leftMax = Integer.MIN_VALUE, rightMax = Integer.MIN_VALUE;

        for (int i = m; i >= l; i--) {
            sum += a[i];
            if (sum > leftMax) leftMax = sum;
        }
        sum = 0;
        for (int i = m + 1; i <= r; i++) {
            sum += a[i];
            if (sum > rightMax) rightMax = sum;
        }
        int crossBest = leftMax + rightMax;

        return Math.max(crossBest, Math.max(leftBest, rightBest));
    }
}
