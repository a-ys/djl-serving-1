# vLLM Engine User Guide

## Model Artifacts Structure

vLLM expects the model artifacts to be in the [standard HuggingFace format](../deployment_guide/model-artifacts.md#huggingface-transformers-pretrained-format).

## Supported Model architecture

LMI is shipping vLLM 0.4.2 with 0.28.0 containers, 
so technically we support all LLM that [vLLM 0.4.2 support](https://github.com/vllm-project/vllm/tree/v0.4.2?tab=readme-ov-file#about).

The model architecture that we carefully tested for vLLM (in CI):

- Falcon
- Gemma
- GPT-NeoX
- LLAMA
- LLAMA with AWQ
- Mistral
- Mixtral
- Phi
- Starcoder

### Complete model set

Text Generation Models

- Aquila & Aquila2 (`BAAI/AquilaChat2-7B`, `BAAI/AquilaChat2-34B`, `BAAI/Aquila-7B`, `BAAI/AquilaChat-7B`, etc.)
- Arctic (`Snowflake/snowflake-arctic-base`, `Snowflake/snowflake-arctic-instruct`, etc.)
- Baichuan & Baichuan2 (`baichuan-inc/Baichuan2-13B-Chat`, `baichuan-inc/Baichuan-7B`, etc.)
- BLOOM (`bigscience/bloom`, `bigscience/bloomz`, etc.)
- ChatGLM (`THUDM/chatglm2-6b`, `THUDM/chatglm3-6b`, etc.)
- Command-R (`CohereForAI/c4ai-command-r-v01`, etc.)
- DBRX (`databricks/dbrx-base`, `databricks/dbrx-instruct` etc.)
- DeciLM (`Deci/DeciLM-7B`, `Deci/DeciLM-7B-instruct`, etc.)
- Falcon & Falcon2 (`tiiuae/falcon-7b`, `tiiuae/falcon-11b`, `tiiuae/falcon-40b`, `tiiuae/falcon-rw-7b`, etc.)
- Gemma (`google/gemma-2b`, `google/gemma-7b`, etc.)
- Gemma2 (`google/gemma-2-9b`, `google/gemma-2-27b`, etc.)
- GPT-2 (`gpt2`, `gpt2-xl`, etc.)
- GPT BigCode (`bigcode/starcoder`, `bigcode/gpt_bigcode-santacoder`, etc.)
- GPT-J (`EleutherAI/gpt-j-6b`, `nomic-ai/gpt4all-j`, etc.)
- GPT-NeoX (`EleutherAI/gpt-neox-20b`, `databricks/dolly-v2-12b`, `stabilityai/stablelm-tuned-alpha-7b`, etc.)
- InternLM (`internlm/internlm-7b`, `internlm/internlm-chat-7b`, etc.)
- InternLM2 (`internlm/internlm2-7b`, `internlm/internlm2-chat-7b`, etc.)
- Jais (`core42/jais-13b`, `core42/jais-13b-chat`, `core42/jais-30b-v3`, `core42/jais-30b-chat-v3`, etc.)
- Jamba (`ai21labs/Jamba-v0.1`, etc.)
- LLaMA, Llama 2, Llama 3, Llama 3.1 (`meta-llama/Meta-Llama-3.1-405B-Instruct`, `meta-llama/Meta-Llama-3.1-70B`, `meta-llama/Meta-Llama-3-70B-Instruct`, `meta-llama/Llama-2-70b-hf`, `01-ai/Yi-34B`, etc.)
- MiniCPM (`openbmb/MiniCPM-2B-sft-bf16`, `openbmb/MiniCPM-2B-dpo-bf16`, etc.)
- Mistral (`mistralai/Mistral-7B-v0.1`, `mistralai/Mistral-7B-Instruct-v0.1`, etc.)
- Mixtral (`mistralai/Mixtral-8x7B-v0.1`, `mistralai/Mixtral-8x7B-Instruct-v0.1`, `mistral-community/Mixtral-8x22B-v0.1`, etc.)
- MPT (`mosaicml/mpt-7b`, `mosaicml/mpt-30b`, etc.)
- OLMo (`allenai/OLMo-1B-hf`, `allenai/OLMo-7B-hf`, etc.)
- OPT (`facebook/opt-66b`, `facebook/opt-iml-max-30b`, etc.)
- Orion (`OrionStarAI/Orion-14B-Base`, `OrionStarAI/Orion-14B-Chat`, etc.)
- Phi (`microsoft/phi-1_5`, `microsoft/phi-2`, etc.)
- Phi-3 (`microsoft/Phi-3-mini-4k-instruct`, `microsoft/Phi-3-mini-128k-instruct`, etc.)
- Qwen (`Qwen/Qwen-7B`, `Qwen/Qwen-7B-Chat`, etc.)
- Qwen2 (`Qwen/Qwen1.5-7B`, `Qwen/Qwen1.5-7B-Chat`, etc.)
- Qwen2MoE (`Qwen/Qwen1.5-MoE-A2.7B`, `Qwen/Qwen1.5-MoE-A2.7B-Chat`, etc.)
- StableLM(`stabilityai/stablelm-3b-4e1t`, `stabilityai/stablelm-base-alpha-7b-v2`, etc.)
- Starcoder2(`bigcode/starcoder2-3b`, `bigcode/starcoder2-7b`, `bigcode/starcoder2-15b`, etc.)
- Xverse (`xverse/XVERSE-7B-Chat`, `xverse/XVERSE-13B-Chat`, `xverse/XVERSE-65B-Chat`, etc.)

Multi Modal Models

- Chameleon (`facebook/chameleon-7b` etc.)
- Fuyu (`adept/fuyu-8b` etc.)
- LlaVA-1.5 (`llava-hf/llava-1.5-7b-hf`, `llava-hf/llava-1.5-13b-hf`, etc.)
- LlaVA-NeXT (`llava-hf/llava-v1.6-mistral-7b-hf`, `llava-hf/llava-v1.6-vicuna-7b-hf`, etc.)
- PaliGemma (`google/paligemma-3b-pt-224`, `google/paligemma-3b-mix-224`, etc.)
- Phi-3-Vision (`microsoft/Phi-3-vision-128k-instruct`, etc.)

We will add more model support for the future versions to have them tested. Please feel free to [file us an issue](https://github.com/deepjavalibrary/djl-serving/issues/new/choose) for more model coverage in CI.

### Quantization

Currently, we allow customer to use `option.quantize=awq` or `OPTION_QUANTIZE=awq` to load an AWQ quantized model in VLLM.

We will have GPTQ supported for vLLM in the upcoming version.

## Quick Start Configurations 

You can leverage `vllm` with LMI using the following starter configurations:

### serving.properties

```
engine=Python
option.tensor_parallel_degree=max
option.model_id=<your model>
option.rolling_batch=vllm
# Adjust the following based on model size and instance type
option.max_rolling_batch_size=64
```

You can follow [this example](../deployment_guide/deploying-your-endpoint.md#configuration---servingproperties) to deploy a model with serving.properties configuration on SageMaker.

### environment variables 

```
HF_MODEL_ID=<your model>
TENSOR_PARALLEL_DEGREE=max
OPTION_ROLLING_BATCH=vllm
# Adjust the following based on model size and instance type
OPTION_MAX_ROLLING_BATCH_SIZE=64
```

You can follow [this example](../deployment_guide/deploying-your-endpoint.md#configuration---environment-variables) to deploy a model with environment variable configuration on SageMaker.

### LoRA Adapter Support

vLLM has support for LoRA adapters using the [adapters API](../../adapters.md).
In order to use the adapters, you must begin by enabling them by setting `option.enable_lora=true`.
Following that, you can configure the LoRA support through the additional settings `option.max_loras`, `option.max_lora_rank`, `option.lora_extra_vocab_size`, and `option.max_cpu_loras`.
If you run into OOM by enabling adapter support, reduce the `option.gpu_memory_utilization`.

### Advanced vLLM Configurations

The following table lists the advanced configurations that are available with the vLLM backend.
There are two types of advanced configurations: `LMI`, and `Pass Through`.
`LMI` configurations are processed by LMI and translated into configurations that vLLM uses.
`Pass Through` configurations are passed directly to the backend library. These are opaque configurations from the perspective of the model server and LMI.
We recommend that you file an [issue](https://github.com/deepjavalibrary/djl-serving/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=) for any issues you encounter with configurations.
For `LMI` configurations, if we determine an issue with the configuration, we will attempt to provide a workaround for the current released version, and attempt to fix the issue for the next release.
For `Pass Through` configurations it is possible that our investigation reveals an issue with the backend library.
In that situation, there is nothing LMI can do until the issue is fixed in the backend library.

| Item                                    | LMI Version | Configuration Type | Description                                                                                                                                                                                                                                                                                                                                                                  | Example value         |
|-----------------------------------------|-------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| option.quantize                         | \>= 0.26.0  | LMI                | Quantize the model with the supported quantization methods. LMI uses this to set the right quantization configs in VLLM                                                                                                                                                                                                                                                      | `awq` Default: `None` |
| option.max_rolling_batch_prefill_tokens | \>= 0.26.0  | LMI                | Limits the number of tokens for prefill(a.k.a prompt processing). This needs to be tuned based on GPU memory available and request lengths. Setting this value too high can limit the number of kv cache blocks or run into OOM. If you don't set this, `vllm` will default to max model length from Hugging Face config(also accounts for rope scaling if applicable).      | Default: `None`       |
| option.max_model_len                    | \>= 0.26.0  | Pass Through       | the maximum length (input+output) vLLM should preserve memory for. If not specified, will use the default length the model is capable in config.json. Sometimes model's maximum length could go to 32k (Mistral 7B) and way beyond the supported KV token size. In that case to deploy on a small instance, we need to adjust this value within the range of KV Cache limit. | Default: `None`       |
| option.load_format                      | \>= 0.26.0  | Pass Through       | The checkpoint format of the model. Default is auto and means bin/safetensors will be used if found.                                                                                                                                                                                                                                                                         | Default: `auto`       |
| option.enforce_eager                    | \>= 0.27.0  | Pass Through       | vLLM by default will run with CUDA graph optimization to reach to the best performance. However, in the situation of very less GPU memory, having CUDA graph enabled will cause OOM. So if you set this option to true, we will use PyTorch Eager mode and disable CUDA graph to save some GBs of memory.                                                                    | Default: `False`      |
| option.gpu_memory_utilization           | \>= 0.27.0  | Pass Through       | This config controls the amount of GPU memory allocated to KV cache. Setting higher value will allocate more memory for KV cache.Default is 0.9. It recommended to reduce this value if GPU OOM's are encountered.                                                                                                                                                           | Default: `0.9`        |
| option.enable_lora                      | \>= 0.27.0  | Pass Through       | This config enables support for LoRA adapters.                                                                                                                                                                                                                                                                                                                               | Default: `false`      |
| option.max_loras                        | \>= 0.27.0  | Pass Through       | This config determines the maximum number of LoRA adapters that can be run at once. Allocates GPU memory for those number of adapters.                                                                                                                                                                                                                                       | Default: `4`          |
| option.max_lora_rank                    | \>= 0.27.0  | Pass Through       | This config determines the maximum rank allowed for a LoRA adapter. Set this value to maximum rank of your adapters. Setting a larger value will enable more adapters at a greater memory usage cost.                                                                                                                                                                        | Default: `16`         |
| option.lora_extra_vocab_size            | \>= 0.27.0  | Pass Through       | This config determines the maximum additional vocabulary that can be added through a LoRA adapter.                                                                                                                                                                                                                                                                           | Default: `256`        |
| option.max_cpu_loras                    | \>= 0.27.0  | Pass Through       | This config determines the maximum number of LoRA adapters to cache in memory. All others will be evicted to disk.                                                                                                                                                                                                                                                           | Default: `None`       |
| option.enable_chunked_prefill           | \>= 0.29.0  | Pass Through       | This config enables chunked prefill support. With chunked prefill, longer prompts will be chunked and batched with decode requests to reduce inter token latency. This option is EXPERIMENTAL and tested for llama and falcon models only. This does not work with LoRA and speculative decoding yet.                                                                        | Default: `None`       |
| option.cpu_offload_gb_per_gpu           | \>= 0.29.0  | Pass Through       | This config allows offloading model weights into CPU to enable large model running with limited GPU memory.                                                                                                                                                                                                                                                                  | Default: `0`          |
| option.enable_prefix_caching            | \>= 0.29.0  | Pass Through       | This config allows the engine to cache the context memory and reuse to speed up inference.                                                                                                                                                                                                                                                                                   | Default: `False`      |
| option.disable_sliding_window           | \>= 0.30.0  | Pass Through       | This config disables sliding window, capping to sliding window size inference.                                                                                                                                                                                                                                                                                               | Default: `False`      |
| option.tokenizer_mode                   | \>= 0.30.0  | Pass Through       | This config sets the tokenizer mode for vllm. When using mistral models with mistral tokenizers, you must set this to `mistral` explicitly.                                                                                                                                                                                                                                  | Default: `auto`       |

