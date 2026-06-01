import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")

BASE_URL = "https://api.rawg.io/api"


def extract_paginated_resource(
    endpoint: str,
    output_file: str,
    max_pages: int = 50
):

    all_records = []
    page = 1
    while page <= max_pages:

        print(f"[{endpoint}] Página {page}")

        url = f"{BASE_URL}/{endpoint}"

        params = {
            "key": API_KEY,
            "page": page,
            "page_size": 20
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:

            print(
                f"Error en página {page}: "
                f"{response.status_code}"
            )

            break

        data = response.json()

        all_records.extend(data["results"])

        if data["next"] is None:
            break

        page += 1

    output_path = f"data/raw/{output_file}"

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_records,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(
        f"{endpoint}: "
        f"{len(all_records)} registros guardados"
    )


if __name__ == "__main__":

    extract_paginated_resource(
        endpoint="games",
        output_file="games.json"
    )

    extract_paginated_resource(
        endpoint="genres",
        output_file="genres.json"
    )

    extract_paginated_resource(
        endpoint="platforms",
        output_file="platforms.json"
    )