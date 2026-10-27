#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) / 2);
            if (nums[middle] > target) {
                right = middle - 1;
            } else if (nums[middle] < target) {
                left = middle + 1;
            } else {
                return middle;
            }
        }

        return -1;
    }
};

/*
std::vector<int>& nums
    - vector：C++ 标准库提供的动态数组类型，完整名称通常写作 std::vector。
    - <int>：模板参数，表示这个 vector 存储的是 int 类型的元素。
    - &：在这里表示引用。
    - nums：参数名。


> vector<int>& nums 表示参数 nums 是一个对整数动态数组的引用。
*/

class Solution1 {
public:
    int search(std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();

        while (left < right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] > target) {
                right = middle;
            } else if (nums[middle] < target) {
                left = middle + 1;
            } else {
                return middle;
            }
        }

        return -1;
    }
};


/*
">>" 是 C++ 的右移运算符。对于非负整数，右移一位相当于整除 2，效果与  / 2 相同。
与 int middle = left + (right - left) / 2; 相同。

为什么不直接写 (left + right) / 2
    当 left 和 right 都很大时，left + right 可能超过 int 能表示的最大值，造成有符号整数溢出。
    通过先计算差值，再取一半，避免了直接将两个边界相加的风险（前提是边界合法，且差值本身可以由 int 表示）。

右移一位并不意味着直接删除十进制数字的末尾一位，而是移动二进制位。
*/