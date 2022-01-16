#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# [RNA-seq数据差异表达分析](https://mp.weixin.qq.com/s?src=11&timestamp=1621838056&ver=3087&signature=yXUtYcqwocIOSviwiPnAn9o3uQsK4sqpJc4LpU5SUWQrGEzjPN*ImtKxwQyY9jtj8k4HeMjssvoSV2qxJq7*689DH9esuapDwoy6cLxJIY2TAXSrwmG10DrTY7w7gbPP&new=1)
# 火山图代码（python）：


import seaborn as sns
import numpy as np
import pandas as pd
# %%
# pd.DataFrame([[1,2,3,4,5],])


# %%
# difexp1 = pd.read_table('dif_exp.csv', sep='\t')
difexp1 = pd.DataFrame({"fold": np.arange(1, 6), "pvalue": np.arange(1, 6)/10})
difexp = difexp1.dropna()

# 将所有基因分为三部分
difexp['sig'] = 'normal'
difexp.loc[(difexp.fold > 1) & (difexp.pvalue < 0.05), 'sig'] = 'up'
difexp.loc[(difexp.fold < -1) & (difexp.pvalue < 0.05), 'sig'] = 'down'
difexp['log(pvalue)'] = -np.log10(difexp['pvalue'])

ax = sns.scatterplot(x="fold", y="log(pvalue)",
                     hue='sig',
                     hue_order=('down', 'normal', 'up'),
                     palette=("#377EB8", "grey", "#E41A1C"),
                     data=difexp)
ax.set_ylabel('-log10(pvalue)', fontweight='bold')
ax.set_xlabel('log2(FoldChange)', fontweight='bold')
