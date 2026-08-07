from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


@unittest.skipUnless(importlib.util.find_spec("streamlit"), "streamlit não instalado")
class StreamlitAppTests(unittest.TestCase):
    def test_app_starts_without_exception(self) -> None:
        from streamlit.testing.v1 import AppTest

        app_path = Path(__file__).resolve().parents[1] / "app.py"
        app = AppTest.from_file(str(app_path), default_timeout=20).run()
        self.assertFalse(list(app.exception))
        self.assertEqual(len(app.selectbox), 1)
        self.assertEqual(len(app.text_area) > 0, True)


if __name__ == "__main__":
    unittest.main()
