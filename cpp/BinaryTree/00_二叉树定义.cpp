#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 结构体可以理解成自定义的数据类型

/*
TreeNode(int x) 是构造函数。

构造函数的特点：
    - 名字与结构体名相同。
    - 没有返回值类型，连 void 也不写。
    - 创建对象时自动调用。

: val(x), left(nullptr), right(nullptr) 
    成员初始化列表，用于在构造对象时初始化成员变量。

{}
    构造函数的函数体。因为成员已经通过初始化列表完成初始化，所以这里不需要执行其他操作，函数体为空。

> 创建一个节点，接收一个整数作为节点值，并且让它的左右子节点初始为空。
*/


int main() {
    TreeNode root(10);

    std::cout << root.val << '\n';

    if (root.left == nullptr) {
        std::cout << "左子节点为空" << '\n';
    }

    return 0;
}