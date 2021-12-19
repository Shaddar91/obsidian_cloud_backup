import tkinter as tk   
import zipfile;import os;import requests
from dotenv import load_dotenv
load_dotenv()
api_key                =os.environ.get("API_KEY")
enc_key             =os.environ.get("ENC_KEY")
path_to_obsidian_env   =os.environ.get("PATH_TO_OBSIDIAN")
slot_number_env        =os.environ.get("SLOT")
zipd_folder_name_env   =os.environ.get("ZIPD_FOLDER_NAME_ENV")
url                = os.environ.get("URL1")
url2               = os.environ.get("URL2")
params_for_post = {
    "apikey": api_key,
    "key" : enc_key,
    "slot" : slot_number_env,
    "data" : zipd_folder_name_env
}

params_for_get = {
    "apikey": api_key,
    "key" : enc_key,
    "slot" : slot_number_env
}


def zipfolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername, 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir)
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

def unzip_file(var_file):
    with zipfile.ZipFile(var_file,"r") as zip_ref:
        zip_ref.extractall("test_folder")
#############################

def backup(zipd_folder_name, path_to_obsidian, url, params):
    zipfolder(zipd_folder_name_env, path_to_obsidian_env)
    post_shit = requests.post(url, params_for_post)
    print(post_shit)

def pull():
    with requests.get(url2, params_for_get, stream=True) as r:
        r.raise_for_status()
        with open(zipd_folder_name_env, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return zipd_folder_name_env
        
#####################
def backup_btn():
    backup(zipd_folder_name_env, path_to_obsidian_env, url, params_for_post)

def unzip_btn():
    pull()
    unzip_file(zipd_folder_name_env)

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

backup_button= tk.Button(frame, 
                   text="backup", 
                   command=backup_btn
                   )

pull_disp= tk.Button(frame, 
                   text="pull", 
                   command=unzip_btn
                   )

exit_button = tk.Button(frame,
                   text="Exit",
                   fg="green",
                   command=quit)


backup_button.pack(side=tk.LEFT)
pull_disp.pack(side=tk.LEFT)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()


