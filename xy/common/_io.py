from io import BytesIO


class RayBytesIO:
    @classmethod
    def pil_image_to_bytes_with_memory(cls, pil_image_cls, img_type):
        memory = BytesIO()
        pil_image_cls.save(memory, img_type)
        _return = memory.getvalue()
        if not memory.closed:
            memory.close()
        return _return


