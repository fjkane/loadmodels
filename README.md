# Loadmodels

Fast Download LLM models from a simple YAML manifest.

`loadmodels` provides a clean CLI (`mload`) for fetching model files from Hugging Face and placing them into the correct local directories. Ideal for automating
model setup workflows for ComfyUI, inference pipelines, or local AI tooling.

---

## Features

- 🔥 Fast model downloads with `huggingface_hub`
- 📝 YAML-based manifest describing all models
- 🚀 Simple CLI: `mload models.yaml`
- 📁 Automatic placement of downloaded files into their destination directories
- 🛡️ AGPLv3 licensing

---

## Installation

You can install via **GitHub**, **pip**, or **uv**.

### From GitHub (pip)

```bash
pip install https://github.com/fjkane/loadmodels.git
```

### With uv

```bash
uv pip install https://github.com/fjkane/loadmodels.git

```

## Run

### Create a models.yaml file (ComfyUI on Runpod example)

```yaml
models:
  - repo: "omfyanonymous/clip_vision_g"
    files: "clip_vision_g.safetensors"
    target_dir: "/workspace/runpod-slim/ComfyUI/models/clip/"
  - repo: "wangkanai/wan21-lightx2v-i2v-14b-480p/"
    files: "wan21-lightx2v-i2v-14b-480p-cfg-step-distill-rank64-bf16.safetensors"
    target_dir: "/workspace/runpod-slim/ComfyUI/models/loras/"
  - repo: "MeiGen-AI/InfiniteTalk"
    files: "infinitetalk_single.safetensors"
    target_dir: "/workspace/runpod-slim/ComfyUI/models/diffusion_models/"
  - repo: "dci05049/umt5_xxl_fp16.safetensors"
    files: "umt5_xxl_fp16.safetensors"
    target_dir: "/workspace/runpod-slim/ComfyUI/models/text_encoders/"
  - repo: "Osrivers/wan_2.1_vae.safetensors"
    files: "wan_2.1_vae.safetensors"
    target_dir: "/workspace/runpod-slim/ComfyUI/models/vae/"
  - repo: "city96/Wan2.1-I2V-14B-480P-gguf"
    files: "wan2.1-i2v-14b-480p-Q4_K_M.gguf"
    target_dir: "/workspace/runpod-slim/ComfyUI/models/diffusion_models/"
```

### Execute the tool

```bash
mload models.yaml
```
