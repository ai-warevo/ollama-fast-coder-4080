# llama.cpp provider for DSH (RTX 4080 16GB, Ryzen 7 9800X3D, 64GB RAM)

Model: **Qwen3.6-35B-A3B**, unsloth `UD-Q4_K_XL` (20.8 GB), served as `qwen3.6-35b-a3b`.
MoE with ~3B active params, so the experts that don't fit in VRAM run from DDR5 at usable speed
(`--fit on` places them). Hybrid attention keeps the 64k q8_0 KV cache to a few hundred MB.
Fallback if you need speed over quality: `Qwen3-Coder-30B-A3B-Instruct-UD-Q4_K_XL.gguf` (16.5 GB, already have IQ4_XS locally).

## 1. Download (~21 GB, resumable)
```sh
cd ollama-fast-coder-4080
mkdir -p models
curl -L -C - -o models/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
  https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/resolve/main/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf
```
(or `pip install -U "huggingface_hub[cli]"` then
`hf download unsloth/Qwen3.6-35B-A3B-GGUF Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf --local-dir models`)

## 2. Start llama-server
```sh
docker compose -f docker-compose.llama.yml pull
docker compose -f docker-compose.llama.yml up -d --force-recreate
docker compose -f docker-compose.llama.yml logs -f llama-server   # wait for "server is listening"
```
Smoke test (tool calling):
```sh
curl -s http://127.0.0.1:8080/v1/chat/completions -H "Authorization: Bearer llamacpp" -H "Content-Type: application/json" -d '{
 "model":"qwen3.6-35b-a3b","messages":[{"role":"user","content":"What is the weather in Paris? Use the tool."}],
 "tools":[{"type":"function","function":{"name":"get_weather","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}]}' | head -c 1500
```
Expect `tool_calls` with `get_weather`.

## 3. Restart DSH
```sh
cd ../deepseek-harness-docker
docker compose up -d --force-recreate          # add --build if Dockerfile.fix changed
```
In the DSH UI pick provider **llamacpp** -> model **Qwen3.6-35B-A3B (UD-Q4_K_XL, local)**
(provider config lives in `deepseek-harness-docker/dsh-home/profiles/web/cordis.patch.yml`;
the key is the `LLAMACPP_API_KEY` ref in `dsh-home/.credentials.yaml` = `llamacpp`, matching `--api-key`).

## Tuning
- VRAM OOM / `nvidia-smi` > 15.5 GB: raise `--fit-target` (e.g. 2048) or use the manual `--n-cpu-moe` block (raise N).
- VRAM left over: lower `--n-cpu-moe`, or `--fit-target 1024`.
- Context: `--ctx-size 65536`; 32768 saves little VRAM (KV is small) but speeds nothing, keep 64k.
- Thinking: DSH toggles it via the effort selector (`off` = fast, `high` = thinks). Keep `high` for hard tasks.
- Change the key: set `LLAMACPP_API_KEY` in env/.env for compose AND the ref in `.credentials.yaml`.

## Troubleshooting
- GPU not detected: install NVIDIA driver + Docker Desktop WSL2 GPU support / `nvidia-container-toolkit`.
- DSH "connection refused": `docker ps`; DSH must use `http://host.docker.internal:8080/v1` (extra_hosts is set in its compose).
- 401: key mismatch between `--api-key` and `.credentials.yaml`.
