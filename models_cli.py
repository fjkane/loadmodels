import argparse

import yaml
from huggingface_hub import snapshot_download
from typing import List
from dataclasses import dataclass

@dataclass
class ModelEntry:
    repo: str
    files: str
    target_dir: str


def load_models(path: str) -> List[ModelEntry]:
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    raw_models = data.get("models", [])
    if not isinstance(raw_models, list):
        raise ValueError("'models' must be a list")

    return [ModelEntry(**m) for m in raw_models]

def process_model(model: ModelEntry):
    try:
        snapshot_download(
            local_dir=model.target_dir,
            repo_id=model.repo,
            allow_patterns = model.files,
        )
        print(f"\nDOWNLOAD COMPLETED to: {model.target_dir}")
        print("Check folder content for downloaded files")

    except Exception as e:
        print(f"Error occurred during download: {str(e)}")



def main() -> None:
    parser = argparse.ArgumentParser(
        description="Process model entries from a YAML config file."
    )
    parser.add_argument(
        "config",
        help="Path to the YAML config file containing 'models:' list",
    )

    args = parser.parse_args()

    models = load_models(args.config)
    for model in models:
        process_model(model)


if __name__ == "__main__":
    main()