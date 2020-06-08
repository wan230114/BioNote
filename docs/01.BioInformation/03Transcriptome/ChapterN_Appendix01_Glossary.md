名词解释：

# 5. 功能分析

## 5.1. GO与KEGG
参考：
- [GO和KEGG是什么意思 - 简书](https://www.jianshu.com/p/6003d341738a)
- [KEGG是什么：快速了解KEGG - 简书](https://www.jianshu.com/p/d7656c2e2cbe)

### 5.1.1. GO: Gene Ontology

GO数据库，全称是Gene Ontology(基因本体)，他们把基因的功能分成了三个部分分别是：细胞组分（cellular component, CC）; 分子功能（molecular function, MF）;生物过程（biological process, BP）。  
利用GO数据库，我们就可以得到我们的目标基因在CC, MF和BP三个层面上，主要和什么有关。

### 5.1.2. KEGG: Kyoto Encyclopedia of Genes and Genomes

KEGG (Kyoto Encyclopedia of Genes and Genomes)，

KEGG数据库：除了对基因本身功能的注释，我们也知道基因会参与人体的各个通路，基于人体通路而形成的数据库就是通路相关的数据库。而KEGG就是通路相关的数据库的一种。其实通路数据库有很多，类似于wikipathway，reactome都是相关的通路数据库。只是因为KEGG比较被人熟知，所以基本上都做这个分析的。

#### KO: KEGG Orthology
KEGG Orthology, 直接存储分子功能的就是 KEGG Orthology 数据库

KEGG Orthology 简称KO,该数据库中的每一条记录用K number 唯一标识。基于同源基因具有相似功能的假设，把基因的功能进行了扩充。对于某个物种中功能研究的很清楚的基因，在不同的物种间搜寻该基因的同源基因，将这些同源基因定义为一个orthology, 用该基因的功能作为该orthology 的功能；这样就将对于不同物种基因功能的研究都利用起来，提供了一个全面的研究基因功能的数据库。（https://cloud.tencent.com/developer/news/119170）

#### KEGG pathway

ko编号就是一个pathway，例如ko04722，这个通路不分物种，相当于所有物种这一通路的并集

**pathway的五种类型：**

仅仅第一种参考通路是手动画出来的，其他的通路图都是通过计算产生的。pathway中的每一个框或线都对应一个或多个K编号、EC编号及R编号。

- map - Reference pathway：对于代谢相关的通路，在reference pathway中，一个点同时表示一个基因，这个基因编码的酶或这个酶参加的反应
- ko - Reference pathway(KO)：KO通路中的点只表示基因
- ec - Reference pathway(EC)：EC通路中的点只表示相关的酶
- rn - Reference pathway(Reaction)：Reaction通路中的点只表示该点参与的某个反应、反应物及反应类型
- org - Organism-specific pathway map：对于所有的代谢和非代谢通路，K编号都被认为是基因的标识符，这个标识符在每一个物种中对应该物种中的某个基因，从而得到物种特异性的pathway。

