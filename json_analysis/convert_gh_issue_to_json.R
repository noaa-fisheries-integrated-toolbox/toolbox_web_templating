# Convert info from a Github issue into json. This is an important step #
# toward making the toolbox onboarding automated.

# Note this may be a bit out of date.
library(gh)
library(jsonlite)

issue_info <- gh("/repos/{owner}/{repo}/issues/{issue_number}",
owner = "noaa-fisheries-integrated-toolbox",
repo = "onboard-and-update",
issue_number = "1"
)
issue_body <- issue_info$body

# break up different form sections
issue_body <- strsplit(issue_body, "### ", fixed = TRUE)[[1]]
# break up headers from content
issue_body <- strsplit(issue_body, "\n\n", fixed = TRUE)

# rm no response components
issue_body <- lapply(issue_body, function(x) {
    nr <- grep("_No response_", x, fixed = TRUE)
    if(length(nr) > 0) {
       return(NULL)
    }
    x
})
# remove nulls and anything of length 0
issue_body <- issue_body[lengths(issue_body) != 0]

# convert the JSON component names
issue_body <- lapply(issue_body, function(x) {
    json_title <- tolower(x[1])
    json_title <- gsub(" ", "_",  json_title, fixed = TRUE)
    json_title <- gsub("(", "",  json_title, fixed = TRUE)
    json_title <- gsub(")", "",  json_title, fixed = TRUE)
    x[1] <- json_title
    x
})

# make names the title instead of a part of the list
names(issue_body) <- unlist(lapply(issue_body, function(x) x[1]))
issue_body <- lapply(issue_body, function(x) x[-1])

# Get rid of comments and code of conduct, not needed 
# in the json
issue_body$comments <- NULL
issue_body$code_of_conduct <- NULL

# Now make changes needed for specific elements to be correct in JSON.
# Then we may need some custom work to convert the arrays.

# Format boolean inputs
issue_body$active_development <-
  ifelse(issue_body$active_development == "Yes","true", "false")
issue_body$noaa_internal <- 
  ifelse(issue_body$noaa_internal == "Yes","true", "false")
issue_body$uses_github_releases <- 
  ifelse(issue_body$uses_github_releases == "Yes", "true", "false")

# format toolbox drawers and keywords
format_checkboxes <- function(original_checkboxes) {
    tmp_boxes <- strsplit(original_checkboxes, "\n", fixed = TRUE)[[1]]
    tmp_boxes <- grep("[X]", tmp_boxes, fixed = TRUE, value = TRUE)
    tmp_boxes <- strsplit(tmp_boxes, "- [X] ", fixed = TRUE)
    tmp_boxes <- unlist(lapply(tmp_boxes, function(x) x[2]))
    tmp_boxes
}

issue_body$toolbox_drawers <- 
  format_checkboxes(issue_body$toolbox_drawers)
issue_body$keywords <- 
  format_checkboxes(issue_body$keywords)

# format other array inputs


if(!is.null(issue_body$references)) {
    tmp_refs <- issue_body$references
    tmp_refs <- strsplit(tmp_refs, "(\\r)|(\\n)")[[1]]
    issue_body$references <- tmp_refs
}

if(!is.null(issue_body$associated_tools)) {
    tmp_tools <- issue_body$associated_tools
    tmp_tools <- strsplit(tmp_tools, ",", fixed = TRUE)[[1]]
    tmp_tools <- gsub("(\n)|(\r)", "", tmp_tools)
    tmp_tools <- strsplit(tmp_tools, " http", fixed = TRUE)
    tmp_tools <- lapply(tmp_tools, function(x) {
          x[2] <- paste0("http", x[2])
          names(x) <- c("name", "link")
          x <- as.list(x)
          x
       })
    issue_body$associated_tools <- tmp_tools
}

if(!is.null(issue_body$user_organizations)) {
    tmp_orgs <- issue_body$user_organizations
    tmp_orgs <- strsplit(tmp_orgs, ",\\s*")[[1]]
    issue_body$user_organizations <- tmp_orgs
}

if(!is.null(issue_body$software_badges)) {
    tmp_badges <- issue_body$software_badges
    tmp_badges <- strsplit(tmp_badges, ",\\s*")[[1]]
    issue_body$software_badges <- tmp_badges
}

# mark singletons before converting to JSON
issue_body$active_development <- unbox(issue_body$active_development)
issue_body$tool_name <- unbox(issue_body$tool_name)
issue_body$tool_abbreviation <- unbox(issue_body$tool_abbreviation)
issue_body$authors <- unbox(issue_body$authors)
issue_body$noaa_internal <- unbox(issue_body$noaa_internal)
issue_body$maintainer_name <- unbox(issue_body$maintainer_name)
issue_body$maintainer_email <- unbox(issue_body$maintainer_email)
issue_body$background_text <- unbox(issue_body$background_text)
issue_body$citation <- unbox(issue_body$citation)
issue_body$online_app_link <- unbox(issue_body$online_app_link)
issue_body$executable_link <- unbox(issue_body$executable_link)
issue_body$website_link <- unbox(issue_body$website_link)
issue_body$documentation_link <- unbox(issue_body$documentation_link)
issue_body$source_code_link <- unbox(issue_body$source_code_link)
issue_body$pdf_download_link <- unbox(issue_body$pdf_download_link)
issue_body$uses_github_releases <- unbox(issue_body$uses_github_releases)
issue_body$static_version_number <- unbox(issue_body$static_version_number)

# to write to a file:
#jsonlite::write_json(issue_body, "test.JSON", pretty = TRUE)

markdown_txt <- paste(
  "Thanks for submitting a tool onboarding request! Below is the JSON equivalent of your responses:"
  "```",
  jsonlite::toJSON(issue_body, pretty = TRUE),
  "```", sep = "\n"
)

# post json as a comment on the issue
gh("POST /repos/{owner}/{repo}/issues/{issue_number}/comments",
   owner = "noaa-fisheries-integrated-toolbox",
   repo = "onboard-and-update",
   issue_number = 1,
   body = markdown_txt)
