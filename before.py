#include <stdio.h>

// 重复代码：add 和 add2 功能完全一样
int add(int a, int b) {
    int res = a + b;
    printf("sum = %d\n", res);
    return res;
}

int add2(int a, int b) {
    int res = a + b;
    printf("sum = %d\n", res);
    return res;
}

// 未使用变量
int unused_var = 100;

// 魔法数字
int mul2(int x) {
    return x * 2;
}

int mul3(int x) {
    return x * 3;
}

int main() {
    add(1, 2);
    add2(3, 4);
    mul2(5);
    mul3(6);
    return 0;
}