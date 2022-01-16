全转录组测序技术(WTS, Whole Transcriptome Sequencing )


- [x] [全转录组测序鉴定与 CHOL 相关的关键差异表达 mRNA、miRNA、lncRNA 和 circRNA - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2162253120301864)
    - 使用配对 t 检验和 Benjamini-Hochberg 方法对 C 与 CP 进行差异表达分析
    - DEG 编码的蛋白质之间的相互作用通过 STRING（版本 10.0）数据库进行分析。 输入基因集设置为所有 DEG，物种设置为人类。为了获得最密切相关的交互对，我们将参数 PPI 分数设置为 0.99（高置信度）。 PPI 网络由 Cytoscape 软件（3.2.0 版；https://cytoscape.org/）构建。 
    - 使用 miRWalk 2.0 (http://zmf.umm.uni-heidelberg.de/apps/zmf/mirwalk2/) 工具对获得的 dif-miRNA 进行 miRNA-基因预测分析。    
    - 使用 StarBase (http://starbase.sysu.edu.cn/) 数据库 (v.2.0) 预测 miRNA-lncRNA 和 miRNA-circRNA 对 dif-miRNA 的调控关系。
    - 利用dif-lncRNA、dif-circRNA、dif-mRNA的矩阵数据，计算出各个dif-mRNA和dif-lncRNA的Pearson相关系数，以及各个dif-mRNA和dif-circRNA的Pearson相关系数；进行相关测试以筛选重要的 mRNA-lncRNA 对和 mRNA-circRNA 对，阈值为 |r| >0.9 和 p <0.05。进一步得到了mRNA-lncRNA和mRNA-circRNA共表达关系列表。

