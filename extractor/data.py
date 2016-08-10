
class Image(object):

    def __init__(self, image_name):
        self.image_name = image_name
        
    @classmethod
    def create_with_image_name(cls, image_name):
        return cls(image_name)
