class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        int ans = nums[0];

        while (left <= right) {
            // if the current segment is already sorted
            if (nums[left] <= nums[right]) {
                ans = Math.min(ans, nums[left]);
                break;
            }

            int mid = (left + right) / 2;
            ans = Math.min(ans, nums[mid]);

            if (nums[left] <= nums[mid]) {
                // left part sorted, so min is on right side
                left = mid + 1;
            } else {
                // right part sorted, so min is on left side
                right = mid - 1;
            }
        }

        return ans;
    }
}
