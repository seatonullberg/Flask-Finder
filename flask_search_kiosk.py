#!/usr/bin/env python3

__author__	= "Kyle Chesney"

from flask import *
import sqlite3
import pandas as pd

app = Flask(__name__)
conn = sqlite3.connect('db/inv.db', check_same_thread = False)
c = conn.cursor()


def search(phrase, option):
    results = []
    if option == "chem": 
        cmd = ("SELECT Name, "
        "Quantity, "
        "Unit, "
        "Location, "
        "Sublocation "
        "FROM chem "
        "WHERE Name LIKE ?")
        columns=["Name", "Quantity", "Unit", "Location", "Shelf"]
    elif option == "stock":
        cmd = ("SELECT Name, "
        "Quantity, "
        "Form, "
        "Location, "
        "Sublocation, "
        "Layer "
        "FROM stock "
        "WHERE Name LIKE ?")
        columns = ["Name", "Quantity", "Form", "Location", "Sublocation",
        "Shelf"]
    elif option == "equip":
        print("Not implemented")
        cmd = ""
    # Sanitize sql queries
    for result in c.execute(cmd, ['%' + phrase + '%']):
        results.append(result)
    return pd.DataFrame(results, columns=columns)


@app.route("/")
def main():
    return render_template('view.html')


@app.route("/", methods=['POST'])
def do_search():
    option = str(request.form['sub_db'])
    phrase = str(request.form['phrase'])
    df = search(phrase, option)
    ### Styling effects
    df.set_index(['Name'], inplace=True)
    df.index.name = None
    ###
    return render_template('view.html',
            tables = [df.to_html()]) # Presented as list to allow multisearch


if __name__ == "__main__":
    app.run(debug=True)

