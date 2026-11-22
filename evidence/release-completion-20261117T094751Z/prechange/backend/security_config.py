"""Security-sensitive environment parsing shared by the FastAPI application."""
from collections.abc import Mapping


def cors_origins_from_env(env: Mapping[str, str]) -> list[str]:
    """Return configured CORS origins and fail closed for production wildcards.

    Development keeps the historical wildcard default so local preview remains
    usable. Production must explicitly provide one or more concrete origins.
    """
    environment = (env.get("APP_ENV") or env.get("ENVIRONMENT") or "").strip().lower()
    production = environment in {"prod", "production"}
    raw = env.get("CORS_ORIGINS")
    if raw is None or not raw.strip():
        if production:
            raise ValueError("CORS_ORIGINS must list the trusted frontend origins in production")
        return ["*"]

    origins = [origin.strip() for origin in raw.split(",") if origin.strip()]
    if not origins:
        if production:
            raise ValueError("CORS_ORIGINS must list the trusted frontend origins in production")
        return ["*"]
    if production and "*" in origins:
        raise ValueError("Wildcard CORS is not allowed in production; configure explicit frontend origins")
    return origins
