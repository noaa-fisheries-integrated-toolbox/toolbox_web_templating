#conda activate simple
import pandas as pd
import json




def into_pandas(f):
    df = pd.read_csv(f);
    headers = [
      "tool_name",
      "model_abbrev",
      "model_type",
      "author_name",
      "background_text",
       "references",
      "online_app_link",
      "download_app_link",
      "code_repository_link",
      "version_number",
      "pdf_download",
      "badge_level",
      "suport_level",
      "documentation_link",
      "associated_tools"
    ]


    new_df= pd.DataFrame(columns = headers)
    new_df.tool_name = df.Model
    new_df.model_abbrev = df['Unnamed: 1']
    new_df.version_number = df.Version
    new_df.author_name = df.Author
    for index, row in new_df.iterrows():
        print(row)
        if row.model_abbrev:
            write_to_json(row)



def write_to_json(x):

    fn = x.model_abbrev.strip('()') + ".json"
    with open(fn, 'w') as f:
        json.dump(x.to_json(), f, ensure_ascii=False)






def main():
    filename = 'toolbox_survey_tally.csv'
    into_pandas(f)




if __name__ == '__main__':
    main()

