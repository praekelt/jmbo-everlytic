from celery import task

from foundry.models import Member

from everlytic import api


@task
def subscribe_user(member_id, profile_class):
    instance = Member.objects.get(pk=member_id)
    ep, created = profile_class.objects.get_or_create(member=instance)
    if created and instance.email:
        ep.everlytic_id = api.subscribeUser(
            instance.last_name,
            instance.first_name,
            instance.email,
            instance.receive_email,
            everlytic_id=ep.everlytic_id)
        ep.save()


@task
def delete_user(everlytic_id):
    api.deleteEverlyticUser(everlytic_id)
