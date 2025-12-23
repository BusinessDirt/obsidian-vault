---
date: 2025-12-23T11:15
tags: []
---
# RHI Resources 
## Vertex & Index Buffers 
We use a **Staging Buffer** strategy to upload data to the GPU. 
- **Heap Type:** `VMA_MEMORY_USAGE_GPU_ONLY` (Fastest, device local). 
- **Upload:** `CPU RAM` -> `Staging Buffer (Mapped)` -> `GPU Buffer`. 
### The `IBuffer` Interface 
Allows us to treat Vertex, Index, and Uniform buffers uniformly. 
```cpp 
struct BufferDesc 
{ 
	uint64_t Size; 
	BufferUsage Usage; // Vertex, Index, Uniform 
}; 

class IBuffer 
{ 
	virtual uint64_t GetSize() = 0; 
};
```

## Descriptor Management

Vulkan descriptors are complex. We abstract them into a "Bindless-style" workflow.

### 1. Growable Allocator
Wraps `VkDescriptorPool`. If a pool runs out, we create a new one and add it to the list.
- **Reset:** All pools are reset at the start of the frame (Frame-based allocation).

### 2. Descriptor Layout Cache

We avoid creating redundant `VkDescriptorSetLayout` objects.

- **Key:** A hashed struct of binding definitions `{Binding, Type, Count, Stage}`.
    
- **Cache:** `HashMap<Info, VkDescriptorSetLayout>`.
    

### 3. The Builder Pattern

Used inside `CommandList` to auto-generate sets.

C++

```
DescriptorBuilder::Begin(&allocator, &cache)
    .BindImage(0, &texInfo)
    .BindBuffer(1, &bufInfo)
    .Build(outSet, outLayout);
```

### 4. Dynamic Binding (Auto-Flush)

The `CommandList` buffers requests:

1. User calls `cmd->SetTexture(0, myTex)`.
    
2. We store `myTex` in a map `m_Bindings`.
    
3. User calls `cmd->Draw()`.
    
4. We **Flush**:
    
    - Build a descriptor set from `m_Bindings`.
        
    - `vkCmdBindDescriptorSets(...)`.
        
    - `vkCmdDraw(...)`.
        

> [!TIP] This mimics the DX11/OpenGL ease of use while keeping the performance of Vulkan.