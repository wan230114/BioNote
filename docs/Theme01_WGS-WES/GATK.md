

ALT列为什么能同时存在两种变异？
- 答： 这种同一个位点有多个变异的叫多等位位点，即两个等位基因都发生了变异

```tsv
##CMD=cat <(e J2105130011-4100-MES-GATK-vqsr.vcf.gz | grep "#CHROM" ) <(e J2105130011-4100-MES-GATK-vqsr.vcf.gz | awk -F "\t" '{if($5~/,/)print}') | T -c 'xxxxx'
#CHROM  POS        ID  REF                              ALT                                               QUAL      FILTER                       INFO                                                                                                                                               
chr1    6029086    .   CAA                              C,CA                                              776.02    PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=1.800,0.300;AS_FS=2.796,2.043;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=0.000,0.000;AS_QD
chr1    16951432   .   CAAAAAAAAAAAAAAAAA               C,CA                                              193.02    PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=.,.;AS_QD=23.67,21.00;AS_
chr1    19203155   .   C                                CTGTGTGTGTGTGTGTGTG,CTGTGTGTGTGTGTGTGTGTG         190.02    PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=.,.;AS_QD=20.00,21.33;AS_
chr1    82149649   .   AC                               GC,GT                                             132.10    PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=.,.;AS_QD=18.00,17.50;AS_
chr1    100652404  .   C                                T,CAT                                             798.06    PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=.,.;AS_QD=28.54,27.60;AS_
chr1    100654907  .   TAA                              T,TA                                              1022.02   PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=-1.100,-0.400;AS_FS=2.336,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=0.000,0.000;AS_
chr1    100657303  .   TATACACACACACACACACACACACACACAC  T,TAC                                             4333.02   PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=.,.;AS_QD=24.26,27.15;AS_
chr1    100696185  .   G                                GA,GAA                                            1665.02   PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=1.800,1.000;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=0.000,0.000;AS_QD
chr1    121485001  .   GC                               AC,AG                                             6332.10   PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=1.400,2.500;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=59.02,58.56;AS_MQRankSum=-0.800,-1.500;AS_
chr1    145185588  .   ATT                              A,AT                                              95.02     PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=43.64,60.00;AS_MQRankSum=.,.;AS_QD=19.50,17.50;AS_
chr1    155208647  .   T                                C,G                                               1125.10   PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=55.72,58.32;AS_MQRankSum=.,.;AS_QD=22.64,24.95;AS_
chr1    156845492  .   AGTGT                            A,AGT                                             352.02    PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=1.200,1.200;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=0.000,0.000;AS_QD
chr1    209788213  .   TG                               CA,CG                                             12504.10  PASS                         AC=1,1;AF=0.500,0.500;AN=2;AS_BaseQRankSum=.,.;AS_FS=0.000,0.000;AS_FilterStatus=PASS,PASS;AS_MQ=60.00,60.00;AS_MQRankSum=.,.;AS_QD=23.96,25.16;AS_
```

