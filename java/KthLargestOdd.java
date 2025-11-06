public class KthLargestOdd {
    public static int findKthLargestOdd(int L, int R, int K) {
        // Find largest odd ≤ R
        int lastOdd = (R % 2 == 0) ? R - 1 : R;

        // Find smallest odd ≥ L
        int firstOdd = (L % 2 == 0) ? L + 1 : L;

        // Check if there are any odd numbers
        if (firstOdd > lastOdd) {
            return 0;
        }

        // Count of odd numbers in the range
        int count = ((lastOdd - firstOdd) / 2) + 1;

        // If K is greater than available odds
        if (K > count) {
            return 0;
        }

        // Greedily compute Kth largest odd
        return lastOdd - 2 * (K - 1);
    }

    public static void main(String[] args) {
        int L = -3, R = 3, K = 1;
        System.out.println(findKthLargestOdd(L, R, K)); // Output: 3
    }
}
