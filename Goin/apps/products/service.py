def compress_image(self):
    from PIL import Image
    if self.image:
        img = Image.open(self.image.path)
        if img != 'null' or img != "None":
            img = img.convert('RGB')
            img.thumbnail((800, 800))
            img.save(self.image.path, 'JPEG', quality=90)
        else:
            pass
    else:
        pass
