# Generated by Django 3.0 on 2024-11-07 18:09

from django.db import migrations


def copy_profile_entities(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )

def reverse_copy_profile_entities(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for new_profile in NewProfile.objects.all():
        OldProfile.objects.create(
            id=new_profile.id,
            user=new_profile.user,
            favorite_city=new_profile.favorite_city
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0002_remove_reverse_accessors_for_refactoring'),
    ]

    operations = [
        migrations.RunPython(copy_profile_entities, reverse_code=reverse_copy_profile_entities),
    ]
