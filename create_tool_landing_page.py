# This script run once creates tool landing pages from a model_list_dir/*.json file.

# import argparse
import json
import os
import shutil
import sys
import requests

from jinja2 import Environment, FileSystemLoader

#basic templating
# use conda web_templating. .. source activate web_templating

def write_html(template, configs, new_dir, modelname, dev_or_prod_config):
    #root = os.path.dirname(os.path.abspath(__file__))
    #docsdir = os.path.join(new_dir, 'deploy')
    htmlname = modelname + '.html'
    filename = os.path.join(new_dir, htmlname)
    #if not os.path.exists(docsdir):
    #    os.mkdir(docsdir)
    with open(filename, 'w') as fh:
        fh.write(template.render(**configs, dev_or_prod_config = dev_or_prod_config))


def load_template():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('tool_landing_page.html')
    return template

# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('files')
#     args = parser.parse_args()
#     filename = args.files;
#     return filename

def write_templates(configs, new_dir, modelname, dev_or_prod_config):
    # filename = parse_args()
    template = load_template()
    write_html(template, configs, new_dir, modelname, dev_or_prod_config)

def run_all_files(list_of_models, folder_out, configdir, dev_or_prod_config):
    for modelname in list_of_models:
        print(modelname)
        old_name = modelname +'.json'
        configfile = os.path.join(configdir,old_name) 
        with open(configfile, "r") as read_file:
          configjson = json.load(read_file)
        # replace citation doi with formatted text string
        # nothing should be replaced if the citation doesn't start
        # with "https://doi.org"
        try:
          tmpcitation = configjson['citation']
          if tmpcitation.startswith("https://doi.org"):
            headers = {
              'Accept': 'text/x-bibliography; style=apa',
            }
            response = requests.get(configjson['citation'], headers=headers)
            # replace citation with the text string.
            # need to change the encoding (ISO-8859-1) to apparent_encoding (utf-8)
            response.encoding = response.apparent_encoding
            configjson['citation'] = response.text
        except:
          pass
        new_dir = os.path.join(folder_out)
        # Create target Directory if don't exist
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        write_templates(configjson, new_dir, modelname, dev_or_prod_config)
        


def main(dev_or_prod_config):
    with open("models_all.json", "r") as read_file:
        modellist_configjson = json.load(read_file)
    list_of_models = modellist_configjson['list_of_models']    
    folder_out= 'deploy'
    configdir= 'model_list_dir'
    run_all_files(list_of_models, folder_out, configdir, dev_or_prod_config)


if __name__ == '__main__':
    dev_or_prod_config = sys.argv[1]; # use this approach if we need to generate multiple files
    with open(dev_or_prod_config) as f:
            dev_or_prod_config =  json.load(f)
    main(dev_or_prod_config)
