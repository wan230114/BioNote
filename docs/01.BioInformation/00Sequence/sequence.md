
# 测序原理

[测序结果中的接头序列来自哪里？ | Public Library of Bioinformatics](https://www.plob.org/article/12140.html)


---
- [ ] [barcode 测序_百度搜索](https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=barcode%20%E6%B5%8B%E5%BA%8F&oq=barcode&rsv_pq=ab184041000079c6&rsv_t=4042RP0enHP8SlwLe4Uvlng69Tm%2BpKTmTGAKlioa%2FHNl8JAvVkgTq4gwbMs&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_btype=t&inputT=3426&rsv_sug4=3532)
- [ ] [二代测序的Barcode选择 | Public Library of Bioinformatics](https://www.plob.org/article/21117.html)


# 建库流程

- [ ] [微生物实验流程及操作介绍 - 豆丁网](https://www.docin.com/p-2089290824.html)



---
# 关于质量值

基因的二代测序中，每测一个碱基会给出一个相应的质量值，这个质量值是衡量测序准确度的。碱基的质量值13，错误率为5%，20的错误率为1%，30的错误率为0.1%。行业中Q20与Q30则表示质量值≧20或30的碱基所占百分比。例如一共测了1G的数据量，其中有0.9G的碱基质量值大于或等于20，那么Q20则为90%。

Q20值是指的测序过程碱基识别（Base Calling）过程中，对所识别的碱基给出的错误概率。

质量值是Q20，则错误识别的概率是1%，即错误率1%，或者正确率是99%；
质量值是Q30，则错误识别的概率是0.1%，即错误率0.1%，或者正确率是99.9%；
质量值是Q40，则错误识别的概率是0.01%，即错误率0.01%，或者正确率是99.99%；

```yml
Q = -10*log10(error P)


Phred+33  [Q+33 => ASCII字符]：

!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI
|    |    |    |    |    |    |    |    |
0....5...10...15...20...25...30...35...40
worst................................best


Phred+64  [Q+64 => ASCII字符]：

@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghi
|    |    |    |    |    |    |    |    |
0....5...10...15...20...25...30...35...40
worst................................best
```
