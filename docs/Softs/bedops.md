
# bedops

<https://bedops.readthedocs.io/en/latest/content/reference/set-operations/bedops.html#intersect-i-intersect>

```bash
# conda install -c bioconda bedops

# A.bed
# (2, 5]
#       (6, 8]
# B.bed
# (2, 5]
#  (3,5]
#              (12,          20]
# C.bed
#               (13,         20]

{
echo  "
chr10 2 5 a_range_1
chr10 6 8 a_range_2
"| awk NF |tr " " "\t" > A.bed
echo  "
chr10 2 5 b_range_1
chr10 3 5 b_range_2
chr10 12 20 b_range_3
"| awk NF |tr " " "\t" > B.bed
echo  "
chr10 13 20 c_range_1
"| awk NF |tr " " "\t" > C.bed
}
cat A.bed
cat B.bed
cat C.bed



cat A.bed B.bed C.bed | bedtools sort  | bedtools merge
cat A.bed B.bed C.bed | bedtools sort
bedops --everything A.bed B.bed C.bed


bedtools intersect -a A.bed -b B.bed
bedtools intersect -a A.bed -b B.bed -wa
bedtools intersect -a A.bed -b B.bed -wb
bedtools intersect -a A.bed -b B.bed -wa -wb

bedops --intersect B.bed A.bed
```