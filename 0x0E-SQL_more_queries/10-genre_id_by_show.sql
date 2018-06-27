-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres -- changed to inner join changed to exclude NULL
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
