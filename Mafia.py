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
    
    # Auto entry detection - sare common names try karega
    called = False
    for entry in ['main', 'start', 'run', 'login', 'Login', 'main_hub', 'Mafia', 'menu', 'home']:
        if hasattr(xxx, entry):
            print(f"[+] Calling {entry}()...")
            getattr(xxx, entry)()
            called = True
            break
    
    # Agar koi entry na mile to jo bhi callable hai wo try karo
    if not called:
        for name in dir(xxx):
            if name.startswith('_'):
                continue
            obj = getattr(xxx, name)
            if callable(obj):
                try:
                    # Only try functions defined in this module, not imports
                    if hasattr(obj, '__module__') and obj.__module__ == 'xxx':
                        print(f"[+] Trying {name}()...")
                        obj()
                        called = True
                        break
                except:
                    continue
    
    if not called:
        print("[!] No entry found, available:")
        print([x for x in dir(xxx) if not x.startswith('_')])

except Exception as e:
    print(f"[!] Load Error: {e}")
    import traceback
    traceback.print_exc()
