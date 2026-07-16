# Delhi Metro Megacity: Schematics & Tooling Strategy

Building a 6000x6000 dense urban environment requires heavy reliance on external tools and schematics. Hand-building every structure is impossible. This document outlines the strategy for utilizing WorldPainter, WorldEdit, and Litematica.

## 1. WorldPainter Terrain Plan
WorldPainter is used to generate the base canvas before any blocks are placed in-game.

* **Heightmap:** Flat plains at Y=64 for the central city, sloping up to Y=90 in the west (The Ridge).
* **Biomes:** Custom biome painting to ensure grass/leaf colors match the district vibe (e.g., Savanna for warmer heritage areas, Plains for bright modern areas).
* **Water Bodies:** Paint the 120-block wide Neel River and the artificial lakes (Lotus and Crescent).
* **Pre-Carving Infrastructure:**
  * **Metro Tunnels:** Pre-carve a grid of 15x15 air tunnels at Y=30 and Y=15 for the underground DMTA network. This eliminates the need for manual excavation.
  * **Highway Trenches:** Carve 25-block wide depressed trenches for the ring roads.
* **Forest Generation:** Use custom tree layers on the southern map edge to generate the dense ridge forest.

## 2. WorldEdit Strategy
WorldEdit is the primary tool for large-scale landscaping and repetitive structural placement.

**Key Commands & Uses:**
* `//copy` & `//paste`: Used heavily for standard residential towers (Sunrise Towers) and generic office blocks.
* `//stack`: Crucial for building long stretches of elevated metro viaducts, highways, and BRT corridors.
* `//replace`: Used to quickly swap out block palettes (e.g., turning a generic white concrete building into a heritage brick building).
* `//cyl` & `//sphere`: Used for creating domed structures (like the University Library) or large circular plazas.
* `//curve`: (Requires FastAsyncWorldEdit) Used for laying down curved metro tracks and smooth highway turns.

## 3. Litematica Schematics Library
Litematica is used for placing highly complex, detailed, and non-repetitive structures that require precision. A comprehensive library of schematics must be created and maintained.

**Required Schematic Categories:**

### Transportation & DMTA
* `dmta_standard_station_shell.litematic`: The basic underground box.
* `dmta_elevated_station.litematic`: The standard elevated concourse and platform.
* `train_6car_standard.litematic`: The standard metro train.
* `train_airport_express.litematic`: The high-speed airport train.
* `bus_electric_red.litematic`: Standard city bus.
* `auto_rickshaw_yellow.litematic`: Standard tuk-tuk.

### Flora & Landscaping
* `tree_banyan_large.litematic`: Massive heritage tree.
* `tree_neem_medium.litematic`: Standard street tree.
* `tree_gulmohar.litematic`: Vibrant flowering tree.
* `streetlamp_modern.litematic`: Standard highway light.
* `traffic_signal_intersection.litematic`: 4-way traffic light setup.

### Architecture & Urban Elements
* `heritage_haveli_1.litematic` to `heritage_haveli_5.litematic`: Variations of traditional houses.
* `street_food_stall_set.litematic`: Pre-built vendor booths.
* `shipping_container_stack.litematic`: Pre-arranged colorful containers for the industrial zone.
* `toll_booth_plaza.litematic`: Highway toll gates.

## 4. Workflow Integration
1. **Generate:** Export the WorldPainter map to the server.
2. **Infrastructure:** Use WorldEdit (`//stack`) to lay down the massive lengths of track and road.
3. **Detailing:** Use Litematica to precisely place stations, trains, trees, and complex buildings into the established grid.
4. **Polish:** Hand-detail the connection points between schematics to ensure a seamless, natural look.
