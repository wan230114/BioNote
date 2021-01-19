
# bedtools 使用技巧

```bash
$ cat a.bed 
chr1    1       20
$ cat b.bed 
chr1    10      30

$ bedtools intersect -a a.bed -b b.bed
chr1    10      20

$ bedtools intersect -a a.bed -b b.bed -wa
chr1    1       20

$ bedtools intersect -a a.bed -b b.bed -wb
chr1    10      20      chr1    10      30

$ bedtools intersect -a a.bed -b b.bed -wa -wb
chr1    1       20      chr1    10      30
```


