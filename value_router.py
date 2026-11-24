class AnyType(str):
    def __ne__(self, other):
        return False

ANY = AnyType("*")


class ValueRouter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "steps":      ("INT", {"default": 4, "min": 1, "max": 100000}),
                "match_1":    ("INT", {"default": 4, "min": 1, "max": 100000}),
                "sigma_1":    (ANY,),   # sai quando steps == match_1
                "match_2":    ("INT", {"default": 6, "min": 1, "max": 100000}),
                "sigma_2":    (ANY,),   # sai quando steps == match_2
                "sigma_else": (ANY,),   # qualquer outro caso
            }
        }

    RETURN_TYPES = (ANY, "STRING")
    RETURN_NAMES = ("sigmas", "full_attention_layers")
    FUNCTION = "run"
    CATEGORY = "Mochorong"

    def run(self, steps, match_1, sigma_1, match_2, sigma_2, sigma_else):
        layers = ",".join(str(i) for i in sorted({0, 1, steps - 1}))
        if steps == match_1:
            sigmas = sigma_1
        elif steps == match_2:
            sigmas = sigma_2
        else:
            sigmas = sigma_else
        return (sigmas, layers)