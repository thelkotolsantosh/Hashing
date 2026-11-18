# File checksum verifier

A matching expected digest exits with code 0. A mismatch exits with code 1. Get the expected digest from a trusted source.

## Run locally

Use Python 3.8 or newer. Run these commands in the project directory.

```sh
python app.py sample.txt
```

Run `python app.py --help` for options and `python -m unittest -v` to check the command-line workflow.
