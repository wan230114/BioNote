# RNA-seq基础知识

## 测序深度和测序覆盖度

[RNA-seq基础知识 - 简书](https://www.jianshu.com/p/cab06582ce61)

对长100bp的目标区域进行测序：采用单端测序，每个read长5bp；总共得到了200个reads；把所有的reads比对到目标区域后，100bp的目标区域中有98bp的位置至少有1个read覆盖到，换言之，剩余的2bp没有1个read覆盖。

深度：200 x 5 / 100 = 10                  我们说这此测序的深度为10X。

覆盖度：98 / 100 × 100% = 98%      我们说这次测序的覆盖度为98%

测序深度越高，基因覆盖度越高。一般人的测序深度到10x，基因覆盖度就100%了，测序深度就饱和了，测序深度再升高没有什么效果了。

---
那么，如何检测测序数据中的深度及覆盖度呢？
见 []()