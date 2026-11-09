"""Load pure-Python DeePMD loss code with a minimal generated-config stand-in.

No native DeePMD extension is loaded; tensor math uses the installed backend.
"""

import os
from pathlib import Path
import sys
import types

root = Path(os.environ.get("DEEPMD_SOURCE", r"C:\PR\deepmd-scout-20261109"))
deps = Path(os.environ.get("DEEPMD_TEST_DEPS", r"C:\PR\deepmd-loss-deps-20261109"))
config = Path(os.environ.get("DEEPMD_TEST_CONFIG", r"C:\PR\deepmd-loss-config-20261109"))
config.mkdir(parents=True, exist_ok=True)
(config / "run_config.ini").write_text("[CONFIG]\n", encoding="utf-8")
sys.path.insert(0, str(root))
sys.path.insert(0, str(deps))
import deepmd

lib = types.ModuleType("deepmd.lib")
lib.__path__ = [str(config)]
sys.modules["deepmd.lib"] = lib
deepmd.lib = lib

import deepmd.pt

for name, path in (
    ("deepmd.dpmodel", "deepmd/dpmodel"),
    ("deepmd.dpmodel.loss", "deepmd/dpmodel/loss"),
    ("deepmd.pt.loss", "deepmd/pt/loss"),
    ("deepmd.pt.utils", "deepmd/pt/utils"),
    ("deepmd.pd.utils", "deepmd/pd/utils"),
):
    package = types.ModuleType(name)
    package.__path__ = [str(root / path)]
    sys.modules[name] = package

if __name__ == "__main__":
    import pytest

    sys.exit(pytest.main(["-q", *sys.argv[1:]]))
