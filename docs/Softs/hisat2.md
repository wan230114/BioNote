

hisat2

```bash
--rna-strandness RF  使得bam输出结果最后一列增加±链信息，帮助分链。该分链会把所有的模糊匹配多比对singleton也算进去，但是可能不那么严格。如果需要严格的做法，还需按4个flag值分链较好
--summary-file <path.summary>  使得比对完后输出比对结果情况的详细信息，该结果可以直接被multiqc可视化为网页
```

```bash
samtools view -F 256 3-2.sorted.bam | grep A00821:419:HC3CMDSXY:3:2253:28402:32643
# A00821:419:HC3CMDSXY:3:2253:28402:32643 99    1   182079      1   150M    =   182197      268     TTTGTTAACTGATTACCATCAGAATTGTACTGTTCTGTATCCCACCAGCAATGTCTAGGAATACCTGTTTCTCCACAAAGTGTTTACTTTTGGATTTTTGCCAGTCTAACAGGTGAAGCCCTGGAGATTCTTATTAGTGATTTGGGCTGG        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:F:FFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFF  AS:i:-10  ZS:i:-10   XN:i:0  XM:i:2  XO:i:0  XG:i:0  NM:i:2  MD:Z:16T45G87  YS:i:0    YT:Z:CP NH:i:4
# A00821:419:HC3CMDSXY:3:2253:28402:32643 147   1   182197      1   150M    =   182079      -268    CCCTGGAGATTCTTATTAGTGATTTGGGCTGGGGCCTGGCCATGTGTATTTTTTTAAATTTCCACTGATGATTTTGCTGCATGGCCGGTGTTGAGAATGACTGCGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAAC        FFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  AS:i:0    ZS:i:0     XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:150       YS:i:-10  YT:Z:CP NH:i:4

samtools view -f 256 3-2.sorted.bam | grep A00821:419:HC3CMDSXY:3:2253:28402:32643
# A00821:419:HC3CMDSXY:3:2253:28402:32643 355   1   11560       1   150M    =   182197      150328  TTTGTTAACTGATTACCATCAGAATTGTACTGTTCTGTATCCCACCAGCAATGTCTAGGAATACCTGTTTCTCCACAAAGTGTTTACTTTTGGATTTTTGCCAGTCTAACAGGTGAAGCCCTGGAGATTCTTATTAGTGATTTGGGCTGG        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:F:FFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFF  AS:i:-10  ZS:i:-10   XN:i:0  XM:i:2  XO:i:0  XG:i:0  NM:i:2  MD:Z:5G56G87   YS:i:0    YT:Z:CP NH:i:4
# A00821:419:HC3CMDSXY:3:2253:28402:32643 355   1   11560       1   150M    =   11678       268     TTTGTTAACTGATTACCATCAGAATTGTACTGTTCTGTATCCCACCAGCAATGTCTAGGAATACCTGTTTCTCCACAAAGTGTTTACTTTTGGATTTTTGCCAGTCTAACAGGTGAAGCCCTGGAGATTCTTATTAGTGATTTGGGCTGG        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:F:FFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFF  AS:i:-10  ZS:i:-10   XN:i:0  XM:i:2  XO:i:0  XG:i:0  NM:i:2  MD:Z:5G56G87   YS:i:0    YT:Z:CP NH:i:4
# A00821:419:HC3CMDSXY:3:2253:28402:32643 403   1   11678       1   150M    =   11560       -268    CCCTGGAGATTCTTATTAGTGATTTGGGCTGGGGCCTGGCCATGTGTATTTTTTTAAATTTCCACTGATGATTTTGCTGCATGGCCGGTGTTGAGAATGACTGCGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAAC        FFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  AS:i:0    ZS:i:0     XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:150       YS:i:-10  YT:Z:CP NH:i:4
# A00821:419:HC3CMDSXY:3:2253:28402:32643 403   1   182197      1   150M    =   11560       -150328 CCCTGGAGATTCTTATTAGTGATTTGGGCTGGGGCCTGGCCATGTGTATTTTTTTAAATTTCCACTGATGATTTTGCTGCATGGCCGGTGTTGAGAATGACTGCGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAAC        FFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  AS:i:0    ZS:i:0     XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:150       YS:i:-10  YT:Z:CP NH:i:4
# A00821:419:HC3CMDSXY:3:2253:28402:32643 419   15  101979140   1   150M    =   101979258   268     GTTTAAACTACATGCAGGAACAGCAAAGGAAATCCGGCAAATTTGCGCAGTCATTCTCAACACCGGCCATGCAGCAAAATCATCAGTGGAAATTTAAAAAAATACACATGGCCAGGCCCCAGCCCAAATCACTAATAAGAATCTCCAGGG        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFF  AS:i:0    ZS:i:0     XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:150       YS:i:-10  YT:Z:CP NH:i:4
# A00821:419:HC3CMDSXY:3:2253:28402:32643 339   15  101979258   1   150M    =   101979140   -268    CCAGCCCAAATCACTAATAAGAATCTCCAGGGCTTCACCTGTTAGACTGGCAAAAATCCAAAAGTAAACACTTTGTGGAGAAACAGGTATTCCTAGACATTGCTGGTGGGATACAGAACAGTACAATTCTGATGGTAATCAGTTAACAAA        FFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFF:F:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  AS:i:-10  ZS:i:-10   XN:i:0  XM:i:2  XO:i:0  XG:i:0  NM:i:2  MD:Z:87C56C5   YS:i:0    YT:Z:CP NH:i:4
```


