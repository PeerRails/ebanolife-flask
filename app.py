from flask import Flask
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import random

# AIzaSyDVMKjM5bLNnAl0NOJwvcMvviqchRf9kWo 

def load_worksheet():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GS_CREDENTIALS_JSON'], scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key(os.environ['GC_KEY']).get_worksheet(0)
    values_list = wks.col_values(1)
    return values_list

def process_list(values_list):
    new_list = list(filter(None, values_list))
    return random.choice( new_list )

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ebano")
def get_src():
    src = process_list( load_worksheet() )
    return src

