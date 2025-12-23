---
date: 2025-12-23T11:08
tags: []
---
# Render Graph Architecture

## Concept
The Render Graph allows us to declare *intent* ("I need to write to the screen") rather than managing raw API calls. It automatically handles:
1.  **Barriers:** Transitioning images (e.g., `Undefined` -> `ColorAttachment`).
2.  **Culling:** Unused passes are not executed.
3.  **Transient Memory:** Resources can be reused (aliased) if their lifetimes don't overlap.

## Structure

### The Pass
A pass consists of data and two lambdas:
1.  **Setup:** defines inputs/outputs (`builder.Read(...)`, `builder.Write(...)`).
2.  **Execute:** records actual commands (`cmd->Draw(...)`).

```cpp
struct PassData 
{
    RGResourceHandle Output;
};

graph.AddPass<PassData>("MainPass",
    [&](RenderGraphBuilder& builder, PassData& data) 
    {
        // Setup Phase
        data.Output = ...;
    },
    [&](const PassData& data, const RenderGraphRegistry& reg, ICommandList* cmd) 
    {
        // Execute Phase
        cmd->SetViewport(...);
        cmd->Draw(...);
    }
);
```

## Key Components

### 1. Resource Registry

Maps abstract handles (`RGResourceHandle`) to physical `Ref<ITexture>`.
- **ImportBackbuffer:** Critical for the Swapchain. Since the `backbuffer` image changes every frame, we import it fresh at the start of `BeginFrame`.

### 2. Synchronization (Barriers)

Since we use **Dynamic Rendering**, we must insert barriers manually.

- **Before Pass:** Transitions resources to their required state (e.g., `ColorAttachmentOptimal`).
- **After Pass:** Transitions to `PresentSrc` if it's the final `backbuffer` write.

## Strategy: Retained vs Immediate

We are using **Immediate Mode** construction (rebuild graph every frame) but **Pooled Allocation** for the pass data.
- **Linear Allocator:** Allocates `PassData` structs in a contiguous block of memory. Reset at frame start.