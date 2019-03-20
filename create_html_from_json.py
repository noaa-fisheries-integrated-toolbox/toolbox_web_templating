import jinja2
import argparse
import json
#basic templating






















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
    print(configs)
    print(configs['model_name'])







if __name__ == '__main__':
    main()

