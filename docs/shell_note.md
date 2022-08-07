
用于检查原始数据完整性

```bash
for fqgz in `ls *.fq.gz`; do
    echo
    echo ========== checking fastq file $fqgz ==========
    zcat $fqgz | awk 'BEGAIN{stat=0; n=0}{
        a[NR]=$0; if (NR>24){ delete a[NR-24] }
        if (NR%4==1){  if($0!~/@/){ stat=1 } } else if (NR%4==3){ if($0!="+"){ stat=1 } }
        if (stat){  n+=1 }
        if(n>11){ for (row in a){ print row": "a[row] }; exit}
    }'
done >log.txt 2>&1  
```

