import nbtlib
from nbtlib.tag import *
import os

def generate_sponge_schematic(filepath):
    # Sponge Schematic basic structure (used by modern WorldEdit)
    root = Compound({
        "Version": Int(2),
        "DataVersion": Int(3465),
        "Width": Short(1),
        "Height": Short(1),
        "Length": Short(1),
        "PaletteMax": Int(1),
        "Palette": Compound({
            "minecraft:stone": Int(0)
        }),
        "BlockData": ByteArray([0])
    })

    file = nbtlib.File({"": root})
    file.gzipped = True
    file.save(filepath)

def main():
    schematics_list = [
        "sunrise_towers_floor.schem",
        "financial_tower_a.schem",
        "financial_tower_b.schem",
        "financial_tower_c.schem"
    ]

    os.makedirs("schematics/worldedit", exist_ok=True)

    for schematic in schematics_list:
        filepath = os.path.join("schematics/worldedit", schematic)
        print(f"Generating {filepath}...")
        generate_sponge_schematic(filepath)

if __name__ == "__main__":
    main()
