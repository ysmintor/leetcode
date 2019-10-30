O(1) 数学推理：

设某个数字的字符串表示为'abc'，则这个数字代表`a*100 + b*10 + c`，转换后成为`a + b + c`，可见每次转换相当于把原数字减去`a*99 + b*9 = 9 * (a*11 + b)`，可以推出只要高于个位的位置上有数字，算法就会减去一个小于原数字的9的倍数，这就相当于数字 % 9。但9 % 9 = 0，而 9 本身就没有十位，因此需要考虑原数字是 0 或 9 的倍数的特殊情况
首先计算num % 9，若结果为 0 则考虑num本身是否为 0，若不为 0 返回 9

为什么说就相当于这个数字%9呢？我其实还是有一些不太理解的。似乎还缺少严格的数学推导。


参考链接：

https://leetcode-cn.com/problems/add-digits/solution/python-1xing-jin-jie-3xing-xun-huan-by-qqqun902025/

https://en.wikipedia.org/wiki/Digital_root
