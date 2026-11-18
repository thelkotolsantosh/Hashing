import argparse
import hashlib
import re
from pathlib import Path


def checksum(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute or verify a file's SHA-256 digest.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--expect")
    args = parser.parse_args()
    if args.expect is not None and not re.fullmatch("[a-fA-F0-9]{64}", args.expect):
        parser.error("Expected digest must have 64 hexadecimal digits.")
    try:
        actual = checksum(args.file)
    except OSError as error:
        parser.error(str(error))
    print(actual)
    raise SystemExit(int(args.expect is not None and actual != args.expect.lower()))
