args <- commandArgs()
print("args <- commandArgs()")
print(args)

args <- commandArgs(T)  # 等效于 args <- commandArgs(trailingOnly = TRUE)
print("args <- commandArgs(T)")
print(args)
