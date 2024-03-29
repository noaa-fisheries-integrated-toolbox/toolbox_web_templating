# This script run once creates a catalog landing page based on the *_config.json file 
# reference when called. E.g., python create_catalog_landing_page.py EcoSys_config.json
from jinja2 import Environment, FileSystemLoader
# import argparse
import json
import os
import shutil
import sys
#basic templating
# use conda web_templating. .. source activate web_templating

def write_html_index(template, configs, org_config):
    root = os.path.dirname(os.path.abspath(__file__))
    #root = path to output directory
    filename = os.path.join(root, 'deploy', 'site-index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(configs = configs, org_config = org_config))

def load_template():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('site_index_template.html')
    return template

# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('files')
#     args = parser.parse_args()
#     filename = args.files;
#     return filename

def write_templates(configs, org_config):
    # filename = parse_args()
    template = load_template()
    write_html_index(template, configs, org_config)

def main(org_config, model_config):
    allthemodels =  {}
    for f in model_config['list_of_models']:
        old_name = f +'.json'
        #print(os.getcwd())
        filename = os.path.join(model_config['location_of_model_list'], old_name)
        with open(filename) as ff:
            allthemodels[f] = json.load(ff)
            #print(allthemodels[f])
    write_templates(allthemodels, org_config)

if __name__ == '__main__':
    org_config_file = sys.argv[1]; # use this approach if we need to generate multiple files
    with open(org_config_file) as f:
            org_config =  json.load(f)
    with open("models_all.json") as f:
            model_config =  json.load(f)
            model_config['list_of_models'].sort(key=lambda x: x.lower())
    main(org_config, model_config)