```bash
samtools view -F 256 3-2.sorted.bam | grep A00821:419:HC3CMDSXY:3:2553:21287:25582
# A00821:419:HC3CMDSXY:3:2553:21287:25582 163   1   185323      1       28M140N69M757N7M        =       185323      -244    CCAGCCCCAGGTCCTTTCCCAGAGATGCCCTTGCGCCTCATGACCAGCTTGTTGAAGAGATCCGACATCAAGTGCCCACCTTGGCTCGTGGCTCTCACTTGCTC     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFF:FFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFF AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:-  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 83    1   185323      1       28M140N69M757N7M        =       185323      -244    CCAGCCCCAGGTCCTTTCCCAGAGATGCCCTTGCGCCTCATGACCAGCTTGTTGAAGAGATCCGACATCAAGTGCCCACCTTGGCTCGTGGCTCTCACTTGCTC     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:-  NH:i:6

samtools view -f 256 3-2.sorted.bam | grep A00821:419:HC3CMDSXY:3:2553:21287:25582
# A00821:419:HC3CMDSXY:3:2553:21287:25582 355   15  101975159   1       7M758N69M140N28M        =       101975159   -862    GAGCAAGTGAGAGCCACGAGCCAAGGTGGGCACTTGATGTCGGATCTCTTCAACAAGCTGGTCATGAGGCGCAAGGGCATCTCTGGGAAAGGACCTGGGGCTGG     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF        AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:+  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 403   15  101975159   1       7M758N69M140N28M        =       101975159   -862    GAGCAAGTGAGAGCCACGAGCCAAGGTGGGCACTTGATGTCGGATCTCTTCAACAAGCTGGTCATGAGGCGCAAGGGCATCTCTGGGAAAGGACCTGGGGCTGG     FFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFF:FFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF        AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:+  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 419   16  14484       1       28M140N69M760N7M        =       14484       -244    CCAGCCCCAGGTCCTTTCCCAGAGATGCCCTTGCGCCTCATGACCAGCTTGTTGAAGAGATCCGACATCAAGTGCCCACCTTGGCTCGTGGCTCTCACTTGCTC     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFF:FFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFF AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:-  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 339   16  14484       1       28M140N69M760N7M        =       14484       -244    CCAGCCCCAGGTCCTTTCCCAGAGATGCCCTTGCGCCTCATGACCAGCTTGTTGAAGAGATCCGACATCAAGTGCCCACCTTGGCTCGTGGCTCTCACTTGCTC     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:-  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 355   2   113597632   1       7M759N69M140N28M        =       113597632   -863    GAGCAAGTGAGAGCCACGAGCCAAGGTGGGCACTTGATGTCGGATCTCTTCAACAAGCTGGTCATGAGGCGCAAGGGCATCTCTGGGAAAGGACCTGGGGCTGG     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF        AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:+  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 403   2   113597632   1       7M759N69M140N28M        =       113597632   -863    GAGCAAGTGAGAGCCACGAGCCAAGGTGGGCACTTGATGTCGGATCTCTTCAACAAGCTGGTCATGAGGCGCAAGGGCATCTCTGGGAAAGGACCTGGGGCTGG     FFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFF:FFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF        AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:+  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 419   9   14913       1       28M140N69M759N7M        =       14913       -244    CCAGCCCCAGGTCCTTTCCCAGAGATGCCCTTGCGCCTCATGACCAGCTTGTTGAAGAGATCCGACATCAAGTGCCCACCTTGGCTCGTGGCTCTCACTTGCTC     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFF:FFFFFFFFFFFFF,FFFFFFFFFFFFFFFFFFFFFFF AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:-  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 339   9   14913       1       28M140N69M759N7M        =       14913       -244    CCAGCCCCAGGTCCTTTCCCAGAGATGCCCTTGCGCCTCATGACCAGCTTGTTGAAGAGATCCGACATCAAGTGCCCACCTTGGCTCGTGGCTCTCACTTGCTC     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:-  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 355   X   156024266   1       7M759N69M140N28M        =       156024266   -812    GAGCAAGTGAGAGCCACGAGCCAAGGTGGGCACTTGATGTCGGATCTCTTCAACAAGCTGGTCATGAGGCGCAAGGGCATCTCTGGGAAAGGACCTGGGGCTGG     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF        AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:+  NH:i:6
# A00821:419:HC3CMDSXY:3:2553:21287:25582 403   X   156024266   1       7M759N69M140N28M        =       156024266   -812    GAGCAAGTGAGAGCCACGAGCCAAGGTGGGCACTTGATGTCGGATCTCTTCAACAAGCTGGTCATGAGGCGCAAGGGCATCTCTGGGAAAGGACCTGGGGCTGG     FFFFFFFFFFFFFFFFFFFFFFF,FFFFFFFFFFFFF:FFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF        AS:i:0  ZS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:104        YS:i:0  YT:Z:CP XS:A:+  NH:i:6

```