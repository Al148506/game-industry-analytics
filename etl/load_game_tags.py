import json
from sqlalchemy import text

from db_connection import get_engine

INPUT_FILE = "data/processed/game_tags.json"


def load_game_tags():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        game_tags = json.load(file)

    engine = get_engine()

    processed = 0

    with engine.begin() as connection:

        for game_tag in game_tags:

            connection.execute(
                text("""
                    INSERT INTO game_tags (
                        game_id,
                        tag_id
                    )
                    VALUES (
                        :game_id,
                        :tag_id
                    )
                    ON CONFLICT (game_id, tag_id)
                    DO NOTHING
                """),
                game_tag
            )

            processed += 1

    print(f"{processed} relaciones procesadas")


if __name__ == "__main__":
    load_game_tags()