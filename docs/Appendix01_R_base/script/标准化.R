#sweep再举一个例子哈
m<-matrix(c(1:9),byrow=TRUE,nrow=3)
#第一行都加1，第二行都加4，第三行都加7
sweep(m, 1, c(1,4,7), "+")  

t(scale(t(m), center = TRUE, scale = F))