a <- TRUE
b <- 1
c <- "1"
d <- factor(c("A","B"),levels=c("A","B","C","D","E"))
e <- factor(c("A","B","F"),levels=c("A","B","C","D","E"))

'''
[1] TRUE
[1] 1
[1] "1"
[1] A B
Levels: A B C D E
[1] A    B    <NA>
Levels: A B C D E
'''