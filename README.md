### For  linux and mac
1. Generate .env file with:
- API_KEY=key
- ENC_KEY=enc_key
- PATH_TO_OBSIDIAN=Path/to/vault
- SLOT=
- ZIPD_FOLDER_NAME_ENV=
- URL1=
- URL2=
2.
run ./pyhton_venv_install.sh
3. run bin/python3 run.py

### For Windows
1.https://www.c-sharpcorner.com/article/how-to-install-python-3-8-in-windows/
2. https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
2:
virtualenv --python C:\Path\To\Python\python.exe venv
.\venv\Scripts\activate
- pip3 install -r requirements.txt
3.create .env file with following
- API_KEY=key
- ENC_KEY=enc_key
- PATH_TO_OBSIDIAN=Path/to/vault
- SLOT=
- ZIPD_FOLDER_NAME_ENV=
- URL1=
- URL2=
4.run run.py
