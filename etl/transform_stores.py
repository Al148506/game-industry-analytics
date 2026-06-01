import json


def transform_stores(
        input_file="data/raw/games.json",
        output_file_1="data/processed/stores_clean.json",
        output_file_2="data/processed/game_stores.json"
):
    with open(input_file, "r", encoding="utf-8") as file:
        games = json.load(file)

    stores = {}
    game_stores = []

    for game in games:

        game_id = game.get("id")

        for stores_info in game.get("stores", []):
            store = stores_info["store"]

            store_id = store["id"]

            stores[store_id] = {
                "id": store.get("id"),
                "name": store.get("name"),
                "slug": store.get("slug")
            }

            game_stores.append({
                "game_id": game_id,
                "store_id": store_id
            })

    stores_clean = list(stores.values())

    with open(output_file_1, "w", encoding="utf-8") as file:
        json.dump(
            stores_clean,
            file,
            ensure_ascii=False,
            indent=4
        )

    with open(output_file_2, "w", encoding="utf-8") as file:
        json.dump(
            game_stores,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"stores únicas: {len(stores_clean)}")
    print(f"Relaciones game_stores: {len(game_stores)}")


if __name__ == "__main__":
    transform_stores()
