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

get_html_snippet <- function() {
    files <- list.files(path = "model_list_dir", full.names = TRUE)
    files <- grep("\\.json$", files, value = TRUE)

    jsoninfo <- lapply(files, function(x) jsonlite::fromJSON(x))
    # extract just the keywords
    keywords <- lapply(jsoninfo, function(x) x[["keywords"]])
    keywords <- unlist(keywords)
    # rm dups from the keywords and alphabetize
    keywords <- sort(unique(keywords))
    # create the html snippits
    snippet <- paste0('<input type="button" value="', keywords, '" onclick="simpleSearch(this.value)">')
    gh_form_snippet <- paste0('- label: "', keywords, '"')
    write.table(snippet, file = file.path("json_analysis", "keywords_html_snippet.txt"), 
    row.names = FALSE, col.names = FALSE, quote = FALSE)
    write.table(gh_form_snippet, file = file.path("json_analysis", "keywords_gh_form_snippet.txt"), 
    row.names = FALSE, col.names = FALSE, quote = FALSE)
}

get_keywords()

get_html_snippet()
