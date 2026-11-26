import os, sys, glob, importlib.util

so_file = None
ver = f"{sys.version_info.major}{sys.version_info.minor}"
for f in glob.glob("xxx*.so"):
    if ver in f:
        so_file = f
        break
if not so_file:
    files = glob.glob("xxx*.so")
    if files:
        so_file = files[0]

if not so_file:
    print(f"[!] xxx.cpython-*.so file nahi mili!")
    print(f"Folder me ye files hain: {os.listdir('.')}")
    sys.exit()

print(f"[+] Loading {so_file}...")

try:
    spec = importlib.util.spec_from_file_location("xxx", os.path.join(os.getcwd(), so_file))
    xxx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(xxx)
        
    if hasattr(xxx, 'main'):
        xxx.main()
    elif hasattr(xxx, 'start'):
        xxx.start()
    elif hasattr(xxx, 'run'):
        xxx.run()
    elif hasattr(xxx, 'login'):
        xxx.login()
    else:        
        print(dir(xxx))

except Exception as e:
    print(f"[!] Load Error: {e}")
    import traceback
    traceback.print_exc()
