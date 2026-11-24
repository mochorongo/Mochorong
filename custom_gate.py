class CustomGate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "enabled": ("BOOLEAN", {"default": True}),
                "in1": ("IMAGE",),
                "in2": ("MASK",),
            },
            "optional": {
                "else1": ("IMAGE",),
                "else2": ("MASK",),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("out1", "out2")
    FUNCTION = "route"
    CATEGORY = "Mochorong"

    def route(self, enabled, in1, in2, else1=None, else2=None):
        if enabled:
            return (in1, in2)
        return (else1, else2)
