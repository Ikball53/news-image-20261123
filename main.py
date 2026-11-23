"""Entry program for the news-image-20261123 competition.

The bundled picture sits next to this file. Running the program copies
that picture to /output/entry.png, creating the output folder first when
it does not exist yet. Nothing is fetched from the network.
"""

import shutil
from pathlib import Path


def locate_picture() -> Path:
    """Return the path of the bundled entry image.

    The picture normally sits beside this script; if it is not there,
    fall back to the current working directory so the program still
    works when invoked from a copied checkout.
    """
    beside_script = Path(__file__).resolve().parent / "entry.png"
    if beside_script.is_file():
        return beside_script
    return Path.cwd() / "entry.png"


def publish(source: Path, target_dir: Path) -> Path:
    """Copy *source* into *target_dir* as entry.png and return the result."""
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.png"
    shutil.copyfile(source, destination)
    return destination


def main() -> None:
    picture = locate_picture()
    if not picture.is_file():
        raise SystemExit(f"bundled image missing: {picture}")
    written = publish(picture, Path("/output"))
    print(f"wrote {written} ({written.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
