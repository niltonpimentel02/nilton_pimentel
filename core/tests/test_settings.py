import os
import subprocess
import sys


def test_sentry_initializes_with_production_settings():
    env = {**os.environ, 'DEBUG': 'False', 'SENTRY_DSN': ''}
    subprocess.run(
        [
            sys.executable,
            '-c',
            """
import logging
import nilton_pimentel.settings
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

client = sentry_sdk.get_client()
data_collection = client.options["data_collection"]
assert data_collection["user_info"] is True
assert data_collection["http_bodies"] == []
assert data_collection["database_query_data"] is False
assert data_collection["stack_frame_variables"] is False
integration = client.get_integration(LoggingIntegration)
assert integration is not None
assert integration._event_handler.level == logging.ERROR
assert integration._logs_handler.level == logging.INFO
""",
        ],
        env=env,
        check=True,
    )
