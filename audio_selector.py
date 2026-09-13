class AudioSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "select": (["Bass", "Drums", "Guitar", "Vocals"],),
            },
            "optional": {
                "Bass": ("AUDIO",),
                "Drums": ("AUDIO",),
                "Guitar": ("AUDIO",),
                "Vocals": ("AUDIO",),
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "select_audio"
    CATEGORY = "Mochorong"

    def select_audio(self, select, **kwargs):
        audio = kwargs.get(select)
        if audio is None:
            raise ValueError(f"No audio connected to '{select}' input")
        return (audio,)
