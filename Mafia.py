import os, sys, glob, importlib.util

# Jo .so file hai usko dhoond kar load karo
so_file = None
# 1. Pehle current python version ki file dhoondo
ver = f"{sys.version_info.major}{sys.version_info.minor}"
for f in glob.glob("SASA*.so"):
    if ver in f:
        so_file = f
        break
# 2. Agar version wali na mile to koi bhi SASA wali utha lo
if not so_file:
    files = glob.glob("SASA*.so")
    if files:
        so_file = files[0]

if not so_file:
    print(f"[!] SASA.cpython-*.so file nahi mili!")
    print(f"Folder me ye files hain: {os.listdir('.')}")
    sys.exit()

print(f"[+] Loading {so_file}...")

try:
    spec = importlib.util.spec_from_file_location("SASA", os.path.join(os.getcwd(), so_file))
    SASA = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SASA)
    
    # Ab SASA ke andar function chalao
    if hasattr(SASA, 'main'):
        SASA.main()
    elif hasattr(SASA, 'start'):
        SASA.start()
    elif hasattr(SASA, 'run'):
        SASA.run()
    else:
        print("[+] SASA loaded, lekin main() function nahi mila")
        # kuch .so direct run hote hain
        print(dir(SASA))

except Exception as e:
    print(f"[!] Load Error: {e}")
    import traceback
    traceback.print_exc()
