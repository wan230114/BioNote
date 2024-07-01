#!/usr/bin/env bash
set -ev

bam=`realpath $1`
name=`basename $bam .bam`
dirname=reads_density-${name}
mkdir -p $dirname && cd $dirname
samtools view $bam -H | grep ^@SQ | sed -e 's#@SQ\tSN:##' -e 's#LN:##' | awk '{print $1 "\t" 1 "\t" $2}' > ${name}-genome.txt


bedtools makewindows -b ${name}-genome.txt -w 1000 > ${name}-genome.window.bed
awk '{print $1"\t"$2"\t"$3"\t0\t0\t+\n"$1"\t"$2"\t"$3"\t0\t0\t-"}'  ${name}-genome.window.bed > ${name}-genome.window.bed.region

# bedtools coverage -S -abam $bam -b ${name}-genome.window.bed.region > ${name}-genome.window.bed.region.cov
# cat ${name}-genome.window.bed.region.cov | cut -f 1,2,6,7 > ${name}-genome.window.bed.region.cov.txt
bedtools bamtobed -i $bam   > ${name}-bam.bed
bedtools coverage -S -a ${name}-genome.window.bed.region -b ${name}-bam.bed > ${name}-genome.window.bed.region.cov
cut -f 1,2,3,6,7 ${name}-genome.window.bed.region.cov > ${name}-genome.window.bed.region.cov.txt

# docker run --rm -it --entrypoint="" -v $PWD:$PWD rocker/tidyverse R

echo '
data <- read.table("./'${name}-genome.window.bed.region.cov.txt'",sep="\t")
library(tidyverse)
data <- data  |>
    mutate(log=case_when(V4=="+"~log2(V5+1),
    V4!="+"~ -log2(V5+1))) 

# chr <-c("chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chr22","chrX","chrY") #因为人类染色体还有很多非常规染色体，如果全部画出来会不好看，所有此处只画出常规染色体。也可以在文件hg19.txt里面只输入常规染色体。data2<- data[data$V1 %in% chr,]
chr <- as.vector(read.table("'${name}-genome.txt'")[,1])
# data2<- data[data$V1 %in% c(c(1:20),"X","Y","MT"),]
data2<- data
color <- c("+"="#008B00","-"="#FF8247") # 定义正负链颜色

png(file="'$dirname'.png", width=1200, height=1200)
# pdf(file="'$dirname'.pdf", width=12, height=12)
ggplot(data2)+
    facet_grid(V1~.)+
    geom_point(aes(V2/1000000,log,colour=V4),size=1)+
    theme(
    strip.text.y=element_text(angle=0,face="bold",hjust=0),
    legend.position="none",panel.grid.minor=element_blank(),
    panel.grid.major=element_blank(),
    plot.title=element_text(size=20,face="bold"),
    axis.text.y=element_text(size=10,angle=50,face="bold"),
    strip.background=element_blank(),
    panel.background=element_rect(fill="white"),
    axis.line=element_line(linetype=1))+
    scale_colour_manual(values=color)+
    scale_y_continuous(breaks=c(-15,15))+
    labs(title="Reads Density in Chromosomes ('$(basename $bam)')")+
    xlab("chromosome position(Mb)")+
    ylab("reads density(log2)")
dev.off()
' > plot-${name}.R
Rscript plot-${name}.R

rm -f ${name}-genome.txt ${name}-genome.window.bed ${name}-genome.window.bed.region ${name}-bam.bed ${name}-genome.window.bed.region.cov

gzip ${name}-genome.window.bed.region.cov.txt

