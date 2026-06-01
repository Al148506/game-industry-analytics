import json

INPUT_FILE = "../data/data/raw/games.json"

FIELDS_TO_CHECK = [
    "released",
    "rating",
    "ratings_count",
    "reviews_count",
    "metacritic",
    "playtime",
    "added"
]


def profile_null_values():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        games = json.load(file)

    total_records = len(games)

    print(f"\nTotal de registros: {total_records}\n")

    for field in FIELDS_TO_CHECK:

        null_count = 0

        for game in games:

            if game.get(field) is None:
                
                null_count += 1

        percentage = (null_count / total_records) * 100

        print(
            f"{field:<15} "
            f"NULLs: {null_count:<5} "
            f"({percentage:.2f}%)"
        )


if __name__ == "__main__":
    profile_null_values()