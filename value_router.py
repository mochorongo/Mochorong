class AnyType(str):
    def __ne__(self, other):
        return False

ANY = AnyType("*")


class ValueRouter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "selected": ("INT", {"default": 1, "min": 1, "max": 4}),
                "sigma_1": (ANY,),
                "sigma_2": (ANY,),
                "sigma_3": (ANY,),
                "sigma_4": (ANY,),
            }
        }

    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("sigmas",)
    FUNCTION = "route"
    CATEGORY = "Mochorong"

    def route(self, selected, sigma_1, sigma_2, sigma_3, sigma_4):
        opts = [sigma_1, sigma_2, sigma_3, sigma_4]
        i = max(1, min(4, selected)) - 1   # protects out of 1-4 range
        return (opts[i],)