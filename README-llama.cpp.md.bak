# llama.cpp provider for DSH
This setup runs `llama.cpp` in a Docker container with full NVIDIA GPU support, providing an OpenAI-compatible API for DeepSeek Harness (DSH).

## Setup
1. **Prepare models directory:**
Ensure you have a `models` folder in the same directory as this file.
```sh
mkdir -p models
```

2. **Download a model:**
Place your `.gguf` model inside the `models` folder.

## Run

1. **Configure the model name:**
Edit `docker-compose.llama.yml` and replace `Qwen3-Coder-30B-A3B-Instruct-Q8_0.gguf` with your actual filename.

2. **Start the server:**
```sh
docker compose -f docker-compose.llama.yml up -d
```

## Configure in DSH GUI
To use this provider in DeepSeek Harness, follow these steps:

1. Go to **Settings** $\rightarrow$ **Models**.
2. Click **[Add model provider]**.
3. Fill in the following:
   - **Provider ID**: `llamacpp`
   - **Display name**: `Llama.cpp (CUDA)`
   - **Base URL**: `http://host.docker.internal:8080/v1`
   - **API Protocol**: `Open AI Chat Completions`
   - **Models**: (Enter the name of your model, e.g., `qwen2.5-coder-32b-instruct`)

## Troubleshooting
- **GPU not detected:** Ensure `nvidia-container-toolkit` is installed on your host machine.
- **Connection refused:** Check if the container is running with `docker ps` and ensure you are using `host.docker.internal` in DSH.
