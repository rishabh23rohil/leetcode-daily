import java.util.*;
class TrappedRainWater {
    public int trap(int[] height) {
        int n = height.length;
        if (n <= 2) return 0;
        //leftmaxbound
        int leftMax[] = new int[n];

        leftMax[0] = height[0];
        for(int i=1;i<n;i++){
            leftMax[i]=Math.max(height[i],leftMax[i-1]);
        }
        //rightmaxbound
        int RightMax[] = new int[n];

        RightMax[n-1] = height[n-1];
        for(int i=n-2;i>=0;i--){
            RightMax[i]=Math.max(height[i],RightMax[i+1]);
        }
        int trappedwater = 0;
        //waterlevel
        for(int i = 0; i<n;i++){
            int waterlevel = Math.min(leftMax[i],RightMax[i]);
                    //trappedwater
            trappedwater += waterlevel - height[i];
        }
        return trappedwater;
    }
}