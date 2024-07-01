
fasta 统计N区域

```bash
echo -en '>seq\nGTCAGNNNNNTGGTN\n'  | seqkit locate --ignore-case --only-positive-strand -r --pattern "N+" | column -t
echo -en '>seq\nGTCAGNNNNNTGGTN\n'  | seqkit locate --ignore-case --only-positive-strand -r --pattern "N+" -M | column -t
cat 67859-1005-PCRNGS-range.fasta  | seqkit locate --ignore-case --only-positive-strand -r --pattern "N+" -M | column -t

```
此方法速度过于缓慢

新方法

```python
from Bio.Seq import Seq
my_dna = Seq("AGTANNNCACTGGTN")
my_dna.find("N")
for x in re.compile("N+").finditer(str(my_dna)):
    a, b = x.span()
```

```python
from Bio import SeqIO
import re
import sys
# fasta = "/output/test-expand-10000/1653273178828/67859-1005-PCRNGS-range.fasta"
fasta = sys.argv[1]

for record in SeqIO.parse(fasta, "fasta"):
    for x in re.compile("N+").finditer(str(record.seq)):
        a, b = x.span()
        print(record.id, a, b, sep="\t")
```