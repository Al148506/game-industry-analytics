import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/game_stores.json"


def load_game_stores():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        game_stores = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for game_store in game_stores:

            connection.execute(
                text("""
                    INSERT INTO game_stores (
                       game_id,
                       store_id
                    )
                    VALUES (
                        :game_id,
                        :store_id
                    )
                    ON CONFLICT (game_id, store_id)
                    DO NOTHING
                """),
                game_store
            )

            inserted += 1

    print(f"{inserted} registros procesados")


if __name__ == "__main__":
    load_game_stores()