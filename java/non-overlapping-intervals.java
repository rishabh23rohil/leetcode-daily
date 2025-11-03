class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingDouble(o -> o[1]));
        //1 st interval
        int count = 1;
        int lastEnd = intervals[0][1];
        for(int i = 1; i <intervals.length;i++){
            if(intervals[i][0]>=lastEnd){
                count++;
                lastEnd = intervals[i][1];         // update end
            }
        }
        return intervals.length - count; 
    }
}
