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

CREATE TABLE IF NOT EXISTS public.genres
(
    id integer NOT NULL,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    slug character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT genres_pkey PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS public.game_genres
(
    game_id integer NOT NULL,
    genre_id integer NOT NULL,
    CONSTRAINT game_genres_pkey PRIMARY KEY (game_id, genre_id),
    CONSTRAINT fk_game FOREIGN KEY (game_id)
        REFERENCES public.games (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_genre FOREIGN KEY (genre_id)
        REFERENCES public.genres (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS platforms (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS game_platforms (
    game_id INTEGER NOT NULL,
    platform_id INTEGER NOT NULL,

    PRIMARY KEY (game_id, platform_id),

    CONSTRAINT fk_game_platform
        FOREIGN KEY (game_id)
        REFERENCES games(id),

    CONSTRAINT fk_platform
        FOREIGN KEY (platform_id)
        REFERENCES platforms(id)
);

CREATE TABLE IF NOT EXISTS stores (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS game_stores (
    game_id INTEGER NOT NULL,
    store_id INTEGER NOT NULL,

    PRIMARY KEY (game_id, store_id),

    CONSTRAINT fk_game_store
        FOREIGN KEY (game_id)
        REFERENCES games(id),

    CONSTRAINT fk_store
        FOREIGN KEY (store_id)
        REFERENCES stores(id)
);