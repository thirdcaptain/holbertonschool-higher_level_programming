-- lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT OUTER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT OUTER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'

/*
SELECT tv_shows.title, tv_shows.id
FROM tv_shows
WHERE title='Dexter'
*/

/*
SELECT tv_genres.name AS genre, COUNT(*)  AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC, genre ASC;
*/
