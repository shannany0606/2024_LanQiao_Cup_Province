# 2024年第十五届蓝桥杯Python A组省赛题目+参赛代码

高位进国赛啦，happyhappyhappy!

目前知道的是G智商检测没过关哈哈，鼠鼠考场写的答案只有组合数；其它的题目似乎都不难

附一个鼠鼠脑补的大致题解：

A. 总面积开根号-1

B. 除了前200是6个，后面每个200都是4，所以2+x//200

C. 2ⁿ不行

D. 贪心，按从左到右顺序处理左半边，能两个一起就两个一起，不能就单个

E：最大子串dp+最大生成树

F：用线性筛打质数表，然后记忆化搜索(win[i]表示长度为i时先手是否能赢，如果后继状态有输的，该状态就赢；否则输）

G：离散化，然后排列组合* 行前缀积 *列前缀积

H：字典树，如果搜到相邻点不返回结果接着搜

如果感觉这个项目对您有帮助（如了解了什么库可以用or提供了题面or提供了做题思路），烦请您到右上角点个Star。祝点star的同学蓝桥杯国赛都能冲到国一哈哈。

PS：相关项目还有 

[2023年第十四届蓝桥杯全国总决赛 Python A组全国一等奖纪念（省赛国赛题目+考场代码）](https://github.com/shannany0606/2023_Lanqiao_Cup)

[2024年第十五届蓝桥杯全国总决赛 Python A组全国一等奖纪念（题目+考场代码）](https://github.com/shannany0606/2024_LanQiao_Cup_Nation)
