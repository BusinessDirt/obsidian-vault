---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - Resources
---
# Vulkan Resources

**Files**: `Resources/Texture.hpp`, `Resources/Buffer.hpp`

## Texture
`Vulkan::Texture` implements `RHI::ITexture`.

### Modes
1. **Owned**: Created via `TextureDesc` or from file.
   - Allocates `VkImage` via VMA.
   - Creates `VkImageView` and `VkSampler`.
   - Handles data upload via Staging Buffer.
2. **Wrapped**: Created from an existing `VkImage` (e.g., Swapchain).
   - Does *not* own the memory (no VMA allocation).
   - Destructor cleans up the View but not the Image.

### Data Upload
When loading from a file (stb_image):
1. Load pixels to CPU memory.
2. Create **Staging Buffer** (Host Visible).
3. Copy pixels to Staging Buffer.
4. Issue `SingleTimeCommand`:
   - Barrier: Undefined -> TransferDst.
   - `vkCmdCopyBufferToImage`.
   - Barrier: TransferDst -> ShaderReadOnly.

## Buffer
`Vulkan::Buffer` implements `RHI::IBuffer`.

- Allocates `VkBuffer` via VMA.
- Usage flags are derived from `RHI::BufferUsage`.
- Supports initial data upload via Staging Buffer (similar to Textures).