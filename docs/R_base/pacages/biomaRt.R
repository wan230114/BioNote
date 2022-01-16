#!/usr/bin/env Rscript

library(biomaRt)
ensembl <- useMart("ensembl") # connect to a specified BioMart database
ensembl <- useDataset("hsapiens_gene_ensembl", mart = ensembl)
# use the hsapiens(人类) dataset.或者直接如下设置
# ensembl = useMart("ensembl",dataset="hsapiens_gene_ensembl")
test <- getBM(
    attributes = c(
        "ensembl_gene_id", "start_position",
        "end_position", "ensembl_transcript_id",
        "transcript_length"
    ),
    filter = "ensembl_gene_id",
    values = c("ENSG00000288723", "ENSG00000288724", "ENSG00000288725"),
    mart = ensembl
)
test
