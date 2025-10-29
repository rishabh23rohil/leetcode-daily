class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        for(int i = 0; i<mat.length;i++){
            //pd
            sum +=mat[i][i];
            //sd
            if(i!=mat.length-1-i){
                sum +=mat[i][mat.length-1-i];
            }
        }
        return sum;  
    }
}
