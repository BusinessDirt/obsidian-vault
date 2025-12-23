---
date: 2024-10-16T16:17
tags:
  - Mixture
  - Render
  - RHI
---
# Render Hardware Interface (RHI)

The **Render Hardware Interface (RHI)** is the foundational abstraction layer of Mixture, designed to decouple the high-level rendering logic from specific graphics APIs (like Vulkan, Direct3D 12, or Metal).

## Key Components

### 1. IGraphicsContext
**File**: `Mixture/Render/RHI/IGraphicsContext.hpp`

The entry point for the rendering backend. It handles:
- Initialization of the Graphics API.
- Surface/Swapchain management.
- Frame synchronization (`BeginFrame` / `EndFrame`).
- Creation of the **Graphics Device**.

### 2. IGraphicsDevice
**File**: `Mixture/Render/RHI/IGraphicsDevice.hpp`

Acts as a factory for GPU resources. It is responsible for creating:
- **Buffers** (`IBuffer`): Vertex, Index, Uniform, Storage.
- **Textures** (`ITexture`): 2D images, Render Targets.
- **Pipelines** (`IPipeline`): Graphics pipeline states (Shaders, Blend State, Depth State).
- **Shaders** (`IShader`): Compiled shader modules (SPIR-V).

### 3. ICommandList
**File**: `Mixture/Render/RHI/ICommandList.hpp`

The primary interface for recording GPU commands. Mixture uses an immediate-mode style recording interface that translates to command buffers under the hood.

**Key Features:**
- **Dynamic Rendering**: No `RenderPass` objects; rendering is defined by attachments passed to `BeginRendering`.
- **State Management**: Viewport, Scissor, Binding (Pipelines, Buffers, Textures).
- **Barriers**: Explicit `PipelineBarrier` calls for resource transitions (though the Render Graph handles most of this).

## Resource Definitions

- **Formats**: `RenderFormats.hpp` defines `RHI::Format` (e.g., `R8G8B8A8_UNORM`, `D32_FLOAT`).
- **States**: `ResourceStates.hpp` defines usage states (e.g., `RenderTarget`, `ShaderResource`, `CopyDest`) used for synchronization.
- **Pipelines**: `RenderStates.hpp` defines fixed-function states like `RasterizerState`, `DepthStencilState`, and `BlendState`.

## Usage Example

```cpp
// 1. Get Device
auto& device = context->GetDevice();

// 2. Create Resources
auto vertexBuffer = device.CreateBuffer({ .Size = 1024, .Usage = BufferUsage::Vertex });

// 3. Record Commands
auto cmd = context->GetCommandBuffer();
cmd->Begin();
    cmd->BeginRendering({ ... });
    cmd->BindVertexBuffer(vertexBuffer);
    cmd->Draw(3, 1, 0, 0);
    cmd->EndRendering();
cmd->End();
```