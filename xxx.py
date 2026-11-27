#!/usr/bin/env python3
from pathlib import Path
import importlib.machinery
import importlib.util
import sys
import sysconfig
import traceback

MODULE_NAME = 'xxx'
_HERE = Path(__file__).resolve().parent


def _extension_path():
    suffixes = []
    exact = sysconfig.get_config_var("EXT_SUFFIX")
    if exact:
        suffixes.append(exact)
    for suffix in importlib.machinery.EXTENSION_SUFFIXES:
        if suffix not in suffixes:
            suffixes.append(suffix)

    for suffix in suffixes:
        candidate = _HERE / (MODULE_NAME + suffix)
        if candidate.is_file():
            return candidate

    found = sorted(p.name for p in _HERE.glob(MODULE_NAME + "*.so"))
    found += sorted(p.name for p in _HERE.glob(MODULE_NAME + "*.pyd"))
    current = sysconfig.get_config_var("EXT_SUFFIX") or "unknown"
    details = ", ".join(found) if found else "koi compiled extension nahi mili"
    raise FileNotFoundError(
        "Is Python/platform ke liye matching compiled file nahi mili. "
        "Current ABI: " + current + "; available: " + details
    )


def main():
    so_path = _extension_path()
    if str(_HERE) not in sys.path:
        sys.path.insert(0, str(_HERE))
    spec = importlib.util.spec_from_file_location(MODULE_NAME, so_path)
    if spec is None or spec.loader is None:
        raise ImportError("Extension loader create nahi hua: " + str(so_path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    # Script code runs during module initialization; no function-name guessing.


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nStopped.")
    except Exception as exc:
        print("[!] Compiled script error:", exc)
        traceback.print_exc()
