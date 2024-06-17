//Very good explanation of right shift and left shift operator in the below code.
// To update the value after left/ right shift then, we have to assign it.

class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        
        for (int i = 0; i < 32; i++)  //Because there is total 32 bits(4 Byte) in integer data type.
        {
            int sum = 0;
            
            for(int j = 0; j < nums.length; j++)
            {
                if (((nums[j] >> i) & 1) == 1)
                    sum += 1;
            }
            
            sum %= 3;
            
            if (sum != 0)
            {
                ans |= (sum << i);
            }
        }
        return ans;
    }
}