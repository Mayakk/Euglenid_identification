
tab1 = read.table("filtered-table.txt ", sep="\t",dec = ".", check.names = FALSE, header=TRUE)

sums = c()      # creates empty vector
for (taxon in c(1:length(tab1[,1]))){ # row numbers
  rowsum <- (sum(tab1[taxon,2:length(tab1[1,])]))  # sums values for given row
  sums[taxon] <- rowsum    # adds row sum to the vector
}

halfper = c()      # creates empty vector
for (taxon in c(1:length(tab1[,1]))){ # row numbers
  rowsum <- (sum(tab1[taxon,2:length(tab1[1,])]))  # sums values for given row
  halfper[taxon] <- as.numeric(rowsum/200)      # adds row sum divided by 200 to the vector
}


tab2 <- cbind(tab1, cbind(sums,halfper)) # creates a table with sums and 0.5% in the last two columns


names = as.vector(tab1[,1])  # creates vector with sequence names
tab3 <- data.frame(names)

temp <- c(mode = "numeric", length = length(tab2[,1]))
temp <- rep(0.0, length(tab2[,1]))
for (sample in c(2:length(tab1[1,]))){ # column numbers
  temp <- c(c(tab2[,sample]) - c(tab2[,length(tab2[1,])]))  # subtracts 0.5% from the values in the column
 
  tab3 <- data.frame(cbind(tab3, temp))  # adds new column with subtracted value to the table
}

colnames(tab3) <- colnames(tab1)

tab4 <- data.frame(matrix(ncol = length(tab1[1,]), nrow = length(tab1[,1])))  # creates a new empty table with the same size as the previous table
colnames(tab4) <- colnames(tab1)

tab4[,1] <- as.vector(tab1[,1])  # adds sequence names to the first column
for (sample in c(2:length(tab1[1,]))){ # column numbers
  for (taxon in c(1:length(tab1[,1]))){  # row numbers
    if(tab3[taxon,sample] > 0){   
      tab4[taxon,sample] <- round(tab3[taxon,sample], digits = 0)
    } else {
      tab4[taxon,sample] <- 0
    }
  
  }
}

write.table(tab4, "filtered-table-halfper.txt", sep="\t", row.names=FALSE, quote=FALSE)