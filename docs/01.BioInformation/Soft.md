
# 1. 比对软件大杂烩

## 1.1. hisat2

功能： 对齐RNA-seq的reads到参考基因组

算法： split align

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

## 1.2. bowtie2

## 1.3. bwa
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


## 1.4. samtools

## 构建索引示例

### 使用

构建INDEX
```bash
## input
name=Rattus_norvegicus
# file: down in data. files: data/*fa, data/*gtf

##########################################
## File preparation (cpu:24, ram:196G)
##########################################

workdir=`pwd`
mkdir -p hisat2_index bowtie2_index bwa_index
ls *.gz|sed 's/\(.\)\{3\}$//'|xargs -i echo "zcat data/{}.gz >{}"|sh  # 解压
genome=`ls *.fa`
gene=`ls *.gtf`

##########################################
### hisat2_index
##########################################
index=${workdir}/hisat2_index/${name}

cd ${workdir}/hisat2_index/
hisat2_extract_exons.py ${gene} >${index}'.exon'
hisat2_extract_splice_sites.py ${gene} >${index}'.ss'
hisat2-build -p 30 --ss ${index}'.ss' --exon ${index}'.exon' ${genome} ${index} 1>${workdir}/hisat2_index/index.log 2>&1
# hisat2-build -p 30 $genome $index/hisat2/$name 1>$index/hisat2/index.log 2>&1

##########################################
### bowtie2_index
##########################################
index=${workdir}/bowtie2_index/${name}
cd ${workdir}/bowtie2_index/
bowtie2-build ${gene} ${index}

##########################################
### bwa_index
##########################################
index=${workdir}/bwa_index/${name}
cd ${workdir}/bwa_index/
bwa index -p ${index} -a bwtsw ${gene}
# -a [is|bwtsw]   构建index的算法，有两个算法： 
# is 是默认的算法，虽然相对较快，但是需要较大的内存，当构建的数据库大于2GB的时候就不能正常工作了。
# bwtsw 对于短的参考序列式不工作的，必须要大于等于10MB, 但能用于较大的基因组数据，比如人的全基因组。
```
