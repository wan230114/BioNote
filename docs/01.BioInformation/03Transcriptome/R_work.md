## 计算RPKM和CPM
```R
countdata<-read.table("all.id.txt",skip = 1,sep="\t",header = T,row.names = 1)
head(countdata,2)
metadata <- countdata[,1:5]#提取基因信息count数据前的几列
head(metadata,2)
countdata <- countdata[,6:ncol(countdata)]#提取counts数，counts数据主题部分

prefix<-"couts"#设置输出文件前缀名

cpm <- t(t(countdata)/colSums(countdata) * 1000000)#参考cpm定义
head(cpm,2)
avg_cpm <- data.frame(avg_cpm=rowMeans(cpm))

#-----TPM Calculation------

kb <- metadata$Length / 1000

rpk <- countdata / kb

tpm <- t(t(rpk)/colSums(rpk) * 1000000)
head(tpm,2)
avg_tpm <- data.frame(avg_tpm=rowMeans(tpm))
head(avg_tpm,2)
write.csv(avg_tpm,paste0(prefix,"_avg_tpm.csv"))

write.csv(avg_cpm,paste0(prefix,"_avg_cpm.csv"))

write.csv(tpm,paste0(prefix,"_tpm.csv"))

write.csv(cpm,paste0(prefix,"_cpm.csv"))
```

