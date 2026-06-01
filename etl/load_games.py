import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/games_clean.json"


def load_games():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        games = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for game in games:

            connection.execute(
                text("""
                    INSERT INTO games (
                        id,
                        slug,
                        name,
                        released,
                        release_year,
                        rating,
                        ratings_count,
                        reviews_count,
                        metacritic,
                        playtime,
                        added
                    )
                    VALUES (
                        :id,
                        :slug,
                        :name,
                        :released,
                        :release_year,
                        :rating,
                        :ratings_count,
                        :reviews_count,
                        :metacritic,
                        :playtime,
                        :added
                    )
                """),
                game
            )

            inserted += 1

    print(f"{inserted} juegos cargados")


if __name__ == "__main__":
    load_games()