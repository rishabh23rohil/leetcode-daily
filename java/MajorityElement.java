import java.util.*;

public class MajorityElement {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int n = nums.length;
        for(int i = 0 ; i < n;i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i],map.get(nums[i])+1);
            }
            else{map.put(nums[i],1);}
        }
        for(int key : map.keySet()){
            if(map.get(key)>n/2){
                return key;
            }
        }
        return -1 ;
    }
    public static void main(String[] args) {
        MajorityElement obj = new MajorityElement();
        int[] nums = {2, 2, 1, 1, 1, 2, 2};   // sample test
        int result = obj.majorityElement(nums);
        System.out.println("Majority element: " + result);
    }
}