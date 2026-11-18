import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class CommandTests(unittest.TestCase):
    def test_workflow(self):
        cases = [
          [
            [
              "sample.txt"
            ],
            0,
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
          ],
          [
            [
              "sample.txt",
              "--expect",
              "0000000000000000000000000000000000000000000000000000000000000000"
            ],
            1,
            "ba7816"
          ]
        ]
        with tempfile.TemporaryDirectory() as folder:
            for name in ["sample.txt"]:
                shutil.copy(ROOT / name, folder)
            for args, code, expected in cases:
                with self.subTest(args=args):
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "app.py"), *args], cwd=folder,
                        capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, code, result.stderr)
                    if expected:
                        self.assertIn(expected, result.stdout + result.stderr)
                    else:
                        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
