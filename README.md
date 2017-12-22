## Flask Finder  
Inventory search for laboratories, developed for use in a large R1 state 
university teaching lab. Intended to be used as a search kiosk on a 
raspberry pi. Includes toggles for searching chemicals, stock, and
equipment separately.  
Written using flask, pandas, and sqlite3. Can be hosted locally or on the web.

# Preparation
Fill in inventories in a .csv file, in `/db` (more verbose README located here), run the `update_*.sh` scripts to store a dated copy of the current inventory and fill a sqlite database.

# Use
Run `flask_search_kiosk.py`, open the web browser and point it at the adress flask runs the web app on (typically `127.0.0.1:5000`). 