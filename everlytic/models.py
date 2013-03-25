from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

import .api


class EverlyticProfile(models.Model):
    user = models.OneToOneField(User)
    # the Neo consumer id used in API requests
    everlytic_id = models.PositiveIntegerField()


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    """ Create an EverlyticProfile and subscribe to the appropriate mailing
    list on the Everlytic service. Store the Everlytic user id in the
    profile.
    """
    import pdb; pdb.set_trace()
    if created and not EverlyticProfile.objects.exists(user=instance):
        ep = EverlyticProfile.objects.create(user=instance)
        ep.erverlytic_id = api.subscribeUser(instance)
        ep.save()


@receiver(pre_delete, sender=User)
def user_pre_delete(sender, instance, **kwargs):
    """ Delete the EverlyticProfile and unsubscribe from the appropriate mailing
    list on the Everlytic service. Delete the user from the Everlytic
    database.
    """
    import pdb; pdb.set_trace()
    try:
        ep = EverlyticProfile.objects.get(user=instance)
        api.unsubscribeUser(ep.everlytic_id)
        ep.delete()
    except EverlyticProfile.DoesNotExist:
        pass
