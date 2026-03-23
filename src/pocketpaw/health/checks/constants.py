"""Shared constants for health check modules."""

from __future__ import annotations

import os

# Providers that do NOT require an Anthropic API key.
NON_ANTHROPIC_PROVIDERS = ("ollama", "openai_compatible", "gemini", "litellm", "openrouter")

# Providers that do NOT require an OpenAI API key.
NON_OPENAI_PROVIDERS = ("ollama", "openai_compatible", "litellm", "openrouter")


def _is_container_env() -> bool:
    """Return True when running inside a Docker container or Railway service."""
    if os.environ.get("RAILWAY_ENVIRONMENT") or os.environ.get("RAILWAY_SERVICE_ID"):
        return True
    if os.path.exists("/.dockerenv"):
        return True
    return False
