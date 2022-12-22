# Big picture

![The setup for the FIT repo](fit-deploy-sketch.png)

1. Try out new changes in a feature branch off of main (or off of dev)
2. Merge changes into dev. Once merged in, use a github action to build the html pages and deploy them to 3.
3. The fit-dev repo is hosted on github pages. Navigate to noaa-fisheries-integrated-toolbox.github.io/fit-dev to preview the FIT website.
4. Once confirming the dev pages look good, merge changes into 4. Once merged in, use a github acion to build the html pages and deploy them to 5.
5. This is the production version of the NOAA fisheries site, advertised to the public.

# Webpage addresses on production

 - FIT landing page (https://noaa-fisheries-integrated-toolbox.github.io/ ; no change)
 - browse landing page (https://noaa-fisheries-integrated-toolbox.github.io/browse; new page)
 - individual drawer landing pages (if we still want these) (https://noaa-fisheries-integrated-toolbox.github.io/nmfs-fish-tools , for example; CHANGE from nmfs-fish-tools.github.io). 
 - individual tool landing pages, toolbox hosted (https://noaa-fisheries-integrated-toolbox.github.io/ASAP, for example; CHANGE from nmfs-fish-tools.github.io/ASAP)

 # redirect pages
 - will need the nmfs-fish-tools.github.io (and other org .io repos) to redirect; same with nmfs-fish-tools.github.io/toolname. Maybe just upload a new link to post for a bit.

# Org Templating

This repository includes templates and JSON data for the FIT. [python's jinja 2](https://zetcode.com/python/jinja/) is used to generate webpages from the html templates and JSON files (For R users, this approach is similar to using [glue](https://glue.tidyverse.org/)).

## How to update or add tool landing pages 
1. In [model_list_dir subfolder](https://github.com/noaa-fisheries-integrated-toolbox/toolbox_web_templating/tree/main/model_list_dir) add or update `.json` files (use [empty.json](https://github.com/noaa-fisheries-integrated-toolbox/toolbox_web_templating/blob/main/model_list_dir/EcoSys_model_list/empty.json) as a template if it’s a new tool). Examples of json are available in [model_list_dir/MODEL_LIST_NOTES.json](https://github.com/noaa-fisheries-integrated-toolbox/toolbox_web_templating/blob/main/model_list_dir/MODEL_LIST_NOTES.json)
2. If it is a new tool, add to the x_config.json file for the drawer it should be in.
3. In toolbox_web_templating [actions](https://github.com/noaa-fisheries-integrated-toolbox/toolbox_web_templating/actions), run the workflow "create html" for the drawer the new tool goes in 
4. Download the `index.html` created by the action (to find this, click into the action after it runs, the `index.html` will be at the bottom)
5. Replace the `index.html` in the github.io repo for whichever drawer the new tool is in: 
- [Fish and Fisheries](https://github.com/nmfs-fish-tools/nmfs-fish-tools.github.io)
- [Protected Species](https://github.com/NMFS-Protected-Species-Tools/nmfs-protected-species-tools.github.io) 
- [Human Dimensions](https://github.com/nmfs-human-dimensions-tools/nmfs-human-dimensions-tools.github.io)
- [Ecosystems](https://github.com/NMFS-ecosystem-tools/nmfs-ecosystem-tools.github.io)
- [General Modeling Tools](https://github.com/nmfs-general-modeling-tools/nmfs-general-modeling-tools.github.io)

Each landing page can be created using the correct config file.

# Explanation of JSON metadata
JSON data can be (partially) validated using [schema](https://json-schema.org/understanding-json-schema/about.html)
```json
{
  "active_development": true,     //in active development? true or false
  "NOAA_internal": false, //Maintained by NOAA? true or false.
  "associated_tools": [
    {"name":"NAME OF TOOL","link":"LINK TO TOOL"},
    {"name":"NAME OF TOOL","link":"LINK TO TOOL"}
  ],
  "authors": "First1 Last1 and First2 Last2",// **Name of the tool author or authors
  "background_text": "Information on this tool goes here and will be displayed on the tool page", //** Please Write up to a paragraph.
  "maintainer_email": "fisheries.toolbox@noaa.gov", //**Email for main contact. Please put a noaa.gov email address that someone will check.
  //Note: At least one of the 5 following links need to be filled out for your tool to be found. Please fill in as many as apply.
  "online_app_link": "", //IF THERE IS A SHINY APP OR OTHER ONLINE APP, PUT LINK HERE OTHERWISE LEAVE AS EMPTY QUOTES, no spaces.
  "executable_link": "", //**LINK TO DOWNLOAD APPLICATION IF EXE exists. Please leave blank if there is not an compiled exe distributed.
  "website_link": "", //**link to the website, if it exists; otherwise, leave blank.
  "documentation_link": "", //**LINK TO EXTERNAL DOCUMENTATION. Not necessary if it is the same as the website_link or source_code_link.
  "source_code_link": "", //LINK TO GITHUB CODE REPO
  "citation": "", //How to cite the package. Ideally an article with DOI.
  "tool_abbreviation": "MODABBREV", //SHORT ABBREVIATION OF TOOL USED AT TOP OF TILE ON LANDING PAGE. Must Match the name of the JSON file. Required.
  "tool_name": "Complete Name of Model Tool", //required
  "pdf_download": "", //A URL to a pdf that might be helpful for users.
  "release_badge":"NMFS-ecosystem-tools/MSCAA"//IF THE REPO UESE RELEASES ON GITHUB, JUST PUT THE ORG/REPO HERE TO LINK.
  "references": ["ref1", "ref2"], //** Formatted publication references. LEAVE AS EMPTY LIST [] IF NONE. Please include DOI if available.
  "shields_badges":["https://www.repostatus.org/badges/latest/active.svg","https://img.shields.io/badge/platform-linux%20%7Cwin-lightgrey"],//** add any extra badges here from repostatus or shields in a list
  "version_number": "",//** add version number only if it is not linked to a release_badge above
  "toolbox_drawer": ["fisheries", "general"], //** options are: "fisheries", "ecosystem", "human_dimensions", "protected_species", and "general"*. Put all that apply to the tool.
  "keywords": ["Economics", "R", "Web App"], //**keywords to sort through tools.,
  "user_organizations": ["SEFSC", "NWFSC", "SWFSC"] //operational users of the tool
```
