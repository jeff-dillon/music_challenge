# music_challenge

## Code Louisville Coding Challenge

Your client is building analytics for a music app and wants you to add some functionality to an existing python script. The script currently has the following analytics functions:
* get_tracks() returns a DataFrame with all of the available Tracks in the database
* get_genres() returns a DataFrame with all of the available Genres in the database
* get_tracks_by_genre() returns a DataFrame with all of the Tracks in a given Genre

### Challenge: Add the following functions.
* get_playlists() return a DataFrame with all of the Playlists in the datbase
* get_tracks_by_playlist() - return a DataFrame with all of the Tracks in a given Playlist

### Bonus: Add the following features.
* get_genres_by_playlist() returns a DataFrame with the distinct Genres in a given playlist. 
    - Example Input: "Heavy Metal Classic" 
    - Example Output: Rock, Metal, Heavy Metal
* Print out the total # of Tracks by Genre.
    - You can do this in using Pandas querying the get_tracks() dataframe
    - You can do this in SQL by writing a new SQL query
* get_top_ten_artists_by_sales() returns a DataFrame with the top 10 artists by total sales
    - Sales are calculated by summing the product of the UnitPrice with the Quantity in the invoice_items table

## Database Diagram

![database diagram](sqlite-sample-database-color.jpg)

You can test queries using an online version of this database here:
[SQLite Tutorial](https://www.sqlitetutorial.net/tryit/)

## Instructions

1. create a virtual environment `python -m venv venv`
2. activate the virtual environment `source venv/bin/activate` or `venv\Scripts\activate.bat`
3. install the required packages `pip install -r requirements.txt`
4. add your code to the `challenge.py` file
