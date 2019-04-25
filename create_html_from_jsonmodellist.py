from jinja2 import Environment, FileSystemLoader
import argparse
import json
import os
import shutil
#basic templating
# use conda web_templating. .. source avtivate web_templating




def write_html_index(template, configs, org_config):
    root = os.path.dirname(os.path.abspath(__file__))
    #root = pathto output directory
    filename = os.path.join(root, 'html', 'index.html')

    with open(filename, 'w') as fh:
        fh.write(template.render(configs = configs, org_config = org_config))


def load_template():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('index.html')
    return template



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files')
    args = parser.parse_args()
    filename = args.files;
    return filename




def write_templates(configs, org_config):
    # filename = parse_args()
    template = load_template()
    write_html_index(template, configs, org_config)




def main(location_of_model_list, list_of_models, org_config):
    allthemodels =  {}
    for f in list_of_models:
        old_name = f +'.json'
        print(f)
        filename = os.path.join(location_of_model_list, old_name)
        with open(filename) as ff:
            allthemodels[f] = json.load(ff)
            print(allthemodels[f])


    write_templates(allthemodels, org_config)





if __name__ == '__main__':
    location_of_model_list = '../model_landing_template'
    list_of_models =['2BOX','AGEPRO','AIM','ASAP','ASPIC',
            'CSA','DCAC','IRATE','KALMAN','MCOMP','MSE','POPSIM-A',
            'POPSIM-L','POPSIM','PSA','RIVARD','SCALE','SEINE','SRFIT',
            'STATCAM','VPA','VRD','YPR','YPRLEN']
    general_info_text = '''The NOAA Fish and Fisheries Toolbox  (Fish-Tools) is a collection of software programs and modeling tools which can be used in fishery stock assessments.  Many of the models are used in peer-reviewed stock assessments in the U.S. and globally.  A variety of fisheries stock assessment models as well as analytical and reporting tools are available, each of which uses a different type of estimation method to produce results.   The NOAA Fish and Fisheries Toolbox (Fish-Tools) is part of the NOAA Fisheries Integrate Toolbox (FIT).
    '''
    general_title= "Fish and Fisheries Tools"
    org_config = {'title':general_title, 'info':general_info_text, 'githubpage':'https://nmfs-fish-tools.github.io/'}


    main(location_of_model_list, list_of_models, org_config)

