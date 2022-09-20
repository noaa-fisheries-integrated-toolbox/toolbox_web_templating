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



def run_all_files(list_of_models, folder_out, configdir):
    for modelname in list_of_models:
        print(modelname)
        old_name = modelname +'.json'
        configfile = os.path.join(configdir,old_name)
        # shutil.copy(old_name, 'config_template.json')
        new_dir = os.path.join(folder_out, modelname)
        # Create target Directory if don't exist
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        write_templates(configfile, new_dir)


def write_templates(filename, new_dir):
    # filename = parse_args()
    configs = load_file_parse(filename)
    template = load_template()
    write_html_index(template, configs, new_dir)
    staticdir = os.path.join(new_dir,'docs','static')
    if os.path.exists:
        shutil.rmtree(staticdir)
    shutil.copytree('./templates/static', staticdir)
    # shutil.copy('./templates/README.MD',new_dir)
    # shutil.copy('./templates/LICENSE.MD',new_dir)



def main():
    which_type_models = 'gen_models'
    if which_type_models == 'legacy':
    #for legacy:
        #list_of_models = ['2BOX']
        list_of_models =['2BOX','AGEPRO','AIM','ASAP','ASPIC',
                'CSA','DCAC','IRATE','KALMAN','MCOMP','MSE','POPSIM-A',
                'POPSIM-L','POPSIM','PSA','RIVARD','SCALE','SEINE','SRFIT',
                 'STATCAM','VPA','VRD','YPR','YPRLEN']
        folder_out= './nmfs-fish-tools/legacy_models'
        configdir= './nmfs-fish-tools/model_list/'
    elif which_type_models == 'new_fish':
    #new models :
        list_of_models = ["RMAS"]
        # list_of_models = ["GMACS","RMAS","WHAM"]

        folder_out= './nmfs-fish-tools'
        configdir= './model_list/'

    elif which_type_models == 'gen_models':
    #gen models:
        list_of_models = ['nmfspalette']
        folder_out= './nmfs-general-modeling-tools'
        configdir= './nmfs-general-modeling-tools/model_list/'
    elif which_type_models == 'eco_models':
    #gen models:
        #list_of_models = ['MSCAA','MSSPM','MSVPA_X2']
        list_of_models = ['DONUT']
        #list_of_models = ['MSSPM']
        folder_out= './nmfs-ecosystem-tools'
        configdir= './nmfs-ecosystem-tools/model_list/'

    run_all_files(list_of_models, folder_out, configdir)





if __name__ == '__main__':
    main()

