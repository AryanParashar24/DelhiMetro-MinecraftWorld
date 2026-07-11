import nbtlib

def test_file(filepath):
    try:
        data = nbtlib.load(filepath)
        print(f"{filepath} is VALID.")
    except Exception as e:
        print(f"Error loading {filepath}: {e}")

test_file("schematics/litematica/dmta_standard_station_shell.litematic")
test_file("schematics/worldedit/sunrise_towers_floor.schem")
test_file("worldpainter/delhi_metro_6000x6000.world")
