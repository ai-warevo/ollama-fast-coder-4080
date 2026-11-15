# ⚠️ Archived — Project Moved

**This repository is archived.** The content (Ollama Modelfiles, RTX 4080 optimizations) has been superseded by a new approach using **llama.cpp + GGUF** in Docker.

👉 **Active repo**: [ai-warevo/.github](https://github.com/ai-warevo/.github)

## Why the move?

- Ollama Modelfiles are no longer used — **llama.cpp** with **GGUF** models is faster, more flexible, and doesn't require rebuilding models on every update.
- Docker-based deployment with NVIDIA GPU support (`docker compose --profile llamacpp up -d`).
- New primary model: **Qwen3.6-35B-A3B** (MoE, ~3B active params) via unsloth UD-Q4_K_XL quantization.

## Old content (for reference)

This repo previously contained Modelfiles for:

- **Gemma 4 Fast / Heavy** — optimized for 16GB VRAM
- **Qwen 2.5 Coder** — general-purpose coding model

These are kept here for historical reference only.

---

*This repository will be archived on GitHub. Please direct all new work to [ai-warevo/.github](https://github.com/ai-warevo/.github).*
