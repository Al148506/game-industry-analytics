import json


def transform_genres(
    input_file="data/raw/games.json",
    output_file_1="data/processed/genres_clean.json",
    output_file_2="data/processed/game_genres.json"
):

    with open(input_file, "r", encoding="utf-8") as file:
        games = json.load(file)

    genres = {}
    game_genres = []

    for game in games:

        game_id = game.get("id")

        for genre in game.get("genres", []):

            genre_id = genre.get("id")

            genres[genre_id] = {
                "id": genre.get("id"),
                "name": genre.get("name"),
                "slug": genre.get("slug")
            }

            game_genres.append({
                "game_id": game_id,
                "genre_id": genre_id
            })

    genres_clean = list(genres.values())

    with open(output_file_1, "w", encoding="utf-8") as file:
        json.dump(
            genres_clean,
            file,
            ensure_ascii=False,
            indent=4
        )

    with open(output_file_2, "w", encoding="utf-8") as file:
        json.dump(
            game_genres,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Géneros únicos: {len(genres_clean)}")
    print(f"Relaciones game_genres: {len(game_genres)}")


if __name__ == "__main__":
    transform_genres()