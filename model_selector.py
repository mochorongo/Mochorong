class ModelSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "select": (["Model 1", "Model 2", "Model 3", "Model 4"],),
                "int_1": ("INT", {"default": 0, "min": -999999, "max": 999999}),
                "int_2": ("INT", {"default": 0, "min": -999999, "max": 999999}),
                "int_3": ("INT", {"default": 0, "min": -999999, "max": 999999}),
                "int_4": ("INT", {"default": 0, "min": -999999, "max": 999999}),
            },
            "optional": {
                "Model 1": ("MODEL",),
                "Model 2": ("MODEL",),
                "Model 3": ("MODEL",),
                "Model 4": ("MODEL",),
            },
        }

    RETURN_TYPES = ("MODEL", "INT")
    RETURN_NAMES = ("model", "int_value")
    FUNCTION = "select_model"
    CATEGORY = "Mochorong"

    def select_model(self, select, int_1, int_2, int_3, int_4, **kwargs):
        model = kwargs.get(select)
        if model is None:
            raise ValueError(f"No model connected to '{select}' input")

        int_map = {
            "Model 1": int_1,
            "Model 2": int_2,
            "Model 3": int_3,
            "Model 4": int_4,
        }

        return (model, int_map[select])
