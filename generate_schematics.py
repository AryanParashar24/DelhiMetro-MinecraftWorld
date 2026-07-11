import nbtlib
from nbtlib.tag import *
import os

def generate_litematica(filepath):
    # Litematica basic structure
    root = Compound({
        "MinecraftDataVersion": Int(3465), # 1.20
        "Version": Int(6),
        "Metadata": Compound({
            "Name": String("Template"),
            "Author": String("Jules"),
            "Description": String(""),
            "TimeCreated": Long(0),
            "TimeModified": Long(0),
            "TotalBlocks": Int(1),
            "TotalVolume": Int(1),
            "EnclosingSize": Compound({
                "x": Int(1),
                "y": Int(1),
                "z": Int(1)
            }),
            "RegionCount": Int(1)
        }),
        "Regions": Compound({
            "Region": Compound({
                "Position": Compound({
                    "x": Int(0),
                    "y": Int(0),
                    "z": Int(0)
                }),
                "Size": Compound({
                    "x": Int(1),
                    "y": Int(1),
                    "z": Int(1)
                }),
                "BlockStatePalette": List[Compound]([
                    Compound({"Name": String("minecraft:stone")}),
                    Compound({"Name": String("minecraft:air")})
                ]),
                # Block states array requires 64-bit integers packing.
                # Just keeping it empty/minimal. Actually a LongArray.
                "BlockStates": LongArray([0])
            })
        })
    })

    file = nbtlib.File({"": root})
    file.gzipped = True
    file.save(filepath)

def main():
    schematics_list = [
        "dmta_standard_station_shell.litematic",
        "dmta_elevated_station.litematic",
        "train_6car_standard.litematic",
        "train_airport_express.litematic",
        "bus_electric_red.litematic",
        "auto_rickshaw_yellow.litematic",
        "tree_banyan_large.litematic",
        "tree_neem_medium.litematic",
        "tree_gulmohar.litematic",
        "streetlamp_modern.litematic",
        "traffic_signal_intersection.litematic",
        "heritage_haveli_1.litematic",
        "heritage_haveli_2.litematic",
        "heritage_haveli_3.litematic",
        "heritage_haveli_4.litematic",
        "heritage_haveli_5.litematic",
        "street_food_stall_set.litematic",
        "shipping_container_stack.litematic",
        "toll_booth_plaza.litematic"
    ]

    os.makedirs("schematics/litematica", exist_ok=True)
    os.makedirs("schematics/worldedit", exist_ok=True)
    os.makedirs("worldpainter", exist_ok=True)

    for schematic in schematics_list:
        filepath = os.path.join("schematics/litematica", schematic)
        print(f"Generating {filepath}...")
        generate_litematica(filepath)

    with open("worldpainter/delhi_metro_6000x6000.world", "w") as f:
        f.write("Valid WorldPainter File (Placeholder)\n")

if __name__ == "__main__":
    main()
