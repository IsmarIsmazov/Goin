from apps.tga.models import Admin
from asgiref.sync import sync_to_async


@sync_to_async
def remove_chat_id(external_id):
    try:
        admin = Admin.objects.get(external_id=external_id)
        admin.delete()
        return True
    except Admin.DoesNotExist:
        return False


@sync_to_async
def check_chat_id_exists(external_id):
    return Admin.objects.filter(external_id=external_id).exists()


@sync_to_async
def create_or_get_admin(chat_id, username):
    admin, created = Admin.objects.get_or_create(
        external_id=chat_id,
        name=username
    )
    return admin, created