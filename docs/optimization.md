# Optimization & Performance Checklist

To ensure this AAA megacity runs smoothly, strict optimization guidelines must be followed.

## Lighting Plan
Proper lighting is essential to prevent mob spawns seamlessly while maintaining aesthetics and performance.
- **Streetlights:** Deepslate walls, iron bars, daylight detectors, and redstone lamps.
- **Interiors:** Sea lanterns hidden under carpets, end rods, froglights in modern buildings.
- **Heritage Areas:** Lanterns, soul lanterns, campfires (chimneys).
- **Optimization:** Ensure all underground areas are fully lit to prevent excessive entity spawning calculations. Bake lighting (using server plugins or chunk pre-generation) before distribution.

## Performance Checklist
- [ ] **Redstone Clocks:** Ensure all clocks have toggle switches and can be disabled to reduce TPS lag.
- [ ] **Entities:** Minimize the use of Item Frames and Armor Stands in densely packed areas. Use block geometry instead.
- [ ] **Water Physics:** Replace flowing water with source blocks or blue stained glass where animations are unnecessary.
- [ ] **Lighting Updates:** Ensure all underground tunnels and stations are fully lit to prevent excessive entity spawning calculations and lighting updates.
- [ ] **Chunk Loading:** Bake lighting and pre-generate chunks before distributing the world.
- [ ] **Culling:** If using custom resource packs, ensure unseen faces are culled.
- [ ] **Hopper Optimization:** Lock hoppers with redstone when not actively transferring items to save tick time.
- [ ] **Mob Spawning:** Use string, slabs, or buttons to prevent unwanted mob spawns on roofs and large flat surfaces seamlessly.
