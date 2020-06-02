# test_1_to_bam.sh

test_1_to_bam.sh:
```bash
echo `date +"%F %H:%M:%S"` hisat2 start
hisat2 -p 8 --dta -x /home/gzsc/genomic/Homo_sapiens/UCSC/hg38/current/current_index/hisat2/Homo_sapiens -1 cleandata/B2_L4_304304.R1_val_1.fq.gz -2 cleandata/B2_L4_304304.R2_val_2.fq.gz |samtools view -bS >B2.bam
echo `date +"%F %H:%M:%S"` hisat2 end

echo `date +"%F %H:%M:%S"` sort start
samtools sort B2.bam -o B2.sorted.bam
echo `date +"%F %H:%M:%S"` sort end
```

## 测试运行
```bash
sh test_1_to_bam.sh
```

消耗资源：
- hisat2 稳定在 9CPU,8G
- sort 稳定在 1CPU,1G

耗时：
- 10min + 6min

磁盘IO及占用情况
```bash
$l
total 6.4G
-rw-r--r-- 1 chenjun gzscbio 4.4G Jun  1 10:43 B2.bam
-rw-r--r-- 1 chenjun gzscbio 2.0G Jun  1 10:55 B2.sorted.bam
lrwxrwxrwx 1 chenjun gzscbio   13 Jun  1 10:33 cleandata -> ../cleandata/
-rw-r--r-- 1 chenjun gzscbio 1.6K Jun  1 11:06 Result.md
-rw-r--r-- 1 chenjun gzscbio  866 Jun  1 11:04 test_1_to_bam.sh
-rw-r--r-- 1 chenjun gzscbio  855 Jun  1 11:03 test_2_to_sam.sh
```

运行日志：
```
2020-06-01 10:33:26 hisat2 start
23234446 reads; of these:                                                                               23234446 (100.00%) were paired; of these:                                                               1447034 (6.23%) aligned concordantly 0 times                                                          21040116 (90.56%) aligned concordantly exactly 1 time             
    747296 (3.22%) aligned concordantly >1 times
    ----
    1447034 pairs aligned concordantly 0 times; of these:
      262998 (18.17%) aligned discordantly 1 time
    ----
    1184036 pairs aligned 0 times concordantly or discordantly; of these:
      2368072 mates make up the pairs; of these:
        1194797 (50.45%) aligned 0 times
        1056647 (44.62%) aligned exactly 1 time
        116628 (4.93%) aligned >1 times
97.43% overall alignment rate
2020-06-01 10:43:49 hisat2 end

2020-06-01 10:49:31 sort start
[bam_sort_core] merging from 24 files and 1 in-memory blocks...
2020-06-01 10:55:47 sort end
```

# test_2_to_sam.sh
暂不做测试
