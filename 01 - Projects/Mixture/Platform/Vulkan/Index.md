---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - Index
---
# Vulkan Backend

This section details the implementation of the **RHI** for the **Vulkan** API.

## Structure
The Vulkan backend is located in `Platform/Vulkan` and roughly maps 1:1 with the RHI interfaces.

- **[[Platform/Vulkan/Context|Context]]**: Initialization (Instance, Surface, Physical Device).
- **[[Platform/Vulkan/Device|Device]]**: Logical Device and Memory Allocator (VMA).
- **[[Platform/Vulkan/Swapchain|Swapchain]]**: Presentation logic.
- **[[Platform/Vulkan/CommandSystem|Command System]]**: Command Pools and Buffers.
- **[[Platform/Vulkan/Resources|Resources]]**: Buffers and Textures.
- **[[Platform/Vulkan/Descriptors|Descriptors]]**: Dynamic Descriptor Management.

## Conventions
- **Vulkan-Hpp**: The engine uses the C++ wrapper (`<vulkan/vulkan.hpp>`) for type safety and RAII where possible, but manual resource management is still used for core objects to control lifecycles explicitly.
- **VMA**: Vulkan Memory Allocator is used for all GPU memory management.
- **Dynamic Rendering**: The backend exclusively uses Vulkan 1.3 Dynamic Rendering, bypassing legacy `VkRenderPass` and `VkFramebuffer` objects.

## Folder Map
- `src/Platform/Vulkan/`
    - `Command/`: Command buffer/pool logic.
    - `Descriptors/`: Descriptor Set logic.
    - `Resources/`: Concrete Texture/Buffer classes.
    - `Sync/`: Fences and Semaphores.