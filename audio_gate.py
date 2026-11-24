import torch


class AudioGate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "enabled": ("BOOLEAN", {"default": True}),
                "audio": ("AUDIO",),
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "gate"
    CATEGORY = "Mochorong"

    def gate(self, enabled, audio):
        if enabled:
            return (audio,)
        silent = {
            "waveform": torch.zeros_like(audio["waveform"]),
            "sample_rate": audio["sample_rate"],
        }
        return (silent,)
