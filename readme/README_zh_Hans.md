# 天池 Token

天池 Token 是面向 Dify 的模型供应商插件，用于通过天池 Token 的 OpenAI 兼容接口调用平台模型。用户只需要在 Dify 中配置 Consumer API Key，即可在应用、工作流和 Agent 中使用天池 Token 模型。

## 官方资源

- 官网：https://skypool.xyz/
- 开发者文档：https://skypool.xyz/docs
- Dify 接入指南：https://skypool.xyz/docs/dify
- Consumer 控制台：https://skypool.xyz/console/consumer
- 模型列表：https://skypool.xyz/models
- Playground：https://skypool.xyz/console/consumer/lab/playground

天池 Token 提供 OpenAI 兼容 API，适合应用开发者和 AI 工具接入。开发者文档包含 Consumer API Key 创建、统一 `baseURL`、模型选择、流式响应、调用记录以及常见工具接入说明。

## 功能

- 内置天池 Token 当前线上聊天模型。
- 支持 OpenAI 兼容的 Chat Completions。
- 支持流式输出。
- 支持工具调用和多工具调用。
- 支持自定义 endpoint URL，便于接入私有或预发环境。

## 配置方式

1. 打开天池 Token Consumer 控制台：https://skypool.xyz/console/consumer
2. 创建或复制 Consumer API Key。
3. 在 Dify 中添加 Skypool 模型供应商。
4. 填入 Consumer API Key。
5. 默认 endpoint URL 为 `https://a.skypool.xyz/v1`，除非你使用其他天池 Token 兼容环境，否则无需修改。
6. 如需完整接入流程和 Dify 截图指引，请阅读 https://skypool.xyz/docs 和 https://skypool.xyz/docs/dify。

## 内置模型

当前版本内置以下模型：

- `qwen3.6:35b`
- `qwen3.5:9b`
- `gemma4:26b`
- `qwen3.5:122b`

## 说明

插件会把 Dify 的提示词、模型参数、工具定义，以及 Dify OpenAI 兼容模型接口支持的输入转发到配置的天池 Token endpoint。计费、额度、模型可用性和请求日志由天池 Token 平台管理。需要最新 endpoint、模型能力或接入说明时，请以天池 Token 文档为准。

## 支持

- 天池 Token 官网：https://skypool.xyz/
- 天池 Token 文档：https://skypool.xyz/docs
- 源码仓库：https://github.com/skypool-xyz/dify-plugin
- 问题反馈与联系：https://github.com/skypool-xyz/dify-plugin/issues
