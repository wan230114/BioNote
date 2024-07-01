
# bedtools 使用技巧

```bash
# A.bed
# (2, 5]
#       (6, 8]
#                 (14,       20]
#                    (15,             25]
#                           (20,               30]
#                                                           (40,     50]
# B.bed
# (2, 5]
#  (3,5]
#              (12,          20]
#                       (18,          25]
{
echo  "
chr10 2 5 a_range_1
chr10 6 8 a_range_2
chr10 14 20 a_range_3
chr10 15 25 a_range_4
chr10 20 30 a_range_5
chr10 40 50 a_range_6
"| awk NF |tr " " "\t" > A.bed
echo  "
chr10 2 5 b_range_1
chr10 3 5 b_range_2
chr10 12 20 b_range_3
chr10 18 25 b_range_4
"| awk NF |tr " " "\t" > B.bed
}
cat A.bed
cat B.bed


# 交集 a & b
bedtools intersect -a A.bed -b B.bed           # 输出交集计算后的区域 【PS：可以后面直接接管道合并重叠区域 ` | bedtools merge ` 】
bedtools intersect -a B.bed -b A.bed
bedtools intersect -a A.bed -b B.bed | bedtools sort | bedtools merge
bedtools intersect -a B.bed -b A.bed | bedtools sort | bedtools merge
bedtools intersect -a A.bed -b B.bed -wa       # 输出存在交集的A区域
bedtools intersect -a A.bed -b B.bed -wb       # 输出交集计算后的区域, 输出存在交集的B区域
bedtools intersect -a A.bed -b B.bed -wa -wb   # 输出存在交集的A区域, 输出存在交集的B区域
bedtools intersect -a A.bed -b B.bed -wa -f 1
bedtools intersect -a A.bed -b B.bed -f 1

intersectBed -nonamecheck -wo -a A.bed -b B.bed  # 等同于 -wa -wb ，并且输出交集的长度信息

bedtools intersect -a A.bed -b B.bed -c        # 输出所有的A区域, 统计A区域与B的交集数量
bedtools intersect -a A.bed -b B.bed -c | awk 'BEGIN{N=0}{if($NF>0)N+=1}END{print N/NR," (",N,"/",NR,")"}'   # 计算A区域中，有多大的比例与B存在交集
bedtools intersect -a B.bed -b A.bed -c | awk 'BEGIN{N=0}{if($NF>0)N+=1}END{print N/NR," (",N,"/",NR,")"}'   # 计算A区域中，有多大的比例与B存在交集

# 窗口交集， demo: A拓展10bp与B交集
# 其他写法，不过这个可以先对A上下游拓展再交集
bedtools window -a A.bed -b B.bed -l 0 -r 0  # 等同于 bedtools intersect -a A.bed -b B.bed -wa -wb
bedtools window -a A.bed -b B.bed -l 0 -r 0 -c
bedtools window -a A.bed -b B.bed -l 1 -r 0  # 减1后 (19, 30] 与 (12, 20] 刚好相交



# 并集 a + b, 并进行区域合并
cat A.bed  B.bed | bedtools sort | bedtools merge  # 并集 a + b, 并进行区域合并


# 补集, 已知基因组长度，计算已知区域的补集
bedtools complement -i A.bed -g <(echo -e "chr10\t100")


# 相减 a - b
bedtools subtract -a A.bed -b B.bed     # A区域减去B
bedtools subtract -a A.bed -b B.bed -A  # A区域减去B，并去除有交集的区域，只输出完全无交集的A区域
# -f (0,1]  : 作为a的一小部分所需的最小重叠。默认值是1E-9
# -F (0,1]  : 作为b的一小部分所需的最小重叠。默认值是1E-9
# 最小重叠的含义便是，至少重叠区域大于该比例的区域才会被减去。
bedtools subtract -a A.bed -b B.bed -A
bedtools subtract -a A.bed -b B.bed -A -f 1     # (20-15)/(25-15) <  1    因此 (15, 25] 不满足去除
bedtools subtract -a A.bed -b B.bed -A -f 0.6   # (20-15)/(25-15) <  0.6  因此 (15, 25] 不满足去除
bedtools subtract -a A.bed -b B.bed -A -f 0.5   # (20-15)/(25-15) >= 0.5  因此 (15, 25] 满足去除
bedtools subtract -a A.bed -b B.bed -A -f 0.49  # (20-15)/(25-15) >= 0.49 因此 (15, 25] 满足去除

# Demo:
# 从A中 剔除 A 与 B 完全相同区域的部分
bedtools subtract -a A.bed -b B.bed -A -f 1 -F 1
# 从A中 剔除 A(-0 +5] 与 B 有交集的部分,  - 代表从标准输出读入
bedtools window -a A.bed -b B.bed -l 0 -r 0  # 对比
bedtools window -a A.bed -b B.bed -l 0 -r 5
bedtools window -a A.bed -b B.bed -l 0 -r 5 | bedtools subtract -a A.bed -b - -A -f 1 -F 1
```


```bash
## bedtools 联合使用案例
head *.bed
bedtools intersect -a A.bed  -b  B.bed  -wa -wb | bedtools groupby -i - -g 1-4 -c 8 -o collapse 
bedtools intersect -a B.bed  -b  A.bed  -wa -wb | bedtools groupby -i - -g 1-4 -c 8 -o collapse

```

---
## 计算指定bed上下游100bp和另一个bed的交集

```bash
echo -e "chr1\t1000\t2000" >A.bed
echo -e "chr1\t500\t800\nchr1\t10000\t20000" >B.bed

cat A.bed
# chr1  1000  2000
cat B.bed
# chr1  500   800
# chr1  10000 20000

bedtools window -a A.bed -b B.bed -l 200 -r 20000
# chr1  1000   2000  chr1  10000  20000
bedtools window -a A.bed -b B.bed -l 300 -r 20000
# chr1  1000   2000  chr1  500    800
# chr1  1000   2000  chr1  10000  20000

# 临界值探索 l: 1000-200=800; r: 2000+8000=100000
# 刚好无交集：
# (500, 800] (800, 100000] (10000, 20000]
bedtools window -a A.bed -b B.bed -l 200 -r 8000
# 无
bedtools window -a A.bed -b B.bed -l 201 -r 8000
# chr1    1000    2000    chr1    500     800
bedtools window -a A.bed -b B.bed -l 200 -r 8001
# chr1    1000    2000    chr1    10000   20000
bedtools window -a A.bed -b B.bed -l 201 -r 8001
# chr1    1000    2000    chr1    500     800
# chr1    1000    2000    chr1    10000   20000


```


# 附

其他类似工具：
- [BEDOPS: the fast, highly scalable and easily-parallelizable genome analysis toolkit — BEDOPS v2.4.40](https://bedops.readthedocs.io/en/latest/index.html)

