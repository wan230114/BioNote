#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-03-07, 02:16:11
# @ Modified By: Chen Jun
# @ Last Modified: 2021-03-07, 15:22:19
#############################################

require(ggplot2)

# Bogus data
x <- rnorm(10000)
y <- as.factor(round(rnorm(10000, mean = 10, sd = 2), 0))
df <- data.frame(vals = x, factors = y)

myplot <- ggplot(data = df, aes(x = vals)) +
    geom_density() +
    facet_wrap(~factors)

ggsave(filename = "foo.pdf", plot = myplot, width = 8, height = 10, units = "in")