#include <vector>
#include <iostream>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int slowIndex = 0;
        for (int fastIndex = 0; fastIndex < nums.size(); fastIndex++) {
            if (val != nums[fastIndex]) {
                nums[slowIndex++] = nums[fastIndex];
            }
        }
        return slowIndex;
    }
};

/*
for (初始化语句; 循环条件; 更新语句) {
    // 循环体
}

初始化一次 → 判断条件 → 执行循环体 → 执行更新 → 再次判断条件
*/

/*
nums[slowIndex++] = nums[fastIndex];

相当于：

nums[slowIndex] = nums[fastIndex];
slowIndex++;
*/

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 5, 6};
    Solution s;
    int res = s.removeElement(nums, 5);
    std::cout << "res: " << res;
    return 0;
}