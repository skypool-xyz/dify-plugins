from collections.abc import Generator
from typing import Optional, Union

from dify_plugin import OAICompatLargeLanguageModel
from dify_plugin.entities.model import ModelFeature
from dify_plugin.entities.model.llm import LLMResult
from dify_plugin.entities.model.message import PromptMessage, PromptMessageTool


DEFAULT_ENDPOINT_URL = "https://a.skypool.xyz/v1"


class SkypoolLargeLanguageModel(OAICompatLargeLanguageModel):
    @staticmethod
    def _normalize_endpoint_url(endpoint_url: str | None) -> str:
        endpoint = (endpoint_url or DEFAULT_ENDPOINT_URL).strip().rstrip("/")
        if not endpoint:
            endpoint = DEFAULT_ENDPOINT_URL
        if not endpoint.endswith("/v1"):
            endpoint = f"{endpoint}/v1"
        return endpoint

    def _update_credential(self, model: str, credentials: dict) -> None:
        credentials["endpoint_url"] = self._normalize_endpoint_url(credentials.get("endpoint_url"))
        credentials["mode"] = self.get_model_mode(model).value
        credentials["endpoint_model_name"] = model

        schema = self.get_model_schema(model, credentials)
        if schema and {
            ModelFeature.TOOL_CALL,
            ModelFeature.MULTI_TOOL_CALL,
        }.intersection(schema.features or []):
            credentials["function_calling_type"] = "tool_call"

    def _invoke(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        model_parameters: dict,
        tools: Optional[list[PromptMessageTool]] = None,
        stop: Optional[list[str]] = None,
        stream: bool = True,
        user: Optional[str] = None,
    ) -> Union[LLMResult, Generator]:
        self._update_credential(model, credentials)
        return self._generate(
            model,
            credentials,
            prompt_messages,
            model_parameters,
            tools,
            stop,
            stream,
            user,
        )

    def validate_credentials(self, model: str, credentials: dict) -> None:
        self._update_credential(model, credentials)
        return super().validate_credentials(model, credentials)

    def _generate(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        model_parameters: dict,
        tools: Optional[list[PromptMessageTool]] = None,
        stop: Optional[list[str]] = None,
        stream: bool = True,
        user: Optional[str] = None,
    ) -> Union[LLMResult, Generator]:
        self._update_credential(model, credentials)
        return super()._generate(
            model,
            credentials,
            prompt_messages,
            model_parameters,
            tools,
            stop,
            stream,
            user,
        )

    def _wrap_thinking_by_reasoning_content(self, delta: dict, is_reasoning: bool) -> tuple[str, bool]:
        reasoning_piece = delta.get("reasoning") or delta.get("reasoning_content") or ""
        content_piece = delta.get("content") or ""
        output = ""

        if reasoning_piece:
            if not is_reasoning:
                output += f"<think>\n{reasoning_piece}"
                is_reasoning = True
            else:
                output += str(reasoning_piece)

        if is_reasoning:
            if not reasoning_piece and not content_piece:
                is_reasoning = False
                output += "\n</think>"
            if content_piece:
                is_reasoning = False
                output += f"\n</think>{content_piece}"
        elif content_piece:
            output += content_piece

        return output, is_reasoning
