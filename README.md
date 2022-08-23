# Org Templating

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
