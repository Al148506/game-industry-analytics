import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/platforms_clean.json"


def load_platforms():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        platforms = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for platform in platforms:

            connection.execute(
                text("""
                    INSERT INTO platforms (
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
                platform
            )

            inserted += 1

    print(f"{inserted} platformas cargadas")


if __name__ == "__main__":
    load_platforms()