from jinja2 import Environment, FileSystemLoader
import argparse
import json
import os
import shutil
#basic templating




def write_html_index(template, configs, new_dir):
    #root = os.path.dirname(os.path.abspath(__file__))
    docsdir = os.path.join(new_dir, 'docs')
    filename = os.path.join(new_dir, 'docs', 'index.html')
    if not os.path.exists(docsdir):
        os.mkdir(docsdir)
    with open(filename, 'w') as fh:
        fh.write(template.render(**configs))


def load_template():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('index.html')
    return template




def load_file_parse(fi):
    with open(fi) as f:
        configs = json.load(f)
        return configs



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files')
    args = parser.parse_args()
    filename = args.files;
    return filename



def run_all_files():
    # list_of_models =['2BOX','AGEPRO','AIM','ASAP','ASPIC','ATL',
    #         'CSA','DCAC','IRATE','KALMAN','MCOMP','MSE','POPSIM-A',
    #         'POPSIM-L','POPSIM','PSA','RIVARD','SCALE','SEINE','SRFIT',
    #         'SS','STATCAM','VPA','VRD','YPR','YPRLEN']
    list_of_models = ['2BOX']
    for modelname in list_of_models:
        old_name = modelname +'.json'
        # shutil.copy(old_name, 'config_template.json')
        new_dir = '../../legacy_models/' + modelname
        # Create target Directory if don't exist
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        write_templates(old_name, new_dir)


def write_templates(filename, new_dir):
    # filename = parse_args()
    configs = load_file_parse(filename)
    template = load_template()
    write_html_index(template, configs, new_dir)
    staticdir = os.path.join(new_dir,'docs','static')
    shutil.copy('./templates/static', staticdir)
    shutil.copy('./templates/README.MD',staticdir)
    shutil.copy('./templates/LICENSE.MD',staticdir)



def main():
    run_all_files()





if __name__ == '__main__':
    main()

