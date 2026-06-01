import json
from sqlalchemy import text

from db_connection import get_engine

INPUT_FILE = "data/processed/tags_clean.json"


def load_tags():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        tags = json.load(file)

    engine = get_engine()

    processed = 0

    with engine.begin() as connection:

        for tag in tags:

            connection.execute(
                text("""
                    INSERT INTO tags (
                        id,
                        name,
                        slug
                    )
                    VALUES (
                        :id,
                        :name,
                        :slug
                    )
                    ON CONFLICT (id)
                    DO NOTHING
                """),
                tag
            )

            processed += 1

    print(f"{processed} tags procesadas")


if __name__ == "__main__":
    load_tags()