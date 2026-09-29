# Optimized Local Models for RTX 4080 🤖⚡

Configuration and Modelfiles for ultra-fast coding using **Gemma 4** and **Qwen 2.5 Coder**, optimized for **NVIDIA RTX 4080** and **AMD Ryzen 7 9800X3D**.

Designed specifically for use with **OpenCode** and **VS Code (Continue)**.

## 🎯 Features ✨

*   **100% GPU Offloading** 🦾: Optimized to maximize RTX 4080 VRAM usage.
*   **Tailored Context** 📜: Different model versions provide various context window sizes depending on your needs.
*   **Spec-Kit Ready** 🗂️: Built to follow Spec-Driven Development workflows (constitution → specify → clarify → plan...).
*   **OpenCode Optimized** 🔌: Pre-configured for seamless local agent integration via Ollama.

## 📦 Available Models 🛠️

### 1. Gemma 4 (Fast)
*Optimized for speed and fits entirely in 16GB VRAM.*
- **Modelfile**: `gemma4-fast.Modelfile`
- **Best use case**: Quick iterative coding, chat, and fast feedback loops.
- **Context**: ~12k

### 2. Gemma 4 (Heavy)
*Maximum capacity for large codebase analysis.*
- **Modelfile**: `gemma4-heavy.Modelfile`
- **Best use case**: Deep architecture planning and analyzing large repositories.
- **Context**: ~64k (Utilizes VRAM + DRAM)

### 3. Qwen 2.5 Coder
*High-performance balance.*
- **Modelfile**: `qwen2.5.Modelfile`
- **Best use case**: General purpose high-quality coding.
- **Context**: ~12k/32k

## 🛠 Installation & Build 🏗️

1.  **Clone repository**:
    ```bash
    git clone https://github.com/ai-warevo/ollama-fast-coder-4080
    cd ollama-fast-coder-4080
    ```

2.  **Build Models in Ollama**:
    ```bash
    # Build Gemma 4 Fast
    ollama create gemma4-fast -f gemma4-fast.Modelfile

    # Build Gemma 4 Heavy
    ollama create gemma4-heavy -f gemma4-heavy.Modelfile

    # Build Qwen 2.5 Coder
    ollama create qwen-fast-coder-4080 -f qwen2.5.Modelfile
    ```

## 💻 Usage with OpenCode 🧩

### 1. Configure OpenCode
Update your `~/.config/opencode/opencode.json` to include the desired model under the Ollama provider:

```json
{
  "provider": {
    "ollama": {
      "models": {
        "gemma4-fast:latest": { "name": "Gemma 4 Fast" },
        "gemma4-heavy:latest": { "name": "Gemma 4 Heavy" }
      }
    }
  }
}
```

### 2. Run OpenCode
Launch your agent through the OpenCode interface. It will automatically interact with your local Ollama instance using the optimized configurations.

## ⚙️ Technical Specifications (Optimizations) 🛠️

*   **Memory Management**: Carefully tuned `use_mlock` and `use_mmap` settings to manage the balance between fast VRAM and larger System RAM (DRAM).
*   **High Precision**: Low temperature (`0.1`) and specific penalties for deterministic, high-quality code generation.
*   **Hardware Affinity**: Parameterized specifically for the performance profiles of RTX 4080 and Ryzen 7 9800X3D.

---
🚀 **Built for speed and privacy.** Local coding at its finest!
