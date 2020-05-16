# 1. 基因组序列处理工具

## 1.1. FASTX-Toolkit

**简介：**  

- 功能：序列格式转化，按多少BP换行处理，...
- 官网：http://hannonlab.cshl.edu/fastx_toolkit/

**安装：**  

- 搜索具体名字，如果软件包发生更改，用此命令搜索

    ```shell
    conda search fastax
    ```

- 安装：

    ```shell
    conda install fastax_toolkit
    ```

**使用示例：**

- 按行基因处理按70bp换行格式化处理：

    ```shell
    fasta formatter -i genome.fa -o genome _format.fa -w 70
    ```

