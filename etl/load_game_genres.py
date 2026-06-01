import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/game_genres.json"


def load_game_genres():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        game_genres = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for game_genre in game_genres:

            connection.execute(
                text("""
                    INSERT INTO game_genres (
                       game_id,
                       genre_id
                    )
                    VALUES (
                        :game_id,
                        :genre_id
                    )
                    ON CONFLICT (game_id, genre_id)
                    DO NOTHING
                """),
                game_genre
            )

            inserted += 1

    print(f"{inserted} registros procesados")


if __name__ == "__main__":
    load_game_genres()