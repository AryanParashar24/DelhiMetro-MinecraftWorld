# Performance Optimization Checklist

## 1. Optimization Checklist
- [ ] Ensure all redstone clocks have toggle switches (can be disabled to reduce TPS lag).
- [ ] Minimize the use of Item Frames and Armor Stands in densely packed areas (use block geometry where possible).
- [ ] Replace flowing water with source blocks or blue stained glass where animations are unnecessary.
- [ ] Ensure all underground areas are fully lit to prevent excessive entity spawning calculations.
- [ ] Bake lighting (using server plugins or chunk pre-generation) before distribution.
- [ ] Cull unseen faces in complex custom blocks (if using resource packs).
