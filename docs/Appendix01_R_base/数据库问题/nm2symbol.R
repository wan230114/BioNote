## install steps, run once
# install.packages("devtools")
# devtools::install_github("stephenturner/annotables")
# install.packages("tidyverse")

library(annotables)
library(tidyverse)
## ── Attaching packages ─────────────── tidyverse 1.2.1 ──
## ✔ ggplot2 3.0.0     ✔ purrr   0.2.4
## ✔ tibble  1.4.2     ✔ dplyr   0.7.6
## ✔ tidyr   0.8.1     ✔ stringr 1.3.1
## ✔ readr   1.1.1     ✔ forcats 0.3.0
## Warning: package 'dplyr' was built under R version 3.5.1
## ── Conflicts ────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
grch38 %>% head()
## # A tibble: 6 x 9
##   ensgene  entrez symbol chr    start    end strand biotype description   
##   <chr>     <int> <chr>  <chr>  <int>  <int>  <int> <chr>   <chr>         
## 1 ENSG000…   7105 TSPAN6 X     1.01e8 1.01e8     -1 protei… tetraspanin 6…
## 2 ENSG000…  64102 TNMD   X     1.01e8 1.01e8      1 protei… tenomodulin […
## 3 ENSG000…   8813 DPM1   20    5.09e7 5.10e7     -1 protei… dolichyl-phos…
# or grch37, grcm38, rnor6, galgal5, wbcel235, bdgp6, mmul801


## install steps, run once
# source("https://bioconductor.org/biocLite.R")
# biocLite("biomaRt")
# library(biomaRt) # <- don't load!, just use the :: 
mart<- biomaRt::useMart(biomart = 'ensembl', dataset = 'hsapiens_gene_ensembl')
# mapping example
refseq_ids <- c("NM_006573", "NM_002985", "NM_032965", "NM_002987", "NM_006274", "NM_004591", "NM_002990")
  
refseq_mapping <- biomaRt::getBM(attributes = c("refseq_mrna","hgnc_symbol"), 
                        filters="refseq_mrna", # you swap out of this filter for whatever your input is
                        values=refseq_ids, # vector of your NMf
                        mart=mart)
refseq_mapping
left_join(select(refseq_mapping, symbol = hgnc_symbol, refseq_mrna), grch38)
