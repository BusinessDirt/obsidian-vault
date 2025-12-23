---
date: 2025-12-23T11:06
tags: []
---
# Mixture Engine Architecture

## Core Philosophy
Mixture is a layered, cross-platform rendering engine.
- **RHI (Render Hardware Interface):** Abstraction layer over Vulkan (primary), Metal, and D3D12.
- **Render Graph:** A high-level frame dependency manager that automates synchronization and resource transitions.
- **Unified Shader Pipeline:** HLSL-first workflow compiling to SPIR-V/DXIL.

## System Map

### 1. Rendering Core
- [[01_Render_Graph_Architecture|Render Graph System]]: How we define passes and handle synchronization barriers.
- [[04_Command_List_Abstraction|Command List]]: The interface for recording GPU commands (`SetTexture`, `Draw`).

### 2. Memory & Resources
- [[02_RHI_Buffers_and_Descriptors#Vertex & Index Buffers|Buffers]]: Staging buffer architecture using VMA.
- [[02_RHI_Buffers_and_Descriptors#Descriptor Management|Descriptors]]: Bindless-style dynamic allocation and layout caching.

### 3. Asset Pipeline
- [[03_Shader_Pipeline_and_Assets|Shader Compiler]]: DXC-based HLSL compilation with SPIR-V/MSL transpilation.
- **Asset Manager:** Caching system for processed binary assets.

---
> [!INFO] Current Status
> - **Platform:** macOS (MoltenVK) & Windows
> - **Context:** Vulkan 1.3 (Dynamic Rendering)