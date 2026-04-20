from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
load_dotenv()

try:
    from langfuse.decorators import observe, langfuse_context
    print(f"DEBUG: Langfuse decorators imported successfully. Keys present: {bool(os.getenv('LANGFUSE_PUBLIC_KEY'))}")
except Exception as e:
    print(f"DEBUG: Langfuse import FAILED: {e}. Using dummy fallback.")
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

    langfuse_context = _DummyContext()


def tracing_enabled() -> bool:
    has_keys = bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
    print(f"DEBUG: tracing_enabled check: {has_keys}")
    return has_keys
