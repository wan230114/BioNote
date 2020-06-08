生信常见文件
---

# 3.3.1. 基因序列  
## 3.3.1.1. fq / fasq  
略  

# 3.3.2. 注释文件  
## 3.3.2.1. gff3

### 文件描述
官网描述：  
> Generic Feature Format Version 3 （GFF3）  
> http://www.sequenceontology.org/gff3.shtml

GFF3文件格式描述  
> GFF3格式文件为文本文件，分为9列，以TAB分开。控制符使用 RFC 3986 Percent-Encoding 编码。比如：%20 代表着ASCII的空格。  
  
9列文件依次是：  
> 1. `seqid` ：参考序列的id。该id的取名不能以’>’开头，不能包含空格。  
> 2. `source` ：注释的来源。如果未知，则用点（.）代替。一般指明产生此gff3文件的软件或方法。  
> 3. `type` ：属性的类型。建议使用符合SO惯例的名称（sequence ontology，参看[[Sequence Ontology Project]]) ,如gene，repeat_region，exon，CDS等。  
> 4. `start position` ：属性对应片段的起点。从1开始计数。  
> 5. `end position` ：属性对应片段的终点。一般比起点的数值要大。  
> 6. `score` ：得分，对于一些可以量化的属性，可以在此设置一个数值以表示程度的不同。如果为空，用点（.）代替。  
> 7. `strand` ：“＋”表示正链，“－”表示负链，“.”表示不需要指定正负链。  
> 8. `phase` ：步进。对于编码蛋白质的CDS来说，本列指定下一个密码子开始的位置。可以是0，1或2，表示到达下一个密码子需要跳过的碱基个数。  
> 对于其它属性，则用点（.）代替。  
> 9. `attributes` ：属性  
> 一个包含众多属性的列表。格式为“标签＝值”（tag=value）。不同属性之间以分号相隔。可以存在空格，不过若有“,=;”则用URL转义（URL escaping rule），同时TAB也需要转换为“%09”表示。所有以大写字幕开头的标签被保留，用于大众认可的用途，而以小写字母开头的标签则根据自己安排随意应用。  
> 
> 
> 常用的标签有：  
> - `ID` ：Feature的标识。该ID具有唯一性。指定一个唯一的标识。对属性分类是非常好用（例如查找一个转录单位中所以的外显子）。
> - `Name` ：Feature的展示名称。Name的值在可视化的时候得到展示。因此，Name可以根据自己展示的需要随意取值。指定属性的名称，展示给用户的就是该属性。
> - `Alias` ：Feature的第2个Name。名称的代称或其它。当存在其它名称时使用该属性。
> - `Parent` ：指明feature所从属的上一级ID。用于将exons聚集成transcript，将transripts聚集成gene。  
> - `Target` ：指明比对的目标区域，一般用于表明序列的比对结果。格式为”target_id start end [strand]”,其中strand是可选的(“+”或”-“), target_id中如果包含空格，则要转换成’%20’。  
> - `Gap` ：比对结果的gap信息，和Target一起，用于表明序列的比对结果。  
> - `Note` ：文本描述，描述性的一些说明。
> - `Is_circular` ：表明featrue是否为环化的。用于环状基因组序列。  
> 
> 同一个tag如果有多个值，则多个值之间使用逗号隔开。
> - 比如：  
> Parent=AF2312,AB2812,abc-3  
> Alias=M19211,gna-12,GAMMA-GLOBULIN  
> - 能够使用多个值的tag有：Parent, Alias, Note, Dbxref and Ontology_term。  


来源：简书，链接：https://www.jianshu.com/p/65bd49d1dbae

### 示例

该示例摘自：[TAIR的gff3文件](https://www.arabidopsis.org/download_files/Genes/Araport11_genome_release/Araport11_GFF3_genes_transposons.201606.gff.gz)

通过查看第三列可以发现类型之多：
```bash
$ less Araport11_GFF3_genes_transposons.201606.gff.gz |
  grep -v "^##"|cut -f 3|sort|uniq -c|sort -k1n
     15 rRNA
     27 pseudogenic_tRNA
     82 snRNA
     91 antisense_RNA
    111 uORF
    286 ncRNA
    287 snoRNA
    325 miRNA_primary_transcript
    427 miRNA
    689 tRNA
    726 transcript_region
    952 pseudogene
   1100 pseudogenic_transcript
   1424 antisense_lncRNA
   2058 pseudogenic_exon
   2455 lnc_RNA
   3901 transposable_element_gene
  31189 transposable_element
  33341 gene
  34856 transposon_fragment
  41127 three_prime_UTR
  46895 five_prime_UTR
  48359 protein
  52270 mRNA
 200542 exon
 286355 CDS
```

文件前24行：

[Ara.gff3](demo/Ara.gff3 ':include')