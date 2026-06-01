import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/stores_clean.json"


def load_stores():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        stores = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for store in stores:

            connection.execute(
                text("""
                    INSERT INTO stores (
                        id,
                        slug,
                        name
                    )
                    VALUES (
                        :id,
                        :slug,
                        :name
                    )
                    ON CONFLICT (id)
                    DO NOTHING
                """),
                store
            )

            inserted += 1

    print(f"{inserted} stores cargadas")


if __name__ == "__main__":
    load_stores()