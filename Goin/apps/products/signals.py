from django.db.models.signals import post_save
from .models import Product

MODELS_TO_COMPRESS = [Product, ]


def compress_images(sender, instance, created, **kwargs):
    if created:
        instance.compress_image()

    for model in MODELS_TO_COMPRESS:
        post_save.connect(compress_images, sender=model)
