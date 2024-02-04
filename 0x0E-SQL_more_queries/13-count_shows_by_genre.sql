-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked --
SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows  FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name, tv_genres.id ORDER BY number_of_shows DESC;
