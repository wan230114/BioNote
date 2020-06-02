
# 比对软件大杂烩

## hisat2

功能： 对齐RNA-seq的reads到参考基因组

算法： sp

命令：
```bash

```
命令解析：
> 
示例(与samtools联用)：
```bash
hisat2 -p 8 --dta \
    -x /home/gzsc/genomic/Homo_sapiens/UCSC/hg38/current/current_index/hisat2/Homo_sapiens \
    -1 cleandata/B2_L4_304304.R1_val_1.fq.gz \
    -2 cleandata/B2_L4_304304.R2_val_2.fq.gz \
    |samtools view -bS >B2.bam
```

安装：
略

## bowtie2

## bwa
BWA的安装
```bash
# 1.下载BWA
wget http://sourceforge.net/projects/bio-bwa/files/bwa-0.7.10.tar.bz2/download
# 2.解压
tar jxvf bwa-0.7.10.tar.bz2
# 3.编译
cd bwa-0.7.10
make
```
Samtool安裝


科学网—高通量测序数据的比对小结----bwa、bowtie、bowtie2、samtools - 张志斌的博文
http://blog.sciencenet.cn/blog-1339458-815241.html


## samtools

