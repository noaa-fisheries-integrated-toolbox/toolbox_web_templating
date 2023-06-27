# Big picture, GitHub Branching

![The setup for the FIT repo](fit-deploy-sketch.png)

1. Try out new changes in a feature branch off of dev.
2. Merge changes into dev. Once merged in, use a github action to build the html pages and deploy them to 3.
3. The fit-dev repo is hosted on github pages. Navigate to noaa-fisheries-integrated-toolbox.github.io/fit-dev to preview the FIT website.
4. Once confirming the dev pages look good, merge changes into 4 (for small changes, can consider squashing or rebasing instead). Once merged in, use a github action (done automatically) to build the html pages and deploy them to 5. Delete the dev branch and recreate it from (so that they are back in sync with the exact same commits).
5. This is the production version of the NOAA fisheries site, advertised to the public.

# Webpage addresses on production

 - FIT landing page (https://noaa-fisheries-integrated-toolbox.github.io/ ; no change)
 - individual tool landing pages, toolbox hosted (https://noaa-fisheries-integrated-toolbox.github.io/ASAP, for example; CHANGE from nmfs-fish-tools.github.io/ASAP)

 # redirect pages
 - will need the nmfs-fish-tools.github.io (and other org .io repos) to redirect; same with nmfs-fish-tools.github.io/toolname. These redirect automatically or have a redirect link.

# Org Templating

This repository includes templates and JSON data for the FIT. [python's jinja 2](https://zetcode.com/python/jinja/) is used to generate webpages from the html templates and JSON files (For R users, this approach is similar to using [glue](https://glue.tidyverse.org/)).

## How to update or add tool landing pages 
1. In [model_list_dir subfolder](https://github.com/noaa-fisheries-integrated-toolbox/toolbox_web_templating/tree/main/model_list_dir) add or update `.json` files. Examples of json are available in the readme. If onboarding a new tool, the issue from [the onboard-and-update repo](https://github.com/noaa-fisheries-integrated-toolbox/onboard-and-update) should have a json based on user input that can be copy/pasted in, then checked.
2. If it is a new tool, add the name of the json file (minus the extension, case sensitive) to the list_of_models item in the models_all.json file.
3. Changes can be checked locally using instructions in the "Creating Webpages Locally From Templates"
4. After committing and pushing to dev, changes can be checked on the [fit-dev](https://noaa-fisheries-integrated-toolbox.github.io/fit-dev/) site. If GitHub actions are failing, look at them and make changes.
5. Once actions passing, share changed dev tool landing page with the person submitting the(e.g., if the tool is called, my-tool, the address would be https://noaa-fisheries-integrated-toolbox.github.io/fit-dev/my-tool). Allow them to request changes. 
6. If the author approves, open an PR to main, which KD will look at and merge in if passing checks.

# Explanation of JSON metadata
JSON data can be validated using [schema](https://json-schema.org/understanding-json-schema/about.html)
```json
{
  "active_development": true,     //in active development? true or false
  "noaa_internal": false, //Maintained by NOAA? true or false.
  "associated_tools": [
    {"name":"NAME OF TOOL","link":"LINK TO TOOL"},
    {"name":"NAME OF TOOL","link":"LINK TO TOOL"}
  ],
  "authors": "First1 Last1 and First2 Last2",// **Name of the tool author or authors
  "background_text": "Information on this tool goes here and will be displayed on the tool page", //** Please Write up to a paragraph.
  "maintainer_email": "fisheries.toolbox@noaa.gov", //**Email for main contact. Please put a noaa.gov email address that someone will check.
  //Note: At least one of the 5 following links need to be filled out for your tool to be found. Please fill in as many as apply.
  "online_app_link": "https://some.link.noaa.gov", //IF THERE IS A SHINY APP OR OTHER ONLINE APP, PUT LINK HERE OTHERWISE leave out this element.
  "executable_link": "https://some.link.noaa.gov", //**LINK TO DOWNLOAD APPLICATION IF EXE exists. Leave out this element if exe does not exist
  "website_link": "https://some.link.noaa.gov", //**link to the website, if it exists; otherwise, leave out.
  "documentation_link": "https://some.link.noaa.gov", //**LINK TO EXTERNAL DOCUMENTATION. Leave element out if does not exist or link is already entered elsewhere (e.g., on the website)
  "source_code_link": "https://github.com/org/repo", //LINK TO GITHUB CODE REPO, if exists.
  "citation": "https://doi.org/10.32614/RJ-2012-002", //How to cite the package. Ideally an article with DOI.
  "tool_abbreviation": "MODABBREV", //SHORT ABBREVIATION OF TOOL USED AT TOP OF TILE ON LANDING PAGE. Must Match the name of the JSON file. Required.
  "tool_name": "Complete Name of Model Tool", //required
  "pdf_download_link": "https://somelink.org/my.pdf", //A URL to a pdf that might be helpful for users.
  "release_badge":"NMFS-ecosystem-tools/MSCAA"//IF THE REPO UESE RELEASES ON GITHUB, JUST PUT THE ORG/REPO HERE TO LINK.
  "references": ["ref1", "ref2"], //** Formatted publication references.Please include DOI if available.
  "software_badges":["https://www.repostatus.org/badges/latest/active.svg","https://img.shields.io/badge/platform-linux%20%7Cwin-lightgrey"],//** add any extra badges here from repostatus or shields in a list
  "static_version_number": "1.0.0",//** add version number only if it is not using github releases and the version is unlikely to change. Omit this element if not used.
  "toolbox_drawers": ["Fish and Fisheries", "General Modeling and Productivity Tools"], //** options are: "Fish and Fisheries", "Ecosystem"", "Human Dimensions", "Protected Species", and "General Modeling and Productivity Tools"*. Put all that apply to the tool.
  "keywords": ["Economics", "R", "Web App"], //**keywords to sort through tools.,
  "user_organizations": ["SEFSC", "NWFSC", "SWFSC"] //operational users of the tool
```

# Creating Webpages Locally From Templates

Python and Jinja2 need to be installed locally.
```
pip install jinja2
```

From bash, run:

```
python create_tool_landing_page.py
python create_catalog_landing_page.py dev_config.json # or prod_config.json if building the production site.
```

These are just the commands in `create_html`.yml. Note that this will create new webpages that should NOT be saved to the repository.

To view the webpages from VS code, try using the Live Preview Extension.
You may need to add .html to the end of a link in order to view it properly. Sometimes the 
embedded preview doesn't work, so a separate browser window will need to be opened instead.