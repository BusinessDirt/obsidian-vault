---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - Descriptors
---
# Vulkan Descriptors

**Files**: `Descriptors/Allocator.hpp`, `Descriptors/LayoutCache.hpp`, `Descriptors/Builder.hpp`

Mixture uses a dynamic descriptor allocation strategy to handle the flexibility of the RHI without manual descriptor set management.

## DescriptorAllocator
Manages a growing pool of `VkDescriptorPool`s.
- **Ratios**: Configured with expected ratios of descriptor types (e.g., 2:1 Uniform Buffers to Textures).
- **Auto-Growth**: If the current pool fills up (`eErrorOutOfPoolMemory`), a new pool is created and added to the list.
- **Frame Reset**: Pools are reset at the start of every frame (`Context::BeginFrame`), invalidating all sets allocated for that frame.

## DescriptorLayoutCache
To avoid creating redundant `VkDescriptorSetLayout` objects (which is expensive):
- The `CommandList` inspects bindings.
- It constructs a `DescriptorLayoutInfo` (list of bindings).
- The Cache checks if this layout already exists.
- If yes, returns it. If no, creates a new `VkDescriptorSetLayout`.

## DescriptorBuilder
A Fluent API used by `CommandList::FlushDescriptors`:
```cpp
DescriptorBuilder::Begin(allocator, cache)
    .BindBuffer(0, &bufferInfo, ...)
    .BindImage(1, &imageInfo, ...)
    .Build(outSet, outLayout);
```
This builds the layout, allocates the set, and writes the descriptors in one go.