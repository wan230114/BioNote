# 数据的产出

## 去除接头

### cutadapter

```bash

```
参数理解：
- -e
  - ref：[cutadapter 软件使用之二_有大聚跟月月的蒋_新浪博客](http://blog.sina.com.cn/s/blog_c4e3e0620102x7x4.html)

【示例： -j是什么意思】
```bash
cutadapt -j 4 -a GATCGGAAGAGCACACGTCTGAACTCC --quality-base 33 -m 10 -O 4 --discard-untrimmed wy-KO-18d-3.R1.clean.fastq.gz> wy-KO-18d-3.R1.clean.trim.fastq
# -m 10 意思是舍弃掉低于10个碱基的reads
# --discard-untrimmed 意思是舍弃掉没有adapter的reads
```

---
- [ ] [cutadapter_百度搜索](https://www.baidu.com/s?wd=cutadapter&ie=UTF-8)


# 1. 比对软件大杂烩

## 1.1. hisat2

功能： 对齐RNA-seq的reads到参考基因组

算法： split align

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

Bowtie2用法祥解 | 陈连福的生信博客
http://www.chenlianfu.com/?p=178

## 1.3. bwa

---

> bwa samtools bowtie2大杂烩 - 简书
> https://www.jianshu.com/p/67b203cc0779

PE（paired end）
```bash
bwa mem -t 18 \
    /path/to/ref.seq.fa \
    /path/to/rawdata/RP01G9E1L3/RP01G9E1L3_R1.fq.gz \
    /path/to/rawdata/RP01G9E1L3/RP01G9E1L3_R2.fq.gz \
  |samtools view -buhS -t /path/to/ref.seq.fa.fai - \
  |samtools sort -n -o Cleandata_sample1_Rd12.vdjab.bam -
```

SE （single end）
```bash
bwa mem -t 18 \
    /path/to/ref.seq.fa \
    /path/to/rawdata/RP01G9E1L3/RP01G9E1L3_R1.fq.gz \
  |samtools view -buhS -t /path/to/ref.seq.fa.fai - \
  |samtools sort -n -o sample1_R1.vdjab.bam -
```

## 1.4. samtools

---
待吃透：
* [ ] [samtools常用命令总结 - 简书](https://www.jianshu.com/p/c48c36affff7)

---

### view

[[SAMtools] 常用指令总结 - 萧飞IDO - 博客园](https://www.cnblogs.com/xiaofeiIDO/p/6805373.html)

```bash
# 提取比对到参考基因组上的数据
samtools view -bF 4 test.bam > test.F.bam
# 提取没有比对到参考基因组上的数据
samtools view -bf 4 test.bam > test.f.bam
```

### index

```bash

```

### sort
```bash
IN=01.hisat/B4_L4_306306.sam
OUT=01.hisat/B4_L4_306306.bam
samtools sort -@ 20 -o ${OUT} ${IN} &>/dev/null
# rm 01.hisat/B4_L4_306306.sam
```


### flagstat

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
11.一对reads比对到不同染色体的且比对质量值大于5的数量。

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

### rmdup

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

### 其他自定义操作
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


## 示例

### 构建索引

构建INDEX
```bash
## input
name=Rattus_norvegicus
# file: down in data. files: data/*fa, data/*gtf

##########################################
## File preparation (cpu:24, ram:196G)
## The most recent test:
## hisat2: 166G, bowtie2: 13G, bwa: 
##########################################

workdir=`pwd`
mkdir -p hisat2_index bowtie2_index bwa_index
# 请手动执行
ls data/|sed 's/\(.\)\{3\}$//'|xargs -i echo "zcat data/{}.gz >{}"  # 解压
genome=`realpath *.fa`
gene=`realpath *.gtf`
echo ${genome} ${gene}

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
bowtie2-build ${genome} ${index} &>${workdir}/bowtie2_index/index.log

##########################################
### bwa_index
##########################################
index=${workdir}/bwa_index/${name}
cd ${workdir}/bwa_index/
bwa index -p ${index} -a bwtsw ${genome} &>${workdir}/bwa_index/index.log
# -a [is|bwtsw]   构建index的算法，有两个算法： 
# is 是默认的算法，虽然相对较快，但是需要较大的内存，当构建的数据库大于2GB的时候就不能正常工作了。
# bwtsw 对于短的参考序列式不工作的，必须要大于等于10MB, 但能用于较大的基因组数据，比如人的全基因组。
```

### 比对

```bash
cd ~/work/2020-06-08.docker_result/test_align/

workdir=`pwd`
mkdir 01.hisat2 02.bowtie2 03.bwa RNAseq -p

cd ${workdir}/RNAseq
# 网页：https://www.ncbi.nlm.nih.gov/sra/SRX8370416[accn]
# proxychain4 wget https://sra-download.ncbi.nlm.nih.gov/traces/sra46/SRR/011542/SRR11819458
# proxychain4 wget https://storage.googleapis.com/sra-pub-src-12/SRR11819458/3F_S2_L001_R1_001.fastq.gz.1 https://sra-pub-src-12.s3.amazonaws.com/SRR11819458/3F_S2_L001_R2_001.fastq.gz.1
# fastq-dump SRR11819476
# fastqc SRR11819476.fastq
# trim_galore -q 25 --phred33 --length 25 --stringency 3 -o ./cleandata SRR11819476.fastq
# fq=`realpath ./cleandata/SRR11819476_trimmed.fq` 

clean1=/home/chenjun/work/2020-05-25.RNA_test/00.QC/01.cleandata/B2_L4_304304.R1_val_1.fq.gz
clean2=/home/chenjun/work/2020-05-25.RNA_test/00.QC/01.cleandata/B2_L4_304304.R2_val_2.fq.gz

# refpath: /home/chenjun/work/2020-05-25.RNA_test/01.Mapping/test/test_1_to_bam.sh
cd ${workdir}/01.hisat2
index=/home/chenjun/work/2020-06-08.docker_result/hisat2_index/Rattus_norvegicus
# genome=/home/chenjun/work/2020-06-08.docker_result/Rattus_norvegicus.Rnor_6.0.dna.toplevel.fa
# gene=/home/chenjun/work/2020-06-08.docker_result/Rattus_norvegicus.Rnor_6.0.100.gtf
hisat2 -p 20 --dta -x $index -1 ${clean1} -2 ${clean2} |samtools view -bS >B2.bam 2>log

cd ${workdir}/02.bowtie2
index=/home/chenjun/work/2020-06-08.docker_result/bowtie2_index/Rattus_norvegicus
bowtie2 -p 4 -x ${index} -1 ${clean1} -2 ${clean2}  2>log|samtools view -bS >B2.bam

cd ${workdir}/03.bwa
index=/home/chenjun/work/2020-06-08.docker_result/bwa_index/Rattus_norvegicus
bwa mem -t 4 ${index} ${clean1} ${clean2} |samtools view -bS >B2.bam 2>log
```



# 定量

## featureCounts

```bash
gtf=/home/gzsc/genomic/Homo_sapiens/UCSC/hg38/current/current_gtf/homo_sapiens/Homo_sapiens.GRCh38.98.chr.gtf
featureCounts -T 12 -p -t exon -g gene_id  -a ${gtf} -o all.id.txt 01.hisat/*.bam  1>log.featureCounts 2>&1
```
