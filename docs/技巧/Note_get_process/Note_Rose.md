# Rose test

ref:
- /home/gzsc/biotools/ROSE_DATA
- /home/gzsc/biotools/rose
- /home/gzsc/work/gf/mm/ROSE/MC1_H3K27ac
- https://github.com/stjude/ROSE
- https://www.nature.com/articles/ncomms12983


## 准备

```bash
cp -ra /home/gzsc/biotools/rose .
cd rose

grep os.system $PWD/*py -n --color -B 1
# 修改Py使得运行日志输出
grep -P "\t" $PWD/*py -n
# 修改\t为空格

conda deactivate; source /home/chenjun/.conda_bashrc_my; conda activate python27
{
echo '
mkdir -p ./MC1_H3K27ac
python ./ROSE_main.py -g mm10 \
    -i /home/gzsc/work/gf/mm/bed/MC1_H3K27ac_peaks.bed \
    -r /home/gzsc/work/gf/mm//bam/SRR5419989_rmdup.bam \
    -c /home/gzsc/work/gf/mm//bam/SRR5419990_rmdup.bam \
    -o ./MC1_H3K27ac \
    -s 12500 -t 2500 1>log.o 2>log.e' >run.sh
}
nohup sh run.sh 1>log.o 2>log.e &

```