# 文档解读

官方文档：
- [官方文档](https://bioconductor.org/packages/release/bioc/vignettes/DiffBind/inst/doc/DiffBind.pdf)
- [官方文档_kami](https://kami.app/ycDSW085WmNq)

详细文档：
- [DiffBind documentation](https://rdrr.io/bioc/DiffBind/man/)
- [实战演练1](https://bioinformatics-core-shared-training.github.io/cruk-summer-school-2018/ChIP/Practicals/Practical4_differentialBinding_DB.html)

网络教程：
- [第9篇：差异peaks分析——DiffBind - 简书](https://www.jianshu.com/p/f849bd55ac27)  
  主要测试文章。测试中，由于没有生物学重复，在第三步的差异分析计算失败。包含原因解释的系列文章
  - [ChIP-Seq: DiffBind无control，无重复样本 - 简书](https://www.jianshu.com/p/00ee9aa4e191)  
    总结的不错，有好几篇子文章可以吸收【尚待吸收】
  - [使用DiffBind进行peak 差异分析](http://www.360doc.com/content/20/0407/00/68068867_904472630.shtml)
- [ChIP 差异peak 脚本（DESeq2&DiffBind） - 简书](https://www.jianshu.com/p/5bda28d3d6fb)  
    【有部分脚本尚待读懂】

原理解读：
- [DiffBind 两个基本问题的解析](https://mp.weixin.qq.com/s/d3VliH3FgbJToTbnShdlrg)

---
- [ ] [搜狗微信](https://weixin.sogou.com/weixin?type=2&s_from=input&query=diffbind&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=3103&sst0=1592810715780&lkt=9%2C1592810713468%2C1592810715678)
- [ ] [DiffBind_百度搜索](https://www.baidu.com/s?wd=DiffBind&pn=10&oq=DiffBind&ie=utf-8&usm=2&rsv_pq=f7811a440018b3b6&rsv_t=7dbfjIisvORct6QPHCaM%2FPt1XNGhQBYLfyN1vmE%2F2bvSxSczJlE7sbxar0M&rsv_page=1)


# 脚本参考

## callPeak macs2参数

参数说明：
```bash
-q/--qvalue
    q值（最小FDR）截止值可调用有效区域。默认值为0.05。
    对于宽阔的分数，您可以尝试使用0.05作为截止值。
    使用Benjamini-Hochberg过程从p值计算Q值。
-p/--pvalue
    P值截止。如果-p指定，则MACS2将使用p值而不是q值。
--extsize
    而--nomodel被设置时，
    MACS使用该参数来扩展读取5“ - > 3”方向到固定大小的片段。
    例如，如果转录因子结合区的大小为200 bp，
    并且您想通过MACS绕过模型构建，则可以将此参数设置为200。
    仅当--nomodel设置了该选项或MACS不能建立模型并--fix-bimodal启动。
```

```bash
macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
# macs2 callpeak \
#     -t ${REP1_TA_FILE}.tagAlign.gz \
#     -c ${CONTROL_TA_PREFIX}.tagAlign.gz \
#     -f BED \
#     -n ${PEAK_OUTPUT_DIR}/${CHIP_TA_PREFIX} \
#     -g ${GENOMESIZE} \
#     -p 1e-2 \
#     --nomodel \
#     --shift 0 \
#     --extsize ${FRAGLEN} \
#     --keep-dup all -B --SPMR
```

## 原始callPeak结果（来自于 Chip_run 流程）

```shell
# 来自于 Chip_run流程 的callPeak结果
(python27) [chenjun@gzscbioinfo: 09:11:04 ~/work/works/chip/test/DiffBind/input_datas/diff]
$ wc -l */*Peak
   95091 YJ-A549-1-8-input_L3_P708503__vs__YJ-A549-1-8-H3K27me3_L3_P709503/YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   42982 YJ-A549-1-8-input_L3_P708503__vs__YJ-A549-1-8-H3K4me3_L3_P710503/YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   57611 YJ-A549-1-8-input_L3_P708503__vs__YJ-A549-1-8-RNA-II_L3_P711503/YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  278194 YJ-A549-3-0uM-input_L4_P707504__vs__YJ-A549-3-0uM-H3K27me3_L4_Y0000035507/YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   66418 YJ-A549-3-0uM-input_L4_P707504__vs__YJ-A549-3-0uM-H3K4me3_L4_Y0000031506/YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  106193 YJ-A549-3-0uM-input_L4_P707504__vs__YJ-A549-3-0uM-RNA-II_L2_Y0000036508/YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  206636 YJ-A549-NC-input_L2_P704503__vs__YJ-A549-NC-H3K27me3_L4_P706503/YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   49505 YJ-A549-NC-input_L2_P704503__vs__YJ-A549-NC-H3K4me3_L2_P705503/YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   27949 YJ-A549-NC-input_L2_P704503__vs__YJ-A549-NC-RNA-II_L4_P707503/YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  120629 YJ-BEAS-2B-input_L4_409209__vs__YJ-BEAS-2B-H3K27me3_L2_411211/YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  147841 YJ-BEAS-2B-input_L4_409209__vs__YJ-BEAS-2B-H3K4me3_L4_410E07/YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   90077 YJ-BEAS-2B-input_L4_409209__vs__YJ-BEAS-2B-RNA-II_BKDL190838938-1a/YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
 1289126 total
```


### 对比：
![](./img/duibi.png)

```
# 来自于 Chip_run流程 的callPeak结果
(python27) [chenjun@gzscbioinfo: 09:11:04 ~/work/works/chip/test/DiffBind/input_datas/diff]
$ wc -l */*Peak
   66418 YJ-A549-3-0uM-input_L4_P707504__vs__YJ-A549-3-0uM-H3K4me3_L4_Y0000031506/YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  106193 YJ-A549-3-0uM-input_L4_P707504__vs__YJ-A549-3-0uM-RNA-II_L2_Y0000036508/YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
  278194 YJ-A549-3-0uM-input_L4_P707504__vs__YJ-A549-3-0uM-H3K27me3_L4_Y0000035507/YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   42982 YJ-A549-1-8-input_L3_P708503__vs__YJ-A549-1-8-H3K4me3_L3_P710503/YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   95091 YJ-A549-1-8-input_L3_P708503__vs__YJ-A549-1-8-H3K27me3_L3_P709503/YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
   57611 YJ-A549-1-8-input_L3_P708503__vs__YJ-A549-1-8-RNA-II_L3_P711503/YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak
```

# 测试过程1

钱总的run: /home/gzsc/R/diffbind/R_work

```bash
workdir=/home/chenjun/work/works/chip/test/DiffBind
cd $workdir && mkdir -p input_datas/diff && cd input_datas/diff

ls -d $workdir/TestOut*/YJ-*/|xargs -i realpath {}|while read path; do
    name_base=`basename $path`;
    # echo $path $name_base;
    mkdir -p ${workdir}/input_datas/diff/${name_base} && cd ${workdir}/input_datas/diff/${name_base}
    ### /home/chenjun/work/2020-06-13.Chip_run/TestOut/YJ-BEAS-2B-input_L4_409209__vs__YJ-BEAS-2B-RNA-II_BKDL190838938-1a/chip/f91df252-4c8d-4ba8-8fbb-84f1be61b140/call-filter_ctl/shard-0/execution/glob-3bcbe4e7489c90f75e0523ac6f3a9385/YJ-BEAS-2B-input_L4_409209.R1.merged.nodup.bam
    ### /home/chenjun/work/2020-06-13.Chip_run/TestOut/YJ-BEAS-2B-input_L4_409209__vs__YJ-BEAS-2B-RNA-II_BKDL190838938-1a/chip/f91df252-4c8d-4ba8-8fbb-84f1be61b140/call-filter/shard-0/execution/glob-3bcbe4e7489c90f75e0523ac6f3a9385/YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup.bam
    ln -s $path/chip/*/call-filter_ctl/shard-0/execution/*/*.merged.nodup.bam ./
    ln -s $path/chip/*/call-filter/shard-0/execution/*/*.merged.nodup.bam ./
    ### line: /home/chenjun/work/2020-06-13.Chip_run/TestOut/YJ-BEAS-2B-input_L4_409209__vs__YJ-BEAS-2B-H3K27me3_L2_411211/chip/f84fb657-3007-44f5-9c03-5606d1d71407/call-call_peak/shard-0/execution/YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_x_ctl_for_rep1.pval0.01.500K.narrowPeak.gz
    cp $path/chip/*/call-call_peak/shard-0/execution/*500K.narrowPeak.gz ./
    filename=`ls *500K.narrowPeak.gz`
    gzip -df ${filename}
    cut -f 1-6 ${filename%.gz} >${filename%.narrowPeak.gz}.bed
done

cd $workdir && mkdir -p input_datas/datas
# cp -a -i ...
# ...
# vim SampleSheet.csv
```

## 数据拆分 split 2

步骤：
- `sample.bam` -- sort --> 
- `sample_sorted.bam`  -- split --> 
- `sample1.bam + sample2.bam` -- call peak --> 
- `peak1 + peak2`

注：sort之后同sort之前对比了一下，发现文件并没有任何改变差异，因此判断caper流程输出的文件是已经sorted之后的，无需sort，只需拆分

```bash
screen -R diffbind
workdir=/home/chenjun/work/works/chip/test/DiffBind
cd $workdir && mkdir -p input_datas/diff && cd input_datas/datas_split

source /home/chenjun/.conda_bashrc_my
conda activate bio

cp -fa ../datas/*.bam ./
ls *nodup.bam|while read inbam; do
    echo $inbam  # YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup.bam
    samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|awk 'NR%2==1') >${inbam%.bam}_1.bam &
    samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|awk 'NR%2==0') >${inbam%.bam}_2.bam &
    wait
done
```

## callPeak -p 1e-2

```bash
source /home/chenjun/.conda_bashrc_gzsc
conda activate python27

workdir=/home/chenjun/work/works/chip/test/DiffBind

mkdir -p $workdir/input_datas/datas_split_callPeak_p0.01  && cd $workdir/input_datas/datas_split_callPeak_p0.01

ls ../datas_split/*input*.nodup.bam|xargs -i basename {}|awk -F "-input" '{print $1}'|while read pre; do
    ls $workdir/input_datas/datas_split/${pre}*.nodup_*.bam|grep -v "\-input"|while read BAM; do
        target=${BAM}
        name=`basename ${BAM}`
        input=`ls $workdir/input_datas/datas_split/${pre}*-input*.nodup.bam`
        echo -e '\n---' ${pre}
        echo 'bam:' ${BAM}
        echo "ls $workdir/input_datas/datas_split/${pre}*-input*.nodup.bam"
        echo 'inp:' $input
        # macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
        macs2 callpeak \
            -t $target \
            -c $input \
            -g hs \
            -f BAMPE \
            -n $name \
            -B \
            -p 1e-2 \
            --nomodel \
            --shift 0 \
            --extsize 150 \
            --keep-dup all \
            --outdir ./ 1>log.$name.o 2>log.$name.e &
    done
done
```

### 结果：--extsize 150

```bash
macs2 callpeak \
    -t $target \
    -c $input \
    -g hs \
    -f BAMPE \
    -n $name \
    -B \
    -p 1e-2 \
    --nomodel \
    --shift 0 \
    --extsize 150 \
    --keep-dup all \
    --outdir ./ 1>log.$name.o 2>log.$name.e &
```

```
(python27) [chenjun@gzscbioinfo: 14:23:51 ~/work/works/chip/test/DiffBind/input_datas/datas_split_callPeak_p0.01]
$ wc -l *Peak
    98466 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
    98628 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
    38317 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_1.bam_peaks.narrowPeak
    38043 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_2.bam_peaks.narrowPeak
    57042 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_1.bam_peaks.narrowPeak
    56724 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_2.bam_peaks.narrowPeak
   100584 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
   100341 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
    67445 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_1.bam_peaks.narrowPeak
    67431 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_2.bam_peaks.narrowPeak
   109354 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_1.bam_peaks.narrowPeak
   109174 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_2.bam_peaks.narrowPeak
   111394 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
   111228 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
    40469 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_1.bam_peaks.narrowPeak
    40522 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_2.bam_peaks.narrowPeak
    78074 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_1.bam_peaks.narrowPeak
    77410 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_2.bam_peaks.narrowPeak
    84280 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
    83755 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
    58895 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_1.bam_peaks.narrowPeak
    59161 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_2.bam_peaks.narrowPeak
   100407 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_1.bam_peaks.narrowPeak
   100892 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam_peaks.narrowPeak
  1888036 total
```


### 结果： no extsize && no BAMPE

```bash
macs2 callpeak \
    -t $target \
    -c $input \
    -g hs \
    -n $name \
    -B \
    -p 1e-2 \
    --nomodel \
    --shift 0 \
    --keep-dup all \
    --outdir ./ 1>log.$name.o 2>log.$name.e &
```



```bash
(python27) [chenjun@gzscbioinfo: 11:08:27 ~/work/works/chip/test/DiffBind/input_datas/datas_split_callPeak2]
$ wc -l *Peak
    28302 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
    28044 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
   372574 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_1.bam_peaks.narrowPeak
   371490 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_2.bam_peaks.narrowPeak
    19776 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_1.bam_peaks.narrowPeak
    19719 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_2.bam_peaks.narrowPeak
   180755 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
   181142 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
    75801 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_1.bam_peaks.narrowPeak
    75850 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_2.bam_peaks.narrowPeak
    49335 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_1.bam_peaks.narrowPeak
    48998 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_2.bam_peaks.narrowPeak
   123010 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
   123182 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
    33722 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_1.bam_peaks.narrowPeak
    33703 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_2.bam_peaks.narrowPeak
    90824 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_1.bam_peaks.narrowPeak
    90424 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_2.bam_peaks.narrowPeak
   154961 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
   154552 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
   235856 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_1.bam_peaks.narrowPeak
   236397 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_2.bam_peaks.narrowPeak
    34769 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_1.bam_peaks.narrowPeak
    34753 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam_peaks.narrowPeak
  2797939 total
```

## callPeak -q 0.01

```bash
source /home/chenjun/.conda_bashrc_gzsc
conda activate python27

workdir=/home/chenjun/work/works/chip/test/DiffBind

mkdir -p $workdir/input_datas/datas_split_callPeak_q0.01  && cd $workdir/input_datas/datas_split_callPeak_q0.01

ls ../datas_split/*input*.nodup.bam|xargs -i basename {}|awk -F "-input" '{print $1}'|while read pre; do
    ls $workdir/input_datas/datas_split/${pre}*.nodup_*.bam|grep -v "\-input"|while read BAM; do
        target=${BAM}
        name=`basename ${BAM}`
        input=`ls $workdir/input_datas/datas_split/${pre}*-input*.nodup.bam`
        echo -e '\n---' ${pre}
        echo 'bam:' ${BAM}
        echo "ls $workdir/input_datas/datas_split/${pre}*-input*.nodup.bam"
        echo 'inp:' $input
        # macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
        # macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
        macs2 callpeak \
            -t $target \
            -c $input \
            -g hs \
            -f BAMPE \
            -n $name \
            -B \
            -q 0.01 \
            --nomodel \
            --shift 0 \
            --extsize 150 \
            --keep-dup all \
            --outdir ./ 1>log.$name.o 2>log.$name.e &
    done
done
```

### 结果：--extsize 150

```bash
macs2 callpeak \
    -t $target \
    -c $input \
    -g hs \
    -f BAMPE \
    -n $name \
    -B \
    -q 0.01 \
    --nomodel \
    --shift 0 \
    --extsize 150 \
    --keep-dup all \
    --outdir ./ 1>log.$name.o 2>log.$name.e &
```

```bash
(python27) [chenjun@gzscbioinfo: 11:03:40 ~/work/works/chip/test/DiffBind/input_datas/datas_split_callPeak_q0.01]
$ wc -l *Peak
    7648 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
    7725 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
    5442 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_1.bam_peaks.narrowPeak
    5416 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_2.bam_peaks.narrowPeak
    7021 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_1.bam_peaks.narrowPeak
    6986 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_2.bam_peaks.narrowPeak
    6695 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
    6694 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
   21242 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_1.bam_peaks.narrowPeak
   21192 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_2.bam_peaks.narrowPeak
   36146 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_1.bam_peaks.narrowPeak
   36047 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_2.bam_peaks.narrowPeak
     654 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
     659 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
   25262 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_1.bam_peaks.narrowPeak
   25146 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_2.bam_peaks.narrowPeak
     377 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_1.bam_peaks.narrowPeak
     361 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_2.bam_peaks.narrowPeak
   12031 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
   12047 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
   14725 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_1.bam_peaks.narrowPeak
   14695 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_2.bam_peaks.narrowPeak
   12424 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_1.bam_peaks.narrowPeak
   12327 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam_peaks.narrowPeak
  298962 total
```

### 结果： no extsize

参数：
```bash
macs2 callpeak \
    -t $target \
    -c $input \
    -g hs \
    -f BAMPE \
    -n $name \
    -B \
    -q 0.01 \
    --nomodel \
    --shift 0 \
    --keep-dup all \
    --outdir ./ 1>log.$name.o 2>log.$name.e &
```

```bash
(python27) [chenjun@gzscbioinfo: 10:43:24 ~/work/works/chip/test/DiffBind/input_datas/datas_split_callPeak_q0.01]
$ wc -l *Peak
    7648 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
    7725 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
    5442 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_1.bam_peaks.narrowPeak
    5416 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_2.bam_peaks.narrowPeak
    7021 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_1.bam_peaks.narrowPeak
    6986 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_2.bam_peaks.narrowPeak
    6695 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
    6694 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
   21242 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_1.bam_peaks.narrowPeak
   21192 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_2.bam_peaks.narrowPeak
   36146 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_1.bam_peaks.narrowPeak
   36047 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_2.bam_peaks.narrowPeak
     654 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
     659 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
   25262 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_1.bam_peaks.narrowPeak
   25146 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_2.bam_peaks.narrowPeak
     377 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_1.bam_peaks.narrowPeak
     361 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_2.bam_peaks.narrowPeak
   12031 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
   12047 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
   14725 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_1.bam_peaks.narrowPeak
   14695 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_2.bam_peaks.narrowPeak
   12424 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_1.bam_peaks.narrowPeak
   12327 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam_peaks.narrowPeak
  298962 total
```

### 结果： no extsize && no BAMPE

```bash
callpeak \
    -t /home/chenjun/work/works/chip/test/DiffBind/input_datas/datas_split/YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam \
    -c /home/chenjun/work/works/chip/test/DiffBind/input_datas/datas_split/YJ-BEAS-2B-input_L4_409209.R1.merged.nodup.bam \
    -g hs \
    -n YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam \
    -B \
    -q 0.01 \
    --nomodel \
    --shift 0 \
    --keep-dup all \
    --outdir ./
```

```
(python27) [chenjun@gzscbioinfo: 10:55:02 ~/work/works/chip/test/DiffBind/input_datas/datas_split_callPeak2--v1]
$ wc -l *Peak
    1870 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
    1874 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
    2880 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_1.bam_peaks.narrowPeak
    2862 YJ-A549-1-8-H3K4me3_L3_P710503.R1.merged.nodup_2.bam_peaks.narrowPeak
    5349 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_1.bam_peaks.narrowPeak
    5398 YJ-A549-1-8-RNA-II_L3_P711503.R1.merged.nodup_2.bam_peaks.narrowPeak
    2820 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
    2775 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
   24004 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_1.bam_peaks.narrowPeak
   24048 YJ-A549-3-0uM-H3K4me3_L4_Y0000031506.R1.merged.nodup_2.bam_peaks.narrowPeak
   12538 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_1.bam_peaks.narrowPeak
   12444 YJ-A549-3-0uM-RNA-II_L2_Y0000036508.R1.merged.nodup_2.bam_peaks.narrowPeak
     308 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
     263 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
   24890 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_1.bam_peaks.narrowPeak
   24949 YJ-A549-NC-H3K4me3_L2_P705503.R1.merged.nodup_2.bam_peaks.narrowPeak
     315 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_1.bam_peaks.narrowPeak
     306 YJ-A549-NC-RNA-II_L4_P707503.R1.merged.nodup_2.bam_peaks.narrowPeak
    6298 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
    6250 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
   14170 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_1.bam_peaks.narrowPeak
   14086 YJ-BEAS-2B-H3K4me3_L4_410E07.R1.merged.nodup_2.bam_peaks.narrowPeak
    7585 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_1.bam_peaks.narrowPeak
    7580 YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup_2.bam_peaks.narrowPeak
  205862 total
```

## callPeak input拆分

```bash
source /home/chenjun/.conda_bashrc_gzsc
conda activate python27

mkdir $workdir/input_datas/datas_split_f3_callPeak_s
cd $workdir/input_datas/datas_split_f3_callPeak_s
ls ../datas_split/*input*.nodup.bam|xargs -i basename {}|awk -F "-input" '{print $1}'|while read pre; do
    ls $workdir/input_datas/datas_split_f3/${pre}*.nodup_*.bam|grep -v "\-input"|while read BAM; do
        target=${BAM}
        name=`basename ${BAM}`
        num=`basename ${BAM}|sed 's#.bam$##'|awk -F "merged.nodup_" '{print $2}'`
        input=`ls $workdir/input_datas/datas_split_f3/${pre}*-input*.nodup_${num}.bam`
        echo -e '\n---' ${pre}
        echo 'bam:' ${BAM}
        echo 'inp:' $input
        # macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
        macs2 callpeak \
            -t $target \
            -c $input \
            -g hs \
            -n $name \
            -B \
            -p 1e-2 \
            --nomodel \
            --shift 0 \
            --keep-dup all \
            --outdir ./ 1>log.$name.o 2>log.$name.e &
    done
done
```

### 结果：--extsize 150

# 测试过程2

## 数据拆分 split 3

screen -R diffbind

```bash
workdir=/home/chenjun/work/works/chip/test/DiffBind
cd $workdir && mkdir -p input_datas/datas_split_f3 && cd input_datas/datas_split_f3

source /home/chenjun/.conda_bashrc_my
conda activate bio

cp -fa ../datas/*.bam ./
ls *nodup.bam|while read inbam; do
    echo $inbam  # YJ-BEAS-2B-RNA-II_BKDL190838938-1a_1.merged.nodup.bam
    samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|awk 'NR%3==2') >${inbam%.bam}_1.bam &
    samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|awk 'NR%3==1') >${inbam%.bam}_2.bam &
    samtools view -bS <(samtools view -H ${inbam}; samtools view ${inbam}|awk 'NR%3==0') >${inbam%.bam}_3.bam &
    wait
done
```

## callPeak input不拆分

```bash
source /home/chenjun/.conda_bashrc_gzsc
conda activate python27

mkdir $workdir/input_datas/datas_split_f3_callPeak
cd $workdir/input_datas/datas_split_f3_callPeak
ls ../datas_split/*input*.nodup.bam|xargs -i basename {}|awk -F "-input" '{print $1}'|while read pre; do
    ls $workdir/input_datas/datas_split_f3/${pre}*.nodup_*.bam|grep -v "\-input"|while read BAM; do
        target=${BAM}
        name=`basename ${BAM}`
        input=`ls $workdir/input_datas/datas_split/${pre}*-input*.nodup.bam`
        echo -e '\n---' ${pre}
        echo 'bam:' ${BAM}
        echo "ls $workdir/input_datas/datas_split/${pre}*-input*.nodup.bam"
        echo 'inp:' $input
        # macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
        macs2 callpeak \
            -t $target \
            -c $input \
            -g hs \
            -n $name \
            -B \
            -p 1e-2 \
            --nomodel \
            --shift 0 \
            --keep-dup all \
            --outdir ./ 1>log.$name.o 2>log.$name.e &
    done
done

```

### 结果：

```shell
(python27) [chenjun@gzscbioinfo: 09:30:23 ~/work/works/chip/test/DiffBind/input_datas/datas_split_f3_callPeak]
$ wc -l *Peak
   454795 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
   455188 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
   455339 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_3.bam_peaks.narrowPeak
   149645 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
   149899 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
   149913 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_3.bam_peaks.narrowPeak
    73859 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
    73467 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
    73508 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_3.bam_peaks.narrowPeak
    83814 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
    83700 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
    83780 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_3.bam_peaks.narrowPeak
  2286907 total
```

## callPeak input拆分

```bash
source /home/chenjun/.conda_bashrc_gzsc
conda activate python27

mkdir $workdir/input_datas/datas_split_f3_callPeak_s
cd $workdir/input_datas/datas_split_f3_callPeak_s
ls ../datas_split/*input*.nodup.bam|xargs -i basename {}|awk -F "-input" '{print $1}'|while read pre; do
    ls $workdir/input_datas/datas_split_f3/${pre}*.nodup_*.bam|grep -v "\-input"|while read BAM; do
        target=${BAM}
        name=`basename ${BAM}`
        num=`basename ${BAM}|sed 's#.bam$##'|awk -F "merged.nodup_" '{print $2}'`
        input=`ls $workdir/input_datas/datas_split_f3/${pre}*-input*.nodup_${num}.bam`
        echo -e '\n---' ${pre}
        echo 'bam:' ${BAM}
        echo 'inp:' $input
        # macs2 callpeak -t $target -c $input -g hs -f BAMPE -n $name -B -q 0.01 --nomodel --shift 0 --extsize 150  --keep-dup all --outdir $dir
        macs2 callpeak \
            -t $target \
            -c $input \
            -g hs \
            -n $name \
            -B \
            -p 1e-2 \
            --nomodel \
            --shift 0 \
            --keep-dup all \
            --outdir ./ 1>log.$name.o 2>log.$name.e &
    done
done
```

### 结果：

```bash
(python27) [chenjun@gzscbioinfo: 09:29:31 ~/work/works/chip/test/DiffBind/input_datas/datas_split_f3_callPeak_s]
$ wc -l *Peak
    9083 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_1.bam_peaks.narrowPeak
    9152 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_2.bam_peaks.narrowPeak
    9079 YJ-A549-1-8-H3K27me3_L3_P709503.R1.merged.nodup_3.bam_peaks.narrowPeak
   22530 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_1.bam_peaks.narrowPeak
   22363 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_2.bam_peaks.narrowPeak
   22530 YJ-A549-3-0uM-H3K27me3_L4_Y0000035507.R1.merged.nodup_3.bam_peaks.narrowPeak
    5510 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_1.bam_peaks.narrowPeak
    5508 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_2.bam_peaks.narrowPeak
    5583 YJ-A549-NC-H3K27me3_L4_P706503.R1.merged.nodup_3.bam_peaks.narrowPeak
   47102 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_1.bam_peaks.narrowPeak
   47379 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_2.bam_peaks.narrowPeak
   46959 YJ-BEAS-2B-H3K27me3_L2_411211.R1.merged.nodup_3.bam_peaks.narrowPeak
  252778 total
```

【?? 为什么input的数据量下降，带来的结果，不应该是callPeak数量上升吗，为何不升反降。】

