# Skypool

Skypool is a Dify model provider plugin for the Skypool OpenAI-compatible API. It lets Dify users call Skypool chat models with a Skypool Consumer API key.

## Resources

- [Website](https://skypool.xyz/)
- [Developer docs](https://skypool.xyz/docs)
- [Dify integration guide](https://skypool.xyz/docs/dify)
- [Consumer console](https://skypool.xyz/console/consumer)
- [Model list](https://skypool.xyz/models)
- [Playground](https://skypool.xyz/console/consumer/lab/playground)

Skypool Token provides an OpenAI-compatible API for application developers and AI tools. The developer docs cover Consumer API key creation, the unified `baseURL`, model selection, streaming responses, request activity records, and common integration guides.

## Features

- Predefined Skypool chat models.
- OpenAI-compatible chat completions.
- Streaming output.
- Tool calling and multi-tool calling for supported Skypool models.
- Optional custom endpoint URL for private or staging Skypool deployments.

## Configuration

1. Open the [Skypool consumer console](https://skypool.xyz/console/consumer).
2. Create or copy a Consumer API key.
3. Add the Skypool provider in Dify.
4. Enter the Consumer API key.
5. Keep the default endpoint URL, `https://a.skypool.xyz/v1`, unless you use another Skypool-compatible deployment.
6. For detailed onboarding and Dify-specific screenshots, read the [developer docs](https://skypool.xyz/docs) and [Dify integration guide](https://skypool.xyz/docs/dify).

## Models

This plugin currently includes these predefined models:

- `qwen3.6:35b`
- `qwen3.5:9b`
- `gemma4:26b`
- `qwen3.5:122b`

## Notes

The plugin forwards prompts, model parameters, tool definitions, and files supported by Dify's OpenAI-compatible model interface to the configured Skypool endpoint. Billing, quotas, model availability, and request logs are managed by Skypool. Check the Skypool docs when you need the latest endpoint guidance, model capabilities, or integration notes.

## Support

- Skypool website: https://skypool.xyz/
- Skypool docs: https://skypool.xyz/docs
- Source repository: https://github.com/skypool-xyz/dify-plugins
- Issues and contact: https://github.com/skypool-xyz/dify-plugins/issues
