---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - Context
---
# Vulkan Context

**File**: `Platform/Vulkan/Context.hpp`

The `Vulkan::Context` class implements `RHI::IGraphicsContext`. It acts as the container for the entire Vulkan state.

## Responsibilities

1. **Instance Creation**:
   - Enables Validation Layers (`VK_LAYER_KHRONOS_validation`) in Debug mode.
   - Enables `VK_KHR_portability_enumeration` for macOS (MoltenVK) support.
   - Sets up the Debug Messenger.

2. **Physical Device Selection**:
   - Enumerates GPUs.
   - Rates suitability based on:
     - Vulkan 1.3 support.
     - Discrete GPU preference.
     - Presentation support.
     - Required extensions (`VK_KHR_swapchain`, `VK_KHR_portability_subset`).

3. **Global Objects**:
   - Holds the `Vulkan::Device` (Logical Device).
   - Holds the `Vulkan::Swapchain`.
   - Holds `CommandPools` and global `DescriptorAllocators`.

4. **Frame Loop**:
   - `BeginFrame()`:
     - Waits for Fences (CPU-GPU sync).
     - Resets Descriptor Pools.
     - Acquires the next Swapchain image.
   - `EndFrame()`:
     - Submits the Command Buffer to the Graphics Queue.
     - Presents the image to the screen.
     - Advances the current frame index (`m_CurrentFrame`).

## Synchronization
The Context manages "Frames in Flight" (double/triple buffering):
- **Fences**: Wait for the CPU to safely reuse command buffers/resources from `Frame[i]`.
- **Semaphores**:
  - `ImageAvailable`: Signaled when swapchain gives us an image.
  - `RenderFinished`: Signaled when rendering is done, waited on by Presentation.