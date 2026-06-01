import json
from sqlalchemy import text

from db_connection import get_engine


INPUT_FILE = "data/processed/genres_clean.json"


def load_genres():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        genres = json.load(file)

    engine = get_engine()

    inserted = 0

    with engine.begin() as connection:

        for genre in genres:

            connection.execute(
                text("""
                    INSERT INTO genres (
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
                genre
            )

            inserted += 1

    print(f"{inserted} generos cargados")


if __name__ == "__main__":
    load_genres()