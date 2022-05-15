"""
Music Challenge
"""
import sys
import os
import sqlite3
import pandas as pd

def create_connection(db_file:str) -> sqlite3.Connection:
    """
    create connection to sqlite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as sql_error:
        print(sql_error)

    return conn

def get_genres(conn:sqlite3.Connection) -> pd.DataFrame:
    """
    Get the list of Genres from the database
    :param: conn: connection to database
    :return: all genres
    """
    return pd.read_sql_query("SELECT * FROM genres", conn)


def get_tracks_by_genre(genre_id:int, conn:sqlite3.Connection) -> pd.DataFrame:
    """
    Get the list of tracks by Genre
    :param: genre_id: the ID of the genre
    :param: conn: connection to database
    :return: all tracks in the specified genre
    """
    sql_query = """
        SELECT t.trackID, t.Name, t.Composer
        FROM tracks t
        INNER JOIN genres g ON t.GenreId = g.GenreId
        WHERE g.GenreId = ?
    """
    return pd.read_sql_query(sql_query, conn, params=(genre_id, ))


def get_tracks(conn:sqlite3.Connection) -> pd.DataFrame:
    """
    Get a list of all tracks
    :param: conn: connection to database
    :return: all tracks in the database
    """
    sql_query = """
        SELECT t.trackID, t.Name as TrackName, t.Composer, 
                g.Name as GenreName, a.Title as AlbumTitle
        FROM tracks t
        INNER JOIN genres g ON t.GenreId = g.GenreId
        INNER JOIN albums a ON t.AlbumId = a.AlbumId
    """
    return pd.read_sql_query(sql_query, conn)

# Challenge 1
def get_playlists():
    """
    document the function here
    """
    # Add your challenge code here


# Challenge 2
def get_tracks_by_playlist():
    """
    document the function here
    """
    #add your challenge code here

# Bonus 1
def get_genres_by_playlist():
    """
    document the function here
    """
    #add your bonus code here

def main():
    """
    main function runs the get* functions
    """
    database = "chinook.db"

    if not os.path.exists(database):
        print("database file not found")
        sys.exit()

    with create_connection(database) as conn:
        print("List of Genres:")
        genre_df = get_genres(conn)
        print(genre_df.head())

        print("List of Tracks in Genre 1")
        tracks_df = get_tracks_by_genre(1, conn)
        print(tracks_df.head())

        print("List of all tracks")
        all_tracks__df = get_tracks(conn)
        print(all_tracks__df.head())

        # call your challenge and bonus functions here


if __name__ == "__main__":
    main()
