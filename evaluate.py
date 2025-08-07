import subprocess
import tempfile
from pathlib import Path

import httpx
import yaml


def download_and_decrypt(url: str, name: str) -> Path:
    """Download encrypted file and decrypt it."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Download encrypted file
        encrypted_file = tmpdir / f"{name}.csv.asc"
        decrypted_file = tmpdir / f"{name}_train.csv"

        print(f"Downloading {name}'s submission...")
        response = httpx.get(url)
        response.raise_for_status()
        encrypted_file.write_bytes(response.content)

        # Decrypt file
        print(f"Decrypting {name}'s data...")
        result = subprocess.run(
            [
                "gpg",
                "--decrypt",
                "--batch",
                "--yes",
                "--output",
                str(decrypted_file),
                str(encrypted_file),
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise Exception(f"Failed to decrypt {name}'s data: {result.stderr}")

        # Copy to data directory for model to use
        target = Path("data/train.csv")
        target.write_bytes(decrypted_file.read_bytes())

        return target


def evaluate_submission(name: str, url: str) -> float:
    """Evaluate a single submission."""
    try:
        # Download and decrypt
        download_and_decrypt(url, name)

        # Run model
        print(f"Evaluating {name}'s model...")
        result = subprocess.run(["python", "model.py"], capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(f"Model evaluation failed: {result.stderr}")

        # Parse accuracy from output
        accuracy = float(result.stdout.strip())
        return accuracy

    except Exception as e:
        print(f"Error processing {name}: {e}")
        return 0.0


def main():
    # Load submissions
    with open("submissions.yaml") as f:
        data = yaml.safe_load(f)

    print("=" * 50)
    print("Starting evaluation of all submissions")
    print("=" * 50)

    # Evaluate each submission
    results = []
    for submission in data["submissions"]:
        name = submission["name"]
        url = submission["url"]

        print(f"\nProcessing {name}...")
        accuracy = evaluate_submission(name, url)
        results.append((name, accuracy))
        print(f"{name}: {accuracy:.4f}")

    # Print final results
    print("\n" + "=" * 50)
    print("Final Results:")
    print("=" * 50)
    for name, accuracy in sorted(results, key=lambda x: x[1], reverse=True):
        print(f"{name}: {accuracy:.4f}")


if __name__ == "__main__":
    main()
