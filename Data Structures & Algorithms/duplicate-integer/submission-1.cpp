class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int current;

        for (int i = 0; i < nums.size();)
        {
            for (int j = i + 1; j < nums.size();)
            {
                current = nums[i];
                if (current == nums[j])
                {
                    return true;
                }
                j++;
            }
            i++;
        }

        return false;
    }
};
