class IntFloatNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 1.0}),
            },
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int", "float")
    FUNCTION = "process"
    CATEGORY = "Mochorong"

    def process(self, value):
        return (int(value), float(value))
