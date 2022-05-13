import os
import sqlite3
import pandas as pd

def create_connection(db_file:str):
    """
    create connection to sqlite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def get_genres(conn:sqlite3.Connection) -> pd.DataFrame:
    """
    Get the list of Genres from the database
    :param: conn: connection to database
    :return: all genres
    """
    df = pd.read_sql_query("SELECT * FROM genres", conn)
    
    return df
    

def get_tracks_by_genre(genre_id:int, conn:sqlite3.Connection) -> pd.DataFrame:
    """
    Get the list of tracks by Genre
    :param: genre_id: the ID of the genre
    :param: conn: connection to database
    :return: all tracks in the specified genre
    """
    sql_query = """
        SELECT t.trackID, t.Name, t.Composer
        FROM tracks t, genres g 
        WHERE t.GenreId = g.GenreId
        AND g.GenreId = ?
    """
    df = pd.read_sql_query(sql_query, conn, params=(genre_id, ))
    return df

def get_playlists():
    """
    document the function here
    """
    # Add your challenge code here
    pass

def get_tracks_by_playlist():
    """
    document the function here
    """
    #add your challenge code here
    pass

def main():
    database = "chinook.db"

    if not os.path.exists(database):
        print("database file not found")
        quit()

    # create a database connection
    conn = create_connection(database)
    if not conn:
        print("Error connecting to database")
        quit()

    with conn:
        
        print("List of Genres:")
        genre_df = get_genres(conn)
        print(genre_df.head())

        print("List of Tracks in Genre")
        tracks_df = get_tracks_by_genre(1, conn)
        print(tracks_df.head())


if __name__ == "__main__":
    main()