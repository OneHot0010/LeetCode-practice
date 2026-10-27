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
        if (cur == NULL) return;
        vec.push_back(cur->val);
        traversal(cur->left, vec);
        traversal(cur->right, vec);
    }

    std::vector<int> preorderTraversal(TreeNode* root) {
        std::vector<int> result;
        traversal(root, result);
        return result;
    }
};


// TreeNode* cur：cur 用来保存一个 TreeNode 节点的地址

/*
定义了一种叫 TreeNode 的结构体，用来表示二叉树中的一个节点，每个节点都有三个成员：val、left、right。

## 如何访问节点的 val
先定义一个节点：TreeNode node(10); （这里调用了构造函数，TreeNode(int x))
可以通过对象直接访问成员：node.val  // 获取 node 这个节点的 val 成员，也就是整数 10。

## cur->val：访问 cur 指向的节点的 val 成员。
TreeNode* cur;  // 代码中 cur 是指向节点的指针变量

TreeNode node(10);
TreeNode* cur = &node;
由于 cur 保存的是 node 的地址，所以想要通过 cur 获取节点的值，可以写：cur->val，其中 "->" 是通过指针访问对象成员的运算符。
等价于：(*cur).val
这里分两步理解：
1. *cur：通过指针找到它指向的节点，也就是 node。
2. (*cur).val：再通过 . 获取这个节点的 val 成员。

> cur是一个指针类型的变量，cur->val是通过该类型的变量获取它所指向的那个对象的成员
*/

/*
std::vector<int>& vec

表示：定义一个名为 vec 的引用参数，它引用一个存放 int 类型元素的 vector 对象。


int a = 10;
int& b = a;
让 b 引用变量 a。b 和 a 是同一个变量的两种访问方式

> 引用不是创建一个新的整数，而是给已有变量提供另一个名字


int a = 10;
int& b = a;
b = 20;
std::cout << a;  // 输出 20
b 引用的就是 a。通过 b 修改值，本质上就是修改 a。

> 注意，C++ 中引用必须在定义时初始化，例如 int& b = a;


std::vector<int>& vec;
std::vector<int> nums = {1, 2, 3};
std::vector<int>& vec = nums;
vec 就是 nums 的引用。

vec.push_back(4);
std::cout << nums;  // 输出 [1, 2, 3, 4]
*/


int main() {
    // 创建三个节点
    TreeNode root(1);
    TreeNode left(2);
    TreeNode right(3);

    // 将节点连接起来
    root.left = &left;
    root.right = &right;

    // 调用函数
    Solution s;
    std::vector<int> result = s.preorderTraversal(&root);

    // 输出结果
    for (int x : result) {
        std::cout << x << " ";
    }

    return 0;
}


/*
标准 C++ 中，程序入口函数 main 的返回类型必须是 int，不能写成 std::vector<int> main()。

这里的 int 表示 main() 返回一个整数给操作系统，通常用来表示程序的执行状态：
    - return 0;：通常表示程序正常结束。
    - 非零返回值：通常表示程序以某种错误或特殊状态结束。
*/