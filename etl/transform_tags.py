import json


def transform_tags(
        input_file="data/raw/games.json",
        output_file_1="data/processed/tags_clean.json",
        output_file_2="data/processed/game_tags.json"
):

    with open(input_file, "r", encoding="utf-8") as file:
        games = json.load(file)

    tags = {}
    game_tags = []

    for game in games:

        game_id = game.get("id")

        for tag in game.get("tags", []):

            tag_id = tag.get("id")

            tags[tag_id] = {
                "id": tag.get("id"),
                "name": tag.get("name"),
                "slug": tag.get("slug")
            }

            game_tags.append({
                "game_id": game_id,
                "tag_id": tag_id
            })

    tags_clean = list(tags.values())

    with open(output_file_1, "w", encoding="utf-8") as file:
        json.dump(
            tags_clean,
            file,
            ensure_ascii=False,
            indent=4
        )

    with open(output_file_2, "w", encoding="utf-8") as file:
        json.dump(
            game_tags,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Tags únicas: {len(tags_clean)}")
    print(f"Relaciones game_tags: {len(game_tags)}")


if __name__ == "__main__":
    transform_tags()