# ─────────────────────────────────────────────
# Mochorong — Custom ComfyUI Nodes
# ─────────────────────────────────────────────

from .load_image_optional import LoadImageOptional
from .audio_selector import AudioSelector
from .audio_gate import AudioGate
from .intfloat_node import IntFloatNode
from .custom_gate import CustomGate

NODE_CLASS_MAPPINGS = {
    "AudioSelector": AudioSelector,
    "AudioGate": AudioGate,
    "Int and Float": IntFloatNode,
    "Custom Gate": CustomGate,
    "LoadImageOptional": LoadImageOptional,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AudioSelector": "Audio Selector",
    "AudioGate": "Audio Gate",
    "Int and Float": "Int and Float",
    "Custom Gate": "Custom Gate",
    "LoadImageOptional": "Load Image Optional",
}

