#!/usr/bin/env Rscript
#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-06-17, 17:35:19
# @ Modified By: Chen Jun
# @ Last Modified: 2021-06-17, 23:40:40
#############################################


#############################################
####### Getting Help #########
#############################################

## Accessing the help files

?mean
# Get help of a particular function.
help.search("weighted mean")
# Search the help files for a word or phrase.
help(package = "dplyr")
# Find help for a package.


## More about an object

str(iris)
# Get a summary of an object’s structure.
class(iris)
# Find the class an object belongs to.


#############################################
####### Using Libraries #########
#############################################

install.packages("dplyr")
# Download and install a package from CRAN.

library(dplyr)
# Load the package into the session, making all its functions available to use.

dplyr::select
# Use a particular function from a package.

data(iris)
# Load a built-in dataset into the environment.


#############################################
####### Working Directory #########
#############################################

getwd()
# Find the current working directory (where inputs are found and outputs are sent).
setwd("~/")
# Change the current working directory.

# Use projects in RStudio to set the working directory to the folder you are working in.


#############################################
####### Vectors #########
#############################################

## Creating Vectors

c(2, 4, 6) # 2 4 6
# Join elements into a vector

2:6 # 2 3 4 5 6
# An integer sequence

seq(2, 3, by = 0.5) # 2.0 2.5 3.0
# A complex sequence

rep(1:2, times = 3) # 1 2 1 2 1 2
# Repeat a vector

rep(1:2, each = 3) # 1 1 1 2 2 2
# Repeat elements of a vector


## Vector Functions

x <- c("c", "c", "a", "a", "b", "b", "b")

sort(x)
# Return x sorted.
rev(x)
# Return x reversed.
table(x)
# See counts of values.
unique(x)
# See unique values.

### Selecting Vector Elements

### By Position

x[4]
# The fourth element.
x[-4]
# All but the fourth.
x[2:4]
# Elements two to four.
x[-(2:4)]
# All elements except two to four.
x[c(1, 5)]
# Elements one and five.

### By Value
x <- -10:10
x[x == 10]
# Elements which are equal to 10.
x[x < 0]
# All elements less than zero.
x %in% c(1, 2, 5)
x[x %in% c(1, 2, 5)]
# Elements in the set 1, 2, 5.

### Named Vectors
x <- -10:10
names(x) <- c("apple", "abc123", "apple")
x
x["apple"]
x[c("apple", "abc123")]
# Element with name ‘apple’.


#############################################
####### Programming #########
#############################################

## For Loop

# for (variable in sequence){
#     Do something
# }
x <- 10:14
for (i in 1:length(x)) {
    cat("index:", i, "  vaule:", x[i], "\n")
}

## While Loop
# while (condition){
#     Do something
# }
i <- 0
while (i < 5) {
    print(i)
    i <- i + 1
}


# if (condition){
#     Do something
# } else {
#     Do something different
# }
i <- 1
if (i > 3) {
    print("Yes")
} else {
    print("No")
}