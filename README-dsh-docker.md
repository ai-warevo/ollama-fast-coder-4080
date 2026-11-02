# dsh docker

## clone
```sh
cd ~/Projects/
git clone git@github.com:runzhliu/deepseek-harness-docker.git
```

## configure
```sh
cp ./deepseek-harness-docker/.env.example ./deepseek-harness-docker/.env
# echo "DSH_WORKSPACE=$(pwd)" >> deepseek-harness-docker/.env
sed -i "s|DSH_WORKSPACE=dsh-workspace|DSH_WORKSPACE=$(pwd)|g" deepseek-harness-docker/.env
```

## run
```sh
cd deepseek-harness-docker
docker compose pull
docker compose up --no-build -d 
```

## explore http://127.0.0.1:3080/
```sh
docker compose logs --no-color deepseek-harness | grep 'dsh web:'
```

## add ollama batrak
```sh
-> settings
-> models
[Add model provider]
[Custom model API]
Provider ID = ollama
Display name = ollama
Base URL = http://host.docker.internal:11434/v1
API Protocol = Open AI Chat Completions
Models = gemma4-heavy
```

## add llamacpp batrak
```sh
-> settings
-> models
[Add model provider]
[Custom model API]
Provider ID = llamacpp
Display name = llamacpp
Base URL = http://host.docker.internal:8080/v1
API Protocol = Open AI Chat Completions
Models = Qwen3-Coder-30B-A3B-Instruct-IQ4_XS
Models = Qwen3-Coder-30B-A3B-Instruct-Q8_0
Models = Qwen2.5-Coder-14B-Instruct-Q8_0
```

## enable vision for ollama models (manual patch)
*If image upload is disabled in the UI, you must add a specific patch entry to `/home/node/.dsh/profiles/web/cordis.patch.yml` that explicitly declares vision support and provides necessary metadata:*

1. Edit `/home/node/.dsh/profiles/web/cordis.patch.yml`.
2. Append the following block to the end of the file:
```yaml
- id: llm-deepseek
  name: "@deepseek-ai/dsh-llm-deepseek-api-key"
  config:
    baseURL: http://host.docker.internal:11434/v1
    models:
      - id: gemma4-heavy
        name: gemma4-heavy
        contextWindow: 1000000
        inputModalities:
          - text
          - image
```
3. Restart the container and refresh your browser.

