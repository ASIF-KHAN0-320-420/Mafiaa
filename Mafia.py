import os, sys, glob, importlib.util

so_file = None
ver = f"{sys.version_info.major}{sys.version_info.minor}"
for f in glob.glob("XXXX*.so"):
    if ver in f:
        so_file = f
        break
if not so_file:
    files = glob.glob("XXXX*.so")
    if files:
        so_file = files[0]

if not so_file:
    print(f"[!] XXXX.cpython-*.so file nahi mili!")
    print(f"Folder me ye files hain: {os.listdir('.')}")
    sys.exit()

print(f"[+] Loading {so_file}...")

try:
    spec = importlib.util.spec_from_file_location("XXXX", os.path.join(os.getcwd(), so_file))
    XXXX = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(XXXX)
        
    if hasattr(XXXX, 'main'):
        XXXX.main()
    elif hasattr(XXXX, 'start'):
        XXXX.start()
    elif hasattr(XXXX, 'run'):
        XXXX.run()
    else:        
        print(dir(XXXX))

except Exception as e:
    print(f"[!] Load Error: {e}")
    import traceback
    traceback.print_exc()
