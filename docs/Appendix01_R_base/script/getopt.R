#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-01-06, 17:27:49
# @ Modified By: Chen Jun
# @ Last Modified: 2021-01-06, 17:27:51
#############################################

library("getopt")

## 定义参数
command <- matrix(c(
    "help", "h", 0, "loical", "帮助文档",
    "infileBed", "i", 0, "character", "输入的bed文件",
    "outName", "o", 1, "character", "输出的所有文件前缀",
    "ref", "r", 1, "character", "输入使用的参考，hg38/mm10，默认为hg38"
), byrow = T, ncol = 5)
args <- getopt(command)

## 判断如果为空，则退出
if (!is.null(args$help) || is.null(args$infileBed)) {
    cat(paste(getopt(command, usage = T), "\n"))
    q(status = 1)
}

## 设置默认值
if (is.null(args$outName)) {
    cat("未输入outName, 默认去除后缀“.bed”\n")
    SampleName <- substr(basename(args$infileBed), 1, nchar(basename(args$infileBed)) - 4) # 去除后缀 .bed
} else {
    SampleName <- args$outName
}
if (is.null(args$ref)) {
    cat("未输入ref, 默认hg38\n")
    ref <- "hg38"
} else {
    ref <- args$ref
}
infileBed <- args$infileBed

cat(paste0(
    "\n输入infileBed：", infileBed,
    "\n输出的名字前缀：", SampleName,
    "\n参考：", ref,
    "\n"
))
