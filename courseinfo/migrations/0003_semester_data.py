# Generated by Django 2.1.5 on 2020-03-22 20:49

from django.db import migrations





SEMESTERS = [
    {
        'semester_name': '2020 - Summer',
    },
    {
        'semester_name': '2020 - Fall',
    },
    {
        'semester_name': '2021 - Spring',
    },
    {
        'semester_name': '2021 - Summer',
    },
    {
        'semester_name': '2021 - Fall',
    },
]


def add_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo','Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.create(
            semester_name = semester['semester_name']
        )

def remove_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo','Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.get(
            semester_name = semester['semester_name']
        )
        semester_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_auto_20200211_1940'),
    ]

    operations = [
        migrations.RunPython(
            add_semester_data,  # if migrate forward
            remove_semester_data,  # if migrate backward
        )
    ]

