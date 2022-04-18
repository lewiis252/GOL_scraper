# Gry_Online_News_Scraper
This app will automaticaly download and sent news fromgry-online.pl. You need python and packages from requirements.txt to run it. 
This script automatically sent files from files_to_sent folder to your kindle and move sended files to sended folder.
**Just provide your mail, kindle's mail and password** in .env file (look below).
Remember, you must do something like **Turn Allow less secure apps to ON in your email service** (gmail in this example)

## Requirements
``` sh
pip install -r requirements.txt
```

## Usage of scraper

```sh
git clone git@github.com:lewiis252/GOL_scraper.git
```

After setting your virtual enviroment you must provide your emails and password - create .env file in spiders directory and fill it like this:

```sh
# login settings
sender_email = 'my_email.com'
receiver_email = 'my_device_mail@kindle.com'
password = 'passsword'
```

Then simply run gol_scraper.py.

