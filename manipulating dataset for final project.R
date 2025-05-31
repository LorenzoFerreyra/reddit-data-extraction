library(tidyverse)
library(jsonlite)
library(writexl)

data <- stream_in(file("devsarg.json"))

data <- as.data.frame(data)

data <- as_tibble(data)
# to_excel 

write_xlsx(data, "###devsarg.xlsx")