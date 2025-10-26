class MaxSubarray {
    public int maxSubArray(int[] nums) {
        int cs = 0;
        int ms = Integer.MIN_VALUE;
        int maxnumber = Integer.MIN_VALUE;
        for(int i =0; i< nums.length;i++){
            cs = cs+nums[i];

            if(cs<0){
                cs = 0;
            }
            ms = Math.max(cs,ms);
            maxnumber = Math.max(maxnumber,nums[i]);
        }
        if(ms == 0 && maxnumber<0){
            return maxnumber;
        }
        return ms;
        
    }
}
