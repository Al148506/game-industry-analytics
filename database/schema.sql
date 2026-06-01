CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    slug VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,

    released DATE NOT NULL,
    release_year INTEGER NOT NULL,

    rating NUMERIC(3,2) NOT NULL,

    ratings_count INTEGER NOT NULL,
    reviews_count INTEGER NOT NULL,

    metacritic INTEGER,

    playtime INTEGER NOT NULL,
    added INTEGER NOT NULL
);