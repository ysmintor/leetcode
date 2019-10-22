设定候选人 celeb 为0，原理是先遍历一遍，对于遍历到的人i，若候选人 celeb 认识i，则将候选人 celeb 设为i，完成一遍遍历后，我们来检测候选人 celeb 是否真正是名人，我们如果判断不是名人，则返回 -1，如果并没有冲突，返回 celeb

参考链接:

* https://www.cnblogs.com/grandyang/p/5310649.html
* https://www.jiuzhang.com/solution/find-the-celebrity/#tag-highlight-lang-python