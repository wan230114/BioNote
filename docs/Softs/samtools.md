
# 1. 基本笔记
## 1.1. samtools

[Explain SAM Flags](https://broadinstitute.github.io/picard/explain-flags.html)

---
待吃透：
* [ ] [samtools常用命令总结 - 简书](https://www.jianshu.com/p/c48c36affff7)

---

### 1.1.1. view

[[SAMtools] 常用指令总结 - 萧飞IDO - 博客园](https://www.cnblogs.com/xiaofeiIDO/p/6805373.html)

```bash
# 提取比对到参考基因组上的数据
samtools view -bF 4 test.bam > test.F.bam
# 提取没有比对到参考基因组上的数据
samtools view -bf 4 test.bam > test.f.bam
```

### 1.1.2. index

```bash
# samtools index 对未索引的文件索引
ls *bam|while read x; do if [ -e "$x.bai" ]; then echo \# $x.bai ok;else echo samtools index $x;fi;  done
```

### 1.1.3. sort
```bash
IN=01.hisat/B4_L4_306306.sam
OUT=01.hisat/B4_L4_306306.bam
samtools sort -@ 20 -o ${OUT} ${IN} &>/dev/null
# rm 01.hisat/B4_L4_306306.sam
```

---

测试hisat2与samtools sort联用

```bash
source /home/chenjun/.conda_bashrc_gzsc; conda activate python27

date "+start: %F %T"
hisat2 -p 8 --dta -x /home/gzsc/genomic/Homo_sapiens/UCSC/hg38/current/current_index/hisat2/Homo_sapiens -1 ./test.R1.fastq.gz -2 ./test.R2.fastq.gz \
  |samtools view -bS >B2.bam
samtools sort -o B2.sorted.bam B2.bam
date "+end: %F %T"

date "+start: %F %T"
hisat2 -p 8 --dta -x /home/gzsc/genomic/Homo_sapiens/UCSC/hg38/current/current_index/hisat2/Homo_sapiens -1 ./test.R1.fastq.gz -2 ./test.R2.fastq.gz \
  |samtools sort -o B2_2.sorted.bam
date "+end: %F %T"
```

### 1.1.4. flagstat

samtools flagstat命令简介：

统计输入文件的相关数据并将这些数据输出至屏幕显示。每一项统计数据都由两部分组成，分别是QC pass和QC failed，表示通过QC的reads数据量和未通过QC的reads数量。以“PASS + FAILED”格式显示。还可以根据samtools的标志位显示相应的内容，但是这里不做讨论。

命令格式：

```bash
samtools flagstat <in.bam> |<in.sam> | <in.cram>
```

运行flagstat命令得到的结果如下图所示。

```
115129715 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
3903 + 0 supplementary
0 + 0 duplicates
535869 + 0 mapped (0.47% : N/A)
115125812 + 0 paired in sequencing
57562906 + 0 read1
57562906 + 0 read2
513698 + 0 properly paired (0.45% : N/A)
514954 + 0 with itself and mate mapped
17012 + 0 singletons (0.01% : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
```

从第一行至第十一行分别表示：
1. QC pass的reads的数量为2499917，未通过QC的reads数量为0，意味着一共有2499971条reads；
2. 重复reads的数量，QC pass和failed
3. 比对到参考基因组上的reads数量；
4. paired reads数据数量；
5. read1的数量；
6. read2 的数量；
7. 正确地匹配到参考序列的reads数量；
8. 一对reads都比对到了参考序列上的数量，但是并不一定比对到同一条染色体上；
9. 一对reads中只有一条与参考序列相匹配的数量；
10. 一对reads比对到不同染色体的数量；
11. 一对reads比对到不同染色体的且比对质量值大于5的数量。

版权声明：本文为CSDN博主「BlueWing2000」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u013553061/article/details/53402232

---
refs:  
- [科学网—高通量测序数据的比对小结----bwa、bowtie、bowtie2、samtools - 张志斌的博文](http://blog.sciencenet.cn/blog-1339458-815241.html)


示例：
```bash
cd $workdir && mkdir -p 04.mapping_bwa  && cd 04.mapping_bwa
ls ../01.cleandata/*.gz|awk '{if(NR%2==1){printf $0"\t"}else{print $0}}'|while read x; do

    read R1 R2 <<< $x
    name=`basename $R1|cut -f 1 -d "_"`
    date "+%F %H:%M:%S ${name}"

    # 1) 和病毒比对，mapping，过滤出unmapping
    bwa mem -t 10 ${bwa_index} ${R1} ${R2} 2>log.bwa.${name}|samtools view -bS >${name}.bam
    samtools flagstat ${name}.bam >${name}.bam.stat &
    samtools view -bf 4 ${name}.bam >${name}_unmap.bam &

    # 2) 进行sort，并把它分为两个fq
    read R1 R2 <<< "`realpath ${name}_unmap_1.fq.gz`  `realpath ${name}_unmap_2.fq.gz`"
    # 不sort
    # samtools fastq ${name}_unmap.bam -1 $R1 -2 $R2 -c 6 &>log.bam2fq.${name} &
    samtools sort -@ 10 -n -o ${name}_unmap.sortname.bam ${name}_unmap.bam
    samtools fastq ${name}_unmap.sortname.bam -1 $R1 -2 $R2 -c 6 &>log.bam2fq_2.${name} &

    # 3) 使用猴子作为参考进行比对
    mkdir -p hisat2_unmap_sorted && cd hisat2_unmap_sorted
    index=$hisat2_index_hou
    hisat2 -p 10 --dta  -x $index  -1 $R1  -2 $R2 2>log.hisat2.${name}| samtools view -bS >${name}.bam
    samtools sort ${name}.bam -@ 10 -o ${name}.sorted.bam
    samtools flagstat ${name}.sorted.bam >${name}.sorted.bam.stat &
    cd -

done
```

### 1.1.5. rmdup

去重其他方法：
1. Picard Markduplicates
2. sambamba markdup
```bash
sambamba markdup -t 10 \
    --overflow-list-size 600000 \
    --tmpdir='./'  \
    -r ${name}.raw.bam  \
    ${name}.rmdup.bam
```

### 1.1.6. 其他自定义操作
bam文件的拆分：  
（注：一定要加头文件）

```bash
inbam=test.bam
samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|sed '1~2p') >${inbam%.bam}_1.bam
samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|sed '2~2p') >${inbam%.bam}_2.bam

# 一次IO的高效写法【已测试，效率还不如读两次】
ls *nodup.bam|while read inbam; do
    echo $inbam  # YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup.bam
    >${inbam%.bam}_1.bam;  # clean
    >${inbam%.bam}_2.bam;  # clean
    p=1;
    samtools view ${inbam}|while read line;
    do
        ((x=$x*-1));
        if [ $x -eq 1 ];
            then echo $line >>${inbam%.bam}_1.bam;
            else echo $line >>${inbam%.bam}_2.bam;
        fi;
    done
done
```

# 2. Demo
## 2.1. 截取、深度、统计

```bash
samtools view -h recall.bam chr1:1116029-1116298 > get.sam  # 获取指定位置reads
samtools view -bS get.sam | samtools sort - -o get.bam   # sam--->bam，排序
samtools index get.sam   #  建索引

# 深度统计
samtools depth -r chr1:1116029-1116298 -d 10000000 -a recall.bam > results.cov
# https://blog.csdn.net/dujidan/article/details/115675021
```


# 高级用法
## 修改Header

shell中简单修改：
```bash
samtools view -H $BAM | sed "s/Solid5500XL/Solid/" | samtools reheader - $BAM

```


---
# bam解密

## paired in sequencing

通过观察，第一对reads中，存在 `AAAGATGTACAAATGGCCAGCAGGTACATGAAAAAATGCTCAACATCACTAATCATCAGAGAAACGCAAATAAAAAACTGCAATGAG` 重复序列，第二对reads中存在 `GTGAGCGGAGAGCGCACCATTGCACTCCAGCCTGGGTGACAGAGCAAGACTCCACCTTAAAAAATAAATAAATAAAAGTTGGCCGGGCGCGGTGTCTCACACCTGTAA` 这样的重合序列。  

由此可见双端比对的特性：
- 163的末尾正好与83的开始重叠。

```txt
A00159:849:H73WVDSX2:2:1263:27606:7185  163     chr1    590062  30      150M    =       590125  213     AAACAATAGCAAACAATTAATCGAATTTTAAAATGGGCAAGAGACCTGAGTAGACATTTCTCAAAAGATGTACAAATGGCCAGCAGGTACATGAAAAAATGCTCAACATCACTAATCATCAGAGAAACGCAAATAAAAAACTGCAATGAG  FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
A00159:849:H73WVDSX2:2:1263:27606:7185  83      chr1    590125  30      150M    =       590062  -213    AAAGATGTACAAATGGCCAGCAGGTACATGAAAAAATGCTCAACATCACTAATCATCAGAGAAACGCAAATAAAAAACTGCAATGAGGTCTTCTCTCACCTCAGTTAAAATGGCTTTCGTCAAAAACGCAGGGAATAAGGGATGCTGGCG  FFFFFFFFFFFFFFFFFFFFFFF,FFFFF:FFFFFFFFFFFFFFFFFF
A00159:849:H73WVDSX2:2:2653:25328:6057  163     chr1    590556  31      150M    =       590598  192     TGAGGCAGGAGAATCACTGGAACACAGGAGGTGGAGATTGCGGTGAGCGGAGAGCGCACCATTGCACTCCAGCCTGGGTGACAGAGCAAGACTCCACCTTAAAAAATAAATAAATAAAAGTTGGCCGGGCGCGGTGTCTCACACCTGTAA  FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
A00159:849:H73WVDSX2:2:2653:25328:6057  83      chr1    590598  31      150M    =       590556  -192    GTGAGCGGAGAGCGCACCATTGCACTCCAGCCTGGGTGACAGAGCAAGACTCCACCTTAAAAAATAAATAAATAAAAGTTGGCCGGGCGCGGTGTCTCACACCTGTAATCCCAGCACTTTGGGAGGTGGAGGCGGGCGGATCACAAGGTC  FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```


他们在reads中的表现形式分别为：
- R1的序列与bam中互为反向互补序列，第二列为83。
- R2的序列与bam中一样，第二列为163。

阅读 https://www.samformat.info/sam-format-flag 取83我惊讶发现竟然是

```bash
$ ls UV-beads_R[12].fastq.gz | while read x; do echo $x; zcat $x | grep "A00159:849:H73WVDSX2:2:1263:27606:7185" -A 3; done
UV-beads_R1.fastq.gz
@A00159:849:H73WVDSX2:2:1263:27606:7185 1:N:0:GTTCGAGA+AGGCCAAT
CGCCAGCATCCCTTATTCCCTGCGTTTTTGACGAAAGCCATTTTAACTGAGGTGAGAGAAGACCTCATTGCAGTTTTTTATTTGCGTTTCTCTGATGATTAGTGATGTTGAGCATTTTTTCATGTACCTGCTGGCCATTTGTACATCTTT
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFF,FFFFFFFFFFFFFFFFFFFFFFF
UV-beads_R2.fastq.gz
@A00159:849:H73WVDSX2:2:1263:27606:7185 2:N:0:GTTCGAGA+AGGCCAAT
AAACAATAGCAAACAATTAATCGAATTTTAAAATGGGCAAGAGACCTGAGTAGACATTTCTCAAAAGATGTACAAATGGCCAGCAGGTACATGAAAAAATGCTCAACATCACTAATCATCAGAGAAACGCAAATAAAAAACTGCAATGAG
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

$ ls UV-beads_R[12].fastq.gz | while read x; do echo $x; zcat $x | grep "A00159:849:H73WVDSX2:2:2653:25328:6057" -A 3; done
UV-beads_R1.fastq.gz
@A00159:849:H73WVDSX2:2:2653:25328:6057 1:N:0:GTTCGAGA+AGGCCAAT
GACCTTGTGATCCGCCCGCCTCCACCTCCCAAAGTGCTGGGATTACAGGTGTGAGACACCGCGCCCGGCCAACTTTTATTTATTTATTTTTTAAGGTGGAGTCTTGCTCTGTCACCCAGGCTGGAGTGCAATGGTGCGCTCTCCGCTCAC
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
UV-beads_R2.fastq.gz
@A00159:849:H73WVDSX2:2:2653:25328:6057 2:N:0:GTTCGAGA+AGGCCAAT
TGAGGCAGGAGAATCACTGGAACACAGGAGGTGGAGATTGCGGTGAGCGGAGAGCGCACCATTGCACTCCAGCCTGGGTGACAGAGCAAGACTCCACCTTAAAAAATAAATAAATAAAAGTTGGCCGGGCGCGGTGTCTCACACCTGTAA
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

总结：

```txt
3` --> 5`  R1，比对 83， 负链
5` --> 3`  R2，比对163， 正链
```

其他参考资料： [链特异性建库如何区分正负链？ - 简书](https://www.jianshu.com/p/56aa023decd1)
