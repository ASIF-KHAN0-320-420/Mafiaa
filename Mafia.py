import sys

try:
    import SASA
    # SASA ke andar jo function hai uska naam yahan lagao
    SASA.main()

except ModuleNotFoundError:
    print("SASA module nahi mila! SASA.cpython-*.so file Mafia.py ke sath rakho")
    sys.exit()

except AttributeError:
    # Agar SASA.main() nahi hai to ye try hoga
    try:
        SASA.start()
    except:
        try:
            SASA.run()
        except:
            print("SASA load ho gaya lekin function ka naam main/start/run me se nahi hai")

except Exception as e:
    print(f"Error: {e}")
