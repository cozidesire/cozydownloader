"""Compatibility shim for Qt-generated UI modules.

Qt's Python UI generator commonly emits `import icons_rc` as a top-level import.
This file forwards that import to the actual resource module in `ui_py` so
regenerating `ui_py/ui_mainwindow.py` will not break imports.
"""

from ui_py.icons_rc import *  # noqa: F401,F403
