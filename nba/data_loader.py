import kaggle
import os
import json
from pathlib import Path

# write
# 2. get API keys and save to ~/.kaggle/kaggle.json
# 3. download the NBA database from:
# https://www.kaggle.com/datasets/wyattowalsh/basketball


def kaggle_api_key(
    user_name: str | None = None, api_key: str | None = None
) -> None:
    """
    Function that takes the kaggle API key as input and saves it to
    ~/.kaggle/kaggle.json if it doesn't exist
    """
    if user_name is not None and api_key is not None:
        # Create ~/.kaggle directory if it doesn't exist
        kaggle_dir = Path.home() / ".kaggle"
        kaggle_dir.mkdir(parents=True, exist_ok=True)

        # Path to kaggle.json
        kaggle_json = kaggle_dir / "kaggle.json"

        # Create the JSON content
        api_config = {"username": user_name, "key": api_key}

        # Write the config file if it doesn't exist
        if not kaggle_json.exists():
            with open(kaggle_json, "w") as f:
                json.dump(api_config, f)

            # Set file permissions to be readable only by the user
            os.chmod(
                kaggle_json, 0o600
            )  # read and write permission only for the user
            print(f"Kaggle API key has been saved to {kaggle_json}")


def kaggle_download_data() -> None:
    """
    Function that downloads the NBA database from Kaggle
    """
    # Create the data directory if it doesn't exist
    root_path = Path(__file__).parent.parent
    data_path = root_path / "data"
    data_path.mkdir(parents=True, exist_ok=True)

    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(
        "wyattowalsh/basketball", path=data_path, unzip=True
    )
    print(f"Data has been downloaded to {data_path}")


if __name__ == "__main__":
    kaggle_api_key(user_name="adrian", api_key="1234")
    kaggle_download_data()
