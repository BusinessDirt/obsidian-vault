---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Platform
  - Vulkan
  - CommandSystem
---
# Vulkan Command System

**Files**: `Command/List.hpp`, `Command/Buffers.hpp`, `Command/Pool.hpp`

## CommandList
Implements `RHI::ICommandList`.
- Wraps a `vk::CommandBuffer`.
- **State Tracking**: Caches bound resources (Buffers, Textures) in `m_Bindings`.
- **FlushDescriptors**: Before any `Draw` call, `CommandList` uses the **Descriptor Builder** to generate a new Descriptor Set for the current bindings and binds it.

### Dynamic Rendering
`BeginRendering` translates `RHI::RenderingInfo` into `vk::RenderingInfo`.
- Sets up `vk::RenderingAttachmentInfo` for color and depth.
- Handles explicit Load/Store operations and Clear Colors.
- Transitions layouts (via `ImageLayout::eColorAttachmentOptimal`).

## SingleTimeCommand
Helper for immediate GPU execution (used for Buffer/Texture uploads).
1. Allocate ephemeral Command Buffer.
2. Begin.
3. Execute Lambda.
4. End & Submit.
5. Wait Queue Idle.
6. Free Buffer.