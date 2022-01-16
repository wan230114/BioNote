
## 引用DiffBind的一些文章

关键词：[diffbind chip-seq - Google Scholar](https://scholar.google.com/scholar?q=diffbind+chip-seq)

Kelley, Dylan Z., et al. "Integrated analysis of whole-genome ChIP-Seq and RNA-Seq data of primary head and neck tumor samples associates HPV integration sites with open chromatin marks." Cancer research 77.23 (2017): 6538-6550. [[full text]](https://cancerres.aacrjournals.org/content/77/23/6538.full)


##  一些使用者评价

### 优于其他同类分析方法

- 使用来自bam的结果进行标准化系数

> 不过对于该文章，他们从计数矩阵中去修改标准化参数。正确性有待考证。
> 
> 使用校正尺寸因子与Diffbind集成   
> 在Chip-SEQ分析工具的比较研究中，Diffbind**可靠地优于其他方法**（12），是分析多种重复的芯片-SEQ实验的优选策略。出于这些原因，我们选择困境以支撑我们的分析方法，并作为改进的关键基准。 DiffBind的一个关键特征是，为了计算大小因子，**它利用来自样品表（例如BAM文件）中提供的序列数据的总库大小而不是DESEQ2提供的估计性Factor函数**。尽管如此，在改进的同时，Diffbind对原始数据的分析与推定的不变峰值不完整，示出> 0对数折叠变化（补充图S12）。为了解决这种缺点，我们修改了Diffbind包，直接从控制峰的计数矩阵计算SOUDICFACTOR参数，在我们的情况下，在我们的情况下是H2AV或CTCF峰值（补充图S12B）。[^1]

[^1]: [Guertin, Michael J., et al. "Parallel factor ChIP provides essential internal control for quantitative differential ChIP-seq." Nucleic acids research 46.12 (2018): e75-e75.](https://academic.oup.com/nar/article/46/12/e75/4972874?login=true)


