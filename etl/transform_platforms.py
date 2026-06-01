import json


def transform_platforms(
        input_file="data/raw/games.json",
        output_file_1="data/processed/platforms_clean.json",
        output_file_2="data/processed/game_platforms.json"
):
    with open(input_file, "r", encoding="utf-8") as file:
        games = json.load(file)

    platforms = {}
    game_platforms = []

    for game in games:

        game_id = game.get("id")

        for platform_info in game.get("platforms", []):
            platform = platform_info["platform"]

            platform_id = platform["id"]

            platforms[platform_id] = {
                "id": platform.get("id"),
                "name": platform.get("name"),
                "slug": platform.get("slug")
            }

            game_platforms.append({
                "game_id": game_id,
                "platform_id": platform_id
            })

    platforms_clean = list(platforms.values())

    with open(output_file_1, "w", encoding="utf-8") as file:
        json.dump(
            platforms_clean,
            file,
            ensure_ascii=False,
            indent=4
        )

    with open(output_file_2, "w", encoding="utf-8") as file:
        json.dump(
            game_platforms,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Plataformas únicas: {len(platforms_clean)}")
    print(f"Relaciones game_platforms: {len(game_platforms)}")


if __name__ == "__main__":
    transform_platforms()
