from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str
    GLOBAL_CONFIG_PATH: str = "TG_FARM"

    FIX_CERT: bool = False

    TRACK_BOT_UPDATES: bool = True

    REF_ID: str = "Ut0WvEGu3WPMNDga"

    PERFORM_QUESTS: bool = True
    CHANNEL_SUBSCRIBE_TASKS: bool = True
    UPGRADE_CARDS: bool = True
    SPIN_THE_WHEEL: bool = True
    AUTO_TAP: bool = True

    RANDOM_SLEEP_TIME: list[int] = [3600, 10800]

    SESSION_START_DELAY: int = 360

    SESSIONS_PER_PROXY: int = 1
    USE_PROXY_FROM_FILE: bool = False
    DISABLE_PROXY_REPLACE: bool = False
    USE_PROXY_CHAIN: bool = False

    DEVICE_PARAMS: bool = False

    DEBUG_LOGGING: bool = False


settings = Settings()
