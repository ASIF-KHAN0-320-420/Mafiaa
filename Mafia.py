import sys
import os
import glob
import importlib.util

v = f"{sys.version_info.major}{sys.version_info.minor}"
print(f"[+] Python: {v}")

# File Map - Har ek alag line pe
files = {
    "310": "RURUR5551.cpython-310.so",
    "311": "RURUR5552.cpython-311.so",
    "312": "RURUR5553.cpython-312.so",
    "313": "RURUR5554.cpython-313.so",
    "314": "RURUR5555.cpython-314.so"
}

# File dhoondo
target = files.get(v)

if not target or not os.path.exists(target):
    found = glob.glob(f"*{v}*.so")
    if found:
        target = found[0]

if not target:
    print(f"[!] File not found for {v}")
    sys.exit()

print(f"[+] Loading: {target}")

# Load karo
spec = importlib.util.spec_from_file_location("RURUR", target)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
