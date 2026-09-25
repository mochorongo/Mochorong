import os
import folder_paths
import numpy as np
from PIL import Image, ImageOps
import torch

class LoadImageOptional:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = sorted(folder_paths.filter_files_content_types(
            os.listdir(input_dir), ["image"]
        ))
        return {
            "required": {
                "enabled": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
            },
            "optional": {
                "image": (["None"] + files, {"image_upload": True}),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "load_image"
    CATEGORY = "Mochorong"

    def load_image(self, enabled=True, image=None):
        if not enabled or image is None or image == "None":
            return (None, None)

        image_path = folder_paths.get_annotated_filepath(image)
        img = Image.open(image_path)
        img = ImageOps.exif_transpose(img)
        if img.mode == "I":
            img = img.point(lambda i: i * (1.0 / 65535))
        image_out = img.convert("RGB")
        image_out = np.array(image_out).astype(np.float32) / 255.0
        image_out = torch.from_numpy(image_out)[None,]

        if "A" in img.getbands():
            mask = np.array(img.getchannel("A")).astype(np.float32) / 255.0
            mask = 1.0 - torch.from_numpy(mask)
        else:
            mask = torch.zeros((image_out.shape[1], image_out.shape[2]), dtype=torch.float32)

        return (image_out, mask)

    @classmethod
    def IS_CHANGED(s, enabled=True, image=None):
        if not enabled or image is None or image == "None":
            return "none"
        image_path = folder_paths.get_annotated_filepath(image)
        from comfy.utils import calculate_file_hash
        return calculate_file_hash(image_path)

    @classmethod
    def VALIDATE_INPUTS(s, enabled=True, image=None):
        if not enabled or image is None or image == "None":
            return True
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)
        return True
