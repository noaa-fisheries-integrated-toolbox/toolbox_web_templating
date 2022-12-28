# different approach, convert info from a Github issue into json.

library(gh)

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

