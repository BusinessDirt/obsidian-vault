---
date: 2024-08-07T22:10
tags:
  - Vulkan
  - cpp
---
# DescriptorSetLayout
Contains information about the different descriptor sets. 

# DescriptorSet
Contains information about a Buffer, Image, etc in the form of a binding

# Summary
- Multiple DescriptorSetLayouts per pipeline (declared by the ‘set‘ parameter)
- Multiple DescriptorSets per Layout
	- One DescriptorBinding per Set that describes the memory

# Allocation
Allocation through a DescriptorPool


# Managing different sets
- Descriptors are only used in shaders so we can scan all the shaders and collect every descriptor used
- Then we can group them into their own sets and store a reference to those sets in the shader
- Then we allocate all the descriptor sets and layouts
- At Pipeline Creation we can retrieve all the layouts from the shader and parse them to the PipelineLayout
- The user just has to write the buffer/image info to the the descriptor 
	- Buffers and images might also be create inside the pipeline for further abstraction
		- There could be an issue related to setting the values

## Shader Reflection Structure
- ShaderInformation
	- 