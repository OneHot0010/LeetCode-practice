#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};


class Solution {
public:
    void traversal(TreeNode* cur, std::vector<int>& vec) {
        if (cur == nullptr) return;
        traversal(cur->left, vec);
        vec.push_back(cur->val);
        traversal(cur->right, vec);
    }

    std::vector<int> inOrderTraversal(TreeNode* root) {
        std::vector<int> result;
        traversal(root, result);
        return result;
    }
};