这个题目其实就是考察分治，更确切地讲是变治思想的应用，再结合递归来处理，将大的问题变化为规模更小的问题。在这个过程中难点就是 如何能够继续保持正确解。

我想依据题目就是长串中某个字母x的出现次数不达标，那么在子串中也不会达标，可以理解为反单调性，在 Apriori 算法中进行剪枝的理论。

所以从两头分别进行判断
1. 先对串中各个元素出现次数进行统计
2. 两边向中间判断，如果某个元素出现次数不达标则向中间移动，直到左右达标
3. 在两头都达标的子串中找到一个不达标的元素分裂，用两个子串最较长达标的值返回


主要参考以下力扣题解：

* [Java递归](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/javadi-gui-by-tzfun/)
* [python四行搞定，分治递归，通俗易懂](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/pythonsi-xing-gao-ding-di-gui-xie-fa-by-godcat/)