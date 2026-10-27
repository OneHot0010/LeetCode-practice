#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};


class Solution {
public:
    void traversal(TreeNode* cur, std::vector<int>& vec) {
        if (cur == nullptr) return;
        traversal(cur->left, vec);
        traversal(cur->right, vec);
        vec.push_back(cur->val);
    }

    std::vector<int> postOrderTraversal(TreeNode* root) {
        std::vector<int> result;
        traversal(root, result);
        return result;
    }
};


int main() {
    // 1. 创建二叉树的节点
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // 2. 创建 Solution 对象
    Solution solution;

    // 3. 调用后序遍历函数
    std::vector<int> result = solution.postOrderTraversal(root);

    // 4. 输出遍历结果
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 5. 释放动态分配的内存
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}