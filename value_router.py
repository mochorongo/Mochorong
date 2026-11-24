class AnyType(str):
    def __ne__(self, other):
        return False

ANY = AnyType("*")


class ValueRouter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "selector":   ("INT", {"default": 4, "min": 0, "max": 100000}),
                "match_a":    ("INT", {"default": 6, "min": 0, "max": 100000}),
                "match_b":    ("INT", {"default": 4, "min": 0, "max": 100000}),
                "in_a":       (ANY,),   # output when selector == match_a
                "in_b":       (ANY,),   # output when selector == match_b
                "in_default": (ANY,),   # output otherwise
            }
        }

    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("out",)
    FUNCTION = "route"
    CATEGORY = "Mochorong"

    def route(self, selector, match_a, match_b, in_a, in_b, in_default):
        if selector == match_a:
            return (in_a,)
        if selector == match_b:
            return (in_b,)
        return (in_default,)