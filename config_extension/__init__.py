"""Plugin declaration for config_extension."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class ConfigExtensionConfig(PluginConfig):
    """Plugin configuration for the config_extension plugin."""

    name = "config_extension"
    verbose_name = "Config Extension"
    version = __version__
    author = "Network to Code, LLC"
    description = "Config Extension."
    base_url = "config-extension"
    required_settings = []
    min_version = "1.5.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = ConfigExtensionConfig  # pylint:disable=invalid-name
