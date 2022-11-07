# Big picture

![The setup for the FIMS repo](fit-deploy-sketch.png)

1. Try out new changes in a feature branch off of main (or off of dev)
2. Merge changes into dev. Once merged in, use a github action to build the html pages and deploy them to 3.
3. The fit-dev repo is hosted on github pages. Navigate to noaa-fisheries-integrated-toolbox.github.io/fit-dev to preview the FIMS website.
4. Once confirming the dev pages look good, merge changes into 4. Once merged in, use a github acion to build the html pages and deploy them to 5.
5. This is the production version of the NOAA fisheries site, advertised to the public!

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
Explanation:

{
  "associated_tools": [
    {"name":"NAME OF TOOL","link":"LINK TO TOOL"},
    {"name":"NAME OF TOOL","link":"LINK TO TOOL"}
  ],
  "author_name": "AUTHOR NAME",
  "background_text": "THIS TEXT WILL BE THE MAIN TEXT ON THE MODEL LANDING PAGE",
  "badge_level": "",** for the most part this is no longer used but can be left in older ones
  "contact":"EMAIL FOR MAIN CONTACT use fisheries.toolbox@noaa.gov if no other email is known",
  "documentation_link": "LINK TO EXTERNAL DOUMENTATION OR LOCAL PATH TO FILE WITH DOCUMENTATION",
  "download_app_link": "LINK TO DOWNLOAD APPLICATION IF EXE OR RELEASE VERSION, CAN JUST USE LINK TO RELEASE PAGE",
  "github_link": "LINK TO GITHUB CODE REPO",
  "model_abbrev": "SHORT ABBREVIATION OF TOOL USED AT TOP OF TILE ON LANDING PAGE",
  "model_name": "COOMPLETE NAME OF TOOL SHOWN IN TILE ON SECOND ROW",
  "model_type": "SPECIFIY TYPE OF MODEL< THIS SHOWS UP IN THE TILE OR CAN BE LEFT AS JUST EMPTY QUOTES",
  "model_link_page":"LINK TO LANDING PAGE FOR TOOL, IF EMPTY WILL BE FILLED IN BY THE CURRENT ORG GITHUB.IO page.",
  "online_app_link": "IF THERE IS A SHINY APP OR OTHER ONLINE VERSION PUT LINK HERE OTHERWISE LEAVE AS EMPTY QUOTES, no space",
  "pdf_download": "",
  "release_badge":"IF THE REPO UESE RELEASES ON GITHUB, JUST PUT THE ORG/REPO HERE TO LINK. IF ITS A TAG AND NOT A RELEASE YOU MAY NEED TO MAKE A FIX DIRECTLY IN THE HTML AFTER THE FACT  , EXAMPLE FOR RELEASES: NMFS-ecosystem-tools/MSCAA",
  "references": ["ref1", "ref2"],**LEAVE AS EMPTY LIST [] IF NONE
  "support_level": "external_active",** CHOICES ARE external_active OR internal_active OR interal_inactive
  "tool_type":"SPECIFIY TYPE OF TOOL ( MORE GENERAL THEN MODEL) THIS SHOWS UP IN THE TITLE OR CAN BE LEFT AS JUST EMPTY QUOTES",
  "shields_badges":["https://www.repostatus.org/badges/latest/active.svg","https://img.shields.io/badge/platform-linux%20%7Cwin-lightgrey"],** add any extra badges here from repostatus or shields in a list
  "version_number": "0.9.0",** add version number only if it is not linked to a release_badge above
  "toolbox_drawer": ["fisheries", "general"], ** options are: "fisheries", "ecosystem", "human_dimensions", "protected_species", and "general"**
  "keywords": ["Economics", "R", "Web App"] **keywords to sort through tools**
}
```
