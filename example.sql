-- SQL Challenge

-- Example 1: Get all of the Tracks

SELECT * 
FROM tracks;




-- Example 2: Get the Name, Composer for all tracks

SELECT Name, Composer
FROM tracks;





-- Example 3: Get the Name, Composer for tracks that 
--              have a Composer = 'AC/DC'

SELECT Name, Composer
FROM tracks
WHERE Composer = 'AC/DC';







-- Example 4: Get the track name, composer and genre name for all tracks where 
--              the Composer starts with 'Angus'

SELECT t.Name AS TrackName, Composer, 
    g.Name AS GenreName 
FROM tracks t
INNER JOIN genres g ON t.GenreID = g.GenreID
WHERE Composer LIKE 'Angus%'







-- Example 5: Get the genre name and average track price for all tracks
--              where the composer starts with 'Angus'

SELECT g.Name as GenreName, 
	AVG(t.UnitPrice) as AvgPrice
FROM tracks t
INNER JOIN genres g ON t.GenreID = g.GenreID
GROUP BY GenreName

