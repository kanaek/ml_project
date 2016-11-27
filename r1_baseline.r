# read files
df <- read.table("data/train.csv", sep=',', header=T)
store_item_nbrs <- read.table("model/store_item_nbrs.csv", sep=',', header=T)

# calculate log1p
df$log1p <- log1p(df$units)

# calculate days from 2012-01-01
origin <- as.integer(floor(julian(as.POSIXlt('2012-01-01'))))
df$date2j <- as.integer(floor(julian((as.POSIXlt(df$date))))) - origin



# exclude 2013-12-25
date_excl <- as.integer(floor(julian(as.POSIXlt('2013-12-25')))) - origin
df <- df[df$date2j != date_excl, ]

# for each item_nbr/store_nbrs, fitting by ppr function
df_fitted <- data.frame(date2j=c(), sno=c(), ino=c())

rng <- 1:nrow(store_item_nbrs)
df_fitted <- rbind(df_fitted)


write.table(df_fitted, "model/baseline.csv", quote=F, col.names=T, append=F, sep=",", row.names=F)

cat("curve fitting finished")

q("no")