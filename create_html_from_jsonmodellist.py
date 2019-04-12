from jinja2 import Environment, FileSystemLoader
import argparse
import json
import os
import shutil
#basic templating




def write_html_index(template, configs):
    root = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(root, 'html', 'index.html')

    with open(filename, 'w') as fh:
        fh.write(template.render(configs = configs))


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




def write_templates(configs):
    # filename = parse_args()
    template = load_template()
    write_html_index(template, configs)




def main():

    list_of_models =['2BOX','AGEPRO','AIM','ASAP','ASPIC','ATL',
            'CSA','DCAC','IRATE','KALMAN','MCOMP','MSE','POPSIM-A',
            'POPSIM-L','POPSIM','PSA','RIVARD','SCALE','SEINE','SRFIT',
            'SS','STATCAM','VPA','VRD','YPR','YPRLEN']


    allthemodels =  {}
    for f in list_of_models:
        old_name = f +'.json'
        print(f)
        filename = os.path.join('../model_landing_template', old_name)
        with open(filename) as ff:
            allthemodels[f] = json.load(ff)


    write_templates(allthemodels)





if __name__ == '__main__':
    main()

