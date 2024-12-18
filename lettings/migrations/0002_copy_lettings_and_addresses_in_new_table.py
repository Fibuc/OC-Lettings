# Generated by Django 3.0 on 2024-11-07 18:09

from django.db import migrations


def copy_address_entities(ModelFrom, ModelTo):
    for address_entity in ModelFrom.objects.all():
        ModelTo.objects.create(
            id=address_entity.id,
            number=address_entity.number,
            street=address_entity.street,
            city=address_entity.city,
            state=address_entity.state,
            zip_code=address_entity.zip_code,
            country_iso_code=address_entity.country_iso_code,
        )


def copy_lettings_entities(ModelFrom, ModelTo, ModelAddress):
    for letting_entity in ModelFrom.objects.all():
        ModelTo.objects.create(
            id=letting_entity.id,
            title=letting_entity.title,
            address=ModelAddress.objects.get(id=letting_entity.address.pk)
        )


def copy_lettings_and_address_entities(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    copy_address_entities(OldAddress, NewAddress)
    copy_lettings_entities(OldLetting, NewLetting, NewAddress)


def reverse_copy_lettings_and_address_entities(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    copy_address_entities(NewAddress, OldAddress)
    copy_lettings_entities(NewLetting, OldLetting, OldAddress)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0002_remove_reverse_accessors_for_refactoring'),
    ]

    operations = [
        migrations.RunPython(copy_lettings_and_address_entities, reverse_code=reverse_copy_lettings_and_address_entities),
    ]
