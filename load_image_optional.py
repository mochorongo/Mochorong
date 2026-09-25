@ -13,16 +13,17 @@ class LoadImageOptional:
        ))
        return {
            "required": {
                "image": (["None"] + files, {"image_upload": True}),
                "enabled": ("BOOLEAN", {"default": True}),
                "image": (files, {"image_upload": True}),
            },
        }

    RETURN_TYPES = ("image", "mask")
    FUNCTION = "load_image"
    CATEGORY = "image"
    CATEGORY = "Mochorong"

    def load_image(self, image):
        if image == "None":
    def load_image(self, enabled, image):
        if not enabled:
            return (None, None)

        image_path = folder_paths.get_annotated_filepath(image)
@ -43,16 +44,16 @@ class LoadImageOptional:
        return (image_out, mask)

    @classmethod
    def IS_CHANGED(s, image):
        if image == "None":
            return "none"
    def IS_CHANGED(s, enabled, image):
        if not enabled:
            return "disabled"
        image_path = folder_paths.get_annotated_filepath(image)
        from comfy.utils import calculate_file_hash
        return calculate_file_hash(image_path)

    @classmethod
    def VALIDATE_INPUTS(s, image):
        if image == "None":
    def VALIDATE_INPUTS(s, enabled, image):
        if not enabled:
            return True
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)
