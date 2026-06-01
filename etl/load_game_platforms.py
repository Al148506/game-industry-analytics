import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/game_platforms.json"


def load_game_platforms():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        game_platforms = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for game_platform in game_platforms:

            connection.execute(
                text("""
                    INSERT INTO game_platforms (
                       game_id,
                       platform_id
                    )
                    VALUES (
                        :game_id,
                        :platform_id
                    )
                    ON CONFLICT (game_id, platform_id)
                    DO NOTHING
                """),
                game_platform
            )

            inserted += 1

    print(f"{inserted} registros procesados")


if __name__ == "__main__":
    load_game_platforms()