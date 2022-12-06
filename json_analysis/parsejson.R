# Code to parse json to get keywords

get_keywords <- function() {
    files <- list.files(path = "model_list_dir", full.names = TRUE)
    files <- grep("\\.json$", files, value = TRUE)

    jsoninfo <- lapply(files, function(x) jsonlite::fromJSON(x))
    # extract just the keywords
    keywords <- lapply(jsoninfo, function(x) x[["keywords"]])
    keywords <- unlist(keywords)
    # rm dups from the keywords and alphabetize
    keywords <- sort(unique(keywords))
    write.table(keywords, file.path("json_analysis","keywords.txt"), row.names = FALSE,
    col.names = FALSE)
}

get_keywords()
