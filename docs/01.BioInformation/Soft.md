
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


## 1.4. samtools

```bash
IN=01.hisat/B4_L4_306306.sam
OUT=01.hisat/B4_L4_306306.bam
samtools sort -@ 20 -o ${OUT} ${IN} &>/dev/null
# rm 01.hisat/B4_L4_306306.sam
```

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

---
refs:  
- [科学网—高通量测序数据的比对小结----bwa、bowtie、bowtie2、samtools - 张志斌的博文](http://blog.sciencenet.cn/blog-1339458-815241.html)


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
bowtie2 -p 4 -x ${index} -1 ${clean1} -2 ${clean2} |samtools view -bS >B2.bam 2>log

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
