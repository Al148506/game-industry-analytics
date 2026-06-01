import json


def transform_games(
        input_file="data/raw/games.json",
        output_file="data/processed/games_clean.json"
):

    # Leer archivo
    with open(input_file, "r", encoding="utf-8") as file:
        games = json.load(file)

    clean_games = []

    # Recorrer juegos
    for game in games:

        released = game.get("released")

        release_year = None

        if released:
            release_year = int(released.split("-")[0])

        clean_game = {
            "id": game.get("id"),
            "slug": game.get("slug"),
            "name": game.get("name"),
            "released": released,
            "release_year": release_year,
            "rating": game.get("rating"),
            "ratings_count": game.get("ratings_count"),
            "reviews_count": game.get("reviews_count"),
            "metacritic": game.get("metacritic"),
            "playtime": game.get("playtime"),
            "added": game.get("added")
        }

        clean_games.append(clean_game)

    # Guardar resultado
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            clean_games,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Transformados {len(clean_games)} juegos")


if __name__ == "__main__":
    transform_games()