from apps.person_info.models import ModelActionLog
from django.db.models.signals import post_save, post_delete, pre_syncdb
from django.dispatch import receiver
from south.signals import pre_migrate

EXCLUDE_LIST = ['ModelActionLog', 'RequestLogger', 'LogEntry']

IS_MIGRATING = False

@receiver(post_save)
def object_save_log(sender, created, instance, **kwargs):
    """"Write information about created or updated object"""
    if IS_MIGRATING:
        return
    if instance.__class__.__name__ in EXCLUDE_LIST:
        return
    action = 0 if created else 1
    ModelActionLog.objects.create(inst=instance.__class__.__name__,
                                  action=action)


@receiver(post_delete)
def object_delete_log(sender, instance, **kwargs):
    """"Write information about deleted or updated object"""
    if IS_MIGRATING:
        return
    if instance.__class__.__name__ in EXCLUDE_LIST:
        return
    ModelActionLog.objects.create(inst=instance.__class__.__name__,
                                  action=2)


@receiver(pre_migrate)
@receiver(pre_syncdb)
def disable_signals_during_migration(sender, **kwargs):
    global IS_MIGRATING
    IS_MIGRATING = True
