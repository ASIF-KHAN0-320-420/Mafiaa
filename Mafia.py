import os, sys, glob, importlib.util

so_file = None
ver = f"{sys.version_info.major}{sys.version_info.minor}"
for f in glob.glob("SASA*.so"):
    if ver in f:
        so_file = f
        break
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
        
    if hasattr(SASA, 'main'):
        SASA.main()
    elif hasattr(SASA, 'start'):
        SASA.start()
    elif hasattr(SASA, 'run'):
        SASA.run()
    else:        
        print(dir(SASA))

except Exception as e:
    print(f"[!] Load Error: {e}")
    import traceback
    traceback.print_exc()
