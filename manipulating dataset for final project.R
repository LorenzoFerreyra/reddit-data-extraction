library(tidyverse)
library(jsonlite)
library(writexl)

data <- stream_in(file("devsarg.json"))

#data <- as.data.frame(data)

df <- as_tibble(data)
df <- tibble(
  post_id = data$id,
  title = data$title,
  score = data$score,
  url = data$url,
  created = data$created,
  body = data$body,
  comments = data$posts
)

write_xlsx(data, "devsarg.xlsx")