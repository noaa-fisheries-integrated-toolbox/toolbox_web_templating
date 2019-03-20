from jinja2 import Environment, FileSystemLoader
import argparse
import json
import os
#basic templating




def write_html_index(template, configs):
    root = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(root, 'html', 'index.html')
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






def main():
    filename = parse_args()
    configs = load_file_parse(filename)
    template = load_template()
    write_html_index(template, configs)







if __name__ == '__main__':
    main()

