---
date: 2024-08-13T02:09
tags:
  - Mixture
---
# Shader Uniform Structure
## Scopes (update frequency)
- Globals
	- ex View and Projection Matrix
- Instance
	- ex Material Instance data / textures
- Local (push constants)
	- ex Model Matricies

DescriptorSetLayout 0 for Globals
DescriptorSetLayout 1 for Instance
Push Constants for Local

# Stages
1. Compile shaders if necessary
2. Reflect on shaders to obtain information
	1. Collect Vertex Input Attributes and Bindings
	2. Collect Push Constant Information
	3. Collect UBO and other Descriptor informations
		1. only support 2 sets, set 0 for globals and set 1 for instance
		2. other sets might be supported further down the line 
3. Allocate Descriptors
4. Bind required sets in pipeline creation
