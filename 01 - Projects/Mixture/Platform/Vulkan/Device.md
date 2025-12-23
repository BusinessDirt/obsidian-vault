---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - Device
---
# Vulkan Device

**File**: `Platform/Vulkan/Device.hpp`

The `Vulkan::Device` class implements `RHI::IGraphicsDevice`. It wraps `vk::Device` and the **Vulkan Memory Allocator (VMA)**.

## Logical Device Creation
- Enables **Dynamic Rendering** (`dynamicRendering = VK_TRUE`).
- Enables `VK_KHR_swapchain`.
- Creates the **Graphics Queue**.

## Memory Management
The device initializes **VMA** (`VmaAllocator`).
- All `CreateBuffer` and `CreateTexture` calls delegate allocation to VMA.
- VMA handles `VkDeviceMemory` blocks, sub-allocation, and mapping.

## Factory Methods
Implementation of RHI factories:
- `CreateBuffer` -> Returns `Vulkan::Buffer`.
- `CreateTexture` -> Returns `Vulkan::Texture`.
- `CreateShader` -> (Not implemented yet).
- `CreatePipeline` -> (Not implemented yet).