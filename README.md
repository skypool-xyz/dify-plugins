# Skypool

Skypool is a Dify model provider plugin for the Skypool OpenAI-compatible API. It lets Dify users call Skypool chat models with a Skypool Consumer API key.

## Features

- Predefined Skypool chat models.
- OpenAI-compatible chat completions.
- Streaming output.
- Tool calling and multi-tool calling for supported Skypool models.
- Optional custom endpoint URL for private or staging Skypool deployments.

## Configuration

1. Open the Skypool consumer console.
2. Create or copy a Consumer API key.
3. Add the Skypool provider in Dify.
4. Enter the Consumer API key.
5. Keep the default endpoint URL, `https://a.skypool.xyz/v1`, unless you use another Skypool-compatible deployment.

## Models

The first release includes these predefined models:

- `qwen3.6:35b`
- `qwen3.5:9b`
- `gemma4:26b`
- `qwen3.5:122b`

## Notes

The plugin forwards prompts, model parameters, tool definitions, and files supported by Dify's OpenAI-compatible model interface to the configured Skypool endpoint. Billing, quotas, model availability, and request logs are managed by Skypool.

## Support

- Source repository: https://github.com/Azard/dify-plugin-skypool
- Issues and contact: https://github.com/Azard/dify-plugin-skypool/issues
