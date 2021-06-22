# json-language-file-translator
translates i18n json files to specified language using the Google Cloud Translate API (Basic).

## features
- translates multiple json files at once
- support for hierarchical translation files
- will look for translations that are already present before calling API

## system setup
install python 3 `brew install python3`

## app setup (in app directory)

### setup a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

### install dependencies
    pip3 install -r requirements.txt

### Google API credentials
- setup google authentication for app https://cloud.google.com/translate/docs/setup#creating_service_accounts_and_keys
- after you download key file: `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/google-credentials.json"`

## run app
### translation files
add whatever *TRANSLATION.json* files to the *locales/en* directory you want to translate, as well as *locales/target* files/translations you don't want overwritten (it checks if translations already exist).

### create translations
make sure your credential env variable is set (above)

    python3 main.py es
or whatever language (`es`, `it`, etc)

## notes
- Your translated files will be in *locales/<language_specified>/*
- If there is already a translation for that string (an already existing matching language, file, and key) then that will be used, and no API call will be made. Delete the translated files from the target directory if you don't want this.

