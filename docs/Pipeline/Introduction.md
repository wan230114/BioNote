## 为什么需要Pipeline？

<b>  </b>数据分析往往重复着很多的步骤与操作，做一个分析中，如果方法能被固定下来，那么再次运作时，基本就是改输入路径与输出路径，从一个软件对接到另一个软件，而这些工作完全可以被计算机所取代，所谓流程就是固定一套做事方法的程序，留出所谓变量为外部流程所控制。 我们往往关注的是方法与最终结果，中间的细节能把控就好。 

---
## 一个优秀的pipeline具备哪些要素？

基本要素：
- 使用门槛，尽量简洁。
- 可移植性。 不同平台之间快速配置环境兼容。
- 如何规范日志输出，易于检查查错。
- 流程输出基本命令，易于个性化定制。
- 计算资源的易于拓展。 如集群拓展，CPU，内存改动，使得资源分配同时调控。
- 易于检测流程运行状态。
- 检测每一步运行状态，以及是否达到预期结果。
    - 如果报错是否继续。是否因为资源分配问题的偶发，那么如何重复该步。
    - 如何是数据方面的问题，或者代码BUG，如何纠正后，迅速断点续跑。 
    - 如果达到预期结果，中间占用磁盘较大的中间文件是否可以删除？

其他:
- 文件输出是否需要分目录规范化。

---
一些优秀的Pipeline定义工具：
- [openwdl/wdl: Workflow Description Language - Specification and Implementations](https://github.com/openwdl/wdl)
    - 代表作： [ENCODE-DCC/chip-seq-pipeline2: ENCODE ChIP-seq pipeline](https://github.com/ENCODE-DCC/chip-seq-pipeline2)
- nextflow
- 基于nextflow的 nf-core


