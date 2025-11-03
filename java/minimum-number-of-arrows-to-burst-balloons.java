class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingDouble(o->o[1]));
        //1st arrow
        int count = 1;
        int lastarrow = points[0][1];
        for(int i=1;i<points.length;i++){
            if(points[i][0]>lastarrow){
                count++;
                lastarrow =points[i][1];
            }
        }
        return count;
    }
}
