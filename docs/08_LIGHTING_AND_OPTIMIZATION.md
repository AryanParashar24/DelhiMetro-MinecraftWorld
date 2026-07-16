# Delhi Metro Megacity: Lighting & Optimization Strategy

A 6000x6000 block city with dense interiors, extensive underground networks, and complex redstone can quickly bring a Minecraft server to its knees. This document outlines the strict guidelines required to maintain high TPS (Ticks Per Second) and smooth framerates for players.

## 1. Lighting Plan & Mob Control
Improper lighting leads to massive entity spawning, which is the #1 cause of server lag.

**Core Lighting Rules:**
* **Zero Dark Zones (Above Ground):** All streets, alleys, and parks must be lit above level 0. Use streetlights (redstone lamps) and hidden light sources (light blocks, or sea lanterns hidden under carpets/slabs).
* **Zero Dark Zones (Underground):** Every metro tunnel, maintenance shaft, and basement must be fully lit. Dark areas require the game to constantly check for mob spawn conditions.
* **Concealed Lighting:** To maintain aesthetics, use Sea Lanterns, Glowstone, or Shroomlights hidden behind stairs, slabs, leaves, or carpets.
* **Dynamic Lighting Limits:** Avoid large-scale blinking lights or massive arrays connected to rapid redstone clocks, as lighting updates cause significant block lag.

## 2. Entity Management
Entities (Item Frames, Armor Stands, Minecarts, Mobs) require constant rendering and logic updates.

**Core Entity Rules:**
* **Item Frames:** Use them sparingly. Do not use them for wallpaper or massive screens unless absolutely necessary. Prefer glowing item frames for crucial DMTA signage only.
* **Armor Stands/NPCs:** Disable AI on all decorative entities (`NoAI:1b`, `Silent:1b`, `Invulnerable:1b`).
* **Minecarts/Boats:** Avoid leaving hundreds of empty minecarts on tracks. Use static block-build trains for aesthetics, reserving actual minecarts for functional gameplay loops.
* **Mob Spawning:** The `setup.mcfunction` script explicitly sets `gamerule doMobSpawning false` for adventure map distribution.

## 3. Redstone Optimization
Unoptimized redstone can cause severe TPS drops due to constant block updates.

**Core Redstone Rules:**
* **No Unnecessary Clocks:** All redstone clocks (e.g., for automated ticket gates or traffic lights) must have a toggle switch or proximity sensor. They should only run when a player is nearby.
* **Avoid Hoppers:** Large arrays of hoppers constantly check for items above them. Place composters or droppers on top of hoppers to stop this check if they are only moving items horizontally.
* **Use Observers:** Prefer Observers over complex repeater/comparator logic where possible, as they cause fewer block updates.
* **Pistons:** Use sticky pistons sparingly in dense areas, as moving blocks cause lighting and rendering updates.

## 4. Block Rendering & Water
* **Flowing Water:** Massive waterfalls or flowing rivers require constant block updates. Use source blocks for the Neel River and lakes. Keep flowing water to a minimum.
* **Complex Geometry:** Heavily detailed areas using thousands of stairs, slabs, walls, and fences can lower client framerates. Balance highly detailed focal points with solid block structures nearby.
* **Glass & Transparency:** Massive layers of transparent blocks (glass overlapping glass) can cause render lag. Keep skyscraper windows to a single layer where possible.

## 5. Pre-Release Optimization Checklist
Before exporting the final world save, run through this checklist:

* [ ] Execute `/gamerule randomTickSpeed 0` to stop leaf decay and crop growth.
* [ ] Execute `/gamerule doDaylightCycle false` and set time to day (if distributing a static daytime map).
* [ ] Execute `/gamerule doWeatherCycle false` and clear weather.
* [ ] Execute `/kill @e[type=item]` to remove any dropped blocks left from building.
* [ ] Run a server plugin or mod (like Chunky) to pre-generate all chunks within the 6000x6000 border. This prevents the server from generating terrain dynamically when players explore.
* [ ] Optimize the world save using the in-game "Optimize World" feature to update all chunks to the current version format.
* [ ] Verify that the `datapack/` is correctly loaded and `setup.mcfunction` runs without errors.
* [ ] Fly through the most dense areas (Downtown, DMTA Central) in survival mode to check for framerate drops.
