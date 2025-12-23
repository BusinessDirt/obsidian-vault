---
date: 2025-12-23T11:50
tags:
  - Mixture
  - Assets
  - Shaders
---
# Shader System

The **Shader System** in Mixture is designed to support modern, cross-platform shader compilation and management. It leverages **HLSL** as the primary shading language and transpiles/compiles it to the target API's intermediate language (SPIR-V, DXIL, or MSL).

## Architecture

The system is divided into two main parts: the **Offline Compiler** (Asset side) and the **Runtime Factory** (RHI side).

### 1. Compiler Core

The compilation pipeline relies on standard industry tools to ensure compatibility and optimization.

- **DXC (DirectX Shader Compiler)**: Used as the frontend compiler. It compiles HLSL code into **SPIR-V** (for Vulkan) or **DXIL** (for D3D12).
- **SPIRV-Cross**: A tool used to reflect on SPIR-V binaries and transpile them into other languages, such as **MSL** (Metal Shading Language) for macOS support.

### 2. Asset Management

The `AssetManager` orchestrates the compilation process:
1. **Request**: A shader is requested by path.
2. **Check**: The manager checks if a compiled binary exists for the current platform.
3. **Compile**: If not, `ShaderCompiler::Compile` is invoked.
4. **Store**: The resulting `ShaderAsset` (containing the binary blob) is stored in the cache.

### 3. RHI Integration

At runtime, the RHI takes the raw binary data and creates the API-specific GPU object.
- **Vulkan**: Creates `VkShaderModule` from SPIR-V.
- **Metal**: Creates `MTLLibrary` from MSL source (transpiled from SPIR-V).
- **D3D12**: Creates `ID3DBlob` containing DXIL.

## Class Diagram

The following diagram illustrates the relationship between the Asset Manager, the Compiler tools, and the backend RHI classes.

```mermaid
classDiagram
namespace AssetManagement {

	class AssetManager {
		-string m_CacheDirectory
		-Map~UUID, Ref<IAsset>~ m_LoadedAssets
		+GetShader(path) Ref<IShader>
		-CheckCache(hash) Blob
		-WriteCache(hash, blob) void
	}

	class ShaderAsset {
		+UUID ID
		+string Name
		+Blob BinaryData
		+vector~string~ Dependencies
	}
}

namespace CompilerCore {

	class ShaderCompiler {
		<<Static Utility>>
		%% The Asset Manager calls this
		+Compile(source, stage, targetPlatform) CompileResult
	}

	class CompileResult {
		+vector~uint32~ SPIRV
		+string Source
		+vector~byte~ DXIL
		+bool Success
	}

	class DXCWrapper {
		%% Wraps dxcompiler.dll / libdxcompiler.dylib
		+Init()
		+CompileToSPIRV(hlsl, stage) Blob
		+CompileToDXIL(hlsl, stage) Blob
	}

	class SPIRVCrossWrapper {
		%% Wraps spirv-cross.lib
		+ConvertSPIRV_To_MSL(spirvBlob) string
		+ConvertSPIRV_To_GLSL(spirvBlob) string
	}
}

namespace Vulkan {
	class VulkanShader {
		-VkShaderModule m_Module
		+Create(spirvBlob)
	}
}

namespace Metal {
	class MetalShader {
		-MTLLibrary m_Library
		+Create(mslSource)
	}
}

namespace D3D12 {
	class D3D12Shader {
		-ID3DBlob* m_Blob
		+Create(dxilBlob)
	}
}



namespace Mixture {
	class IShader {
		<<Interface>>
		+Bind()
	}
}



%% Interfaces
IShader <--- VulkanShader
IShader <--- MetalShader
IShader <--- D3D12Shader

%% Asset Manager Flow
AssetManager --> ShaderCompiler : 1. Request Compile
AssetManager --> ShaderAsset : 2. Stores Result in RAM/Disk
AssetManager ..> IShader : 3. Factory Creates GPU Object

%% Compiler Logic
ShaderCompiler --> DXCWrapper : Uses for HLSL->SPIRV/DXIL
ShaderCompiler --> SPIRVCrossWrapper : Uses if Target == Metal/GL

%% Factory Logic (How the Shader is created)
VulkanShader ..> CompileResult : Consumes SPIRV
MetalShader ..> CompileResult : Consumes MSL
D3D12Shader ..> CompileResult : Consumes DXIL
```
