DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INT,
    artist_id INT
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Boxer', '2007', 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Brothers', '2010', 2);
