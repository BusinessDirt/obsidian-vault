---
date: 2026-04-09 11:02
tags:
  - PHPC
  - CUDA
  - SM
  - Warps
links: "[[OpenMP - Offloading]]"
---
## 1. Heterogenes Computing & GPU-Architektur

Graphics Processing Units (GPUs) sind spezialisierte Beschleuniger-Hardware, die auf massive Datenparallelität (**High Throughput**) ausgelegt sind, während CPUs auf minimale Latenz einzelner Threads (**Low Latency**) optimiert sind.

```
+-----------------------------------+  +-----------------------------------+
|               CPU                 |  |               GPU                 |
|  [ALU] [ALU] [ Control ] [Cache]  |  |  [ALU][ALU][ALU][ALU][ALU][ALU]   |
|  [ALU] [ALU] [ DRAM    ]          |  |  [ALU][ALU][ALU][ALU][ALU][ALU]   |
+-----------------------------------+  +-----------------------------------+
```

### Aufbau einer NVIDIA GPU
* **Streaming Multiprocessors (SMs):** Eine GPU besteht aus vielen SMs. Jeder SM enthält hunderte CUDA-Cores, Register-Files, L1-Cache/Shared Memory und Warp-Scheduler.
* **SIMT Execution Model (Single Instruction, Multiple Threads):** Threads werden in Gruppen von **32 Threads**, sogenannten **Warps**, zusammengefasst. Ein Warp führt stets dieselbe Instruktion auf unterschiedlichen Daten aus.

---

## 2. Warp Divergence & Memory Coalescing

### Warp Divergence (Kontrollfluss-Divergenz)
Wenn Threads innerhalb desselben Warps unterschiedliche Pfade einer Verzweigung (`if-else`) nehmen:

> [!WARNING] Performance-Einbuße durch Divergenz
> Der SM führt nacheinander erst den `if`-Zweig aus (während die `else`-Threads inaktiv geschaltet werden) und anschließend den `else`-Zweig. Die Gesamtausführungszeit entspricht der Summe beider Pfade!

### Memory Coalescing (Speicherbündelung)
* **Coalesced Memory Access:** Greifen alle 32 Threads eines Warps auf zusammenhängende, ausgerichtete Speicheradressen im Global Memory zu, werden die Zugriffe hardwareseitig in eine **einzige Transaktion** (z. B. 128 Bytes) gebündelt.
* Unkoordinierte / strided Zugriffe erfordern 32 separate Speicher-Transaktionen $\rightarrow$ Bandbreiten-Kollaps!

---

## 3. CUDA Programmiermodell & Thread-Hierarchie

Das CUDA-Modell unterteilt Arbeit in eine 3-stufige Hierarchie: **Grid $\rightarrow$ Thread Blocks $\rightarrow$ Threads**.

* **Thread Block:** Wird von genau einem SM ausgeführt. Threads im selben Block können über **Shared Memory** kommunizieren und sich mittels `__syncthreads()` synchronisieren.
* **Grid:** Sammlung aller Thread Blocks für den Aufruf eines **Kernels**.

```cpp
// Kernel Definition (wird auf GPU ausgeführt)
__global__ void vecAdd(float *A, float *B, float *C, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}
```

---

## 4. CUDA Speicherhierarchie & Host-Device Transfer

### Speichertypen im Vergleich

| Speichertyp | Ort | Scope | Lebensdauer | Geschwindigkeit |
| :--- | :--- | :--- | :--- | :--- |
| **Register** | On-Chip | Single Thread | Kernel | Extrem schnell (0 Taktzyklen) |
| **Shared Memory**| On-Chip | Block-lokal | Block | Sehr schnell (~L1-Cache Speed) |
| **Global Memory** | Off-Chip DRAM| Global (Host/Device)| Anwendung | Langsam (300-800 Taktzyklen) |

### Host-Device Datentransfer API

```cpp
float *h_A, *d_A;
h_A = (float*) malloc(bytes);
cudaMalloc((void**)&d_A, bytes); // Allokation auf GPU

// Kopieren Host -> Device
cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);

// Kernel Launch: 256 Threads pro Block
dim3 blockDim(256);
dim3 gridDim((N + blockDim.x - 1) / blockDim.x);
vecAdd<<<gridDim, blockDim>>>(d_A, d_B, d_C, N);

// Kopieren Device -> Host
cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost);

cudaFree(d_A); // Freigabe
```
