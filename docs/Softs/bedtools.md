
# bedtools 使用技巧

intersect

```bash
echo  chr1    1       20 | tr " " "\t" > a.bed 
echo  chr1    10      30 | tr " " "\t" > a.bed 
bedtools intersect -a a.bed -b b.bed
# chr1    10      20
bedtools intersect -a a.bed -b b.bed -wa
# chr1    1       20
bedtools intersect -a a.bed -b b.bed -wb
# chr1    10      20      chr1    10      30
bedtools intersect -a a.bed -b b.bed -wa -wb
# chr1    1       20      chr1    10      30
cat a.bed b.bed | bedtools sort | bedtools merge
```

merge

```bash

{
echo  "
chr10 10 20
chr10 1 20
chr2 1 20
"|tr " " "\t" > a.bed
echo  "
chr2 10 30
chr10 10 30
"|tr " " "\t" > b.bed
}

```


统计b1,b2重叠区域数量, 比例
```bash

```