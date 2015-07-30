# SQL-Sentry-API

## Setup and Installation

1) Download or clone this Repo onto a local machine with access to your SQL Sentry database.  
2) Install Python 3.4 EXACTLY as detailed @ http://www.howtogeek.com/197947/how-to-install-python-on-windows/
3) Install dependancies: open an admin command prompt:
```
pip install flask
pip install pymssql
```
4) Modify config.json and set hostname and db as the SQL Instance hostname and SQLSentry database name respectively.
5) Run 'run.py' as a Windows user with read access to your SQLSentry Database

## Security info

This API exposes data from your SQLSentry Database.  Please see config.json SELECT statments for what data will be exposed.
UNDER NO CIRCUMSTANCES will any writes / updates / other data alterations be sent to your SQLSentry DB.  It is recommended that the user not even have write access to the DB.

##Troubleshooting

If you have trouble, feel free to email admin[at]redspin[dot]net

## License Agreement

This is software is provided as-is.  It is not supported, endorsed, or maintained by SQL Sentry, LLC.  It's an open source third party API intended to be hosted on-prem.