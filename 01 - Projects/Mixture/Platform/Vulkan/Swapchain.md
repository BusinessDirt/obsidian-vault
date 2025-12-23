---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - Swapchain
---
# Vulkan Swapchain

**File**: `Platform/Vulkan/Swapchain.hpp`

The `Vulkan::Swapchain` manages the chain of images used for presentation.

## Creation Logic
1. **Capabilities Query**: Checks surface support.
2. **Format Selection**: Prefers `B8G8R8A8_SRGB` or `R8G8B8A8_SRGB` with `ColorSpace::sRGB_NonLinear`.
3. **Present Mode**: Prefers `Mailbox` (Triple Buffering) for low latency, falls back to `FIFO` (VSync).
4. **Resolution**: Clamps requested width/height to surface capabilities.

## Image Views
The Swapchain creates `vk::ImageView`s for all swapchain images. These are wrapped in `Vulkan::Texture` objects (with `m_OwnsImage = false`) so they can be used interchangeably with standard textures in the RHI.

## Re-Creation
Handles window resizing:
- `Recreate(width, height)`:
  - Waits for Idle.
  - Destroys old views.
  - Creates new `VkSwapchainKHR` (passing `oldSwapchain` for recycling).
  - Re-creates views.