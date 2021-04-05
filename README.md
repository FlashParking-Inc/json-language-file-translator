# json-language-file-translator
translates i18n json files to specified language

## system setup
install python 3 `brew install python3`

## app setup
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
add whatever *TRANSLATION.json* files to the *locales/en* directory you want to translate

### create translations
make sure your credential env variable is set (above)

    python3 main.py es
or whatever language (`es`, `it`, etc)

Your translated files will be in *locales/<language_specified>*