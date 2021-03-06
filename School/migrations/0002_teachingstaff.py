# Generated by Django 3.0.3 on 2020-03-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherSlug', models.SlugField()),
                ('teacherFirstName', models.CharField(max_length=100)),
                ('teacherLastName', models.CharField(max_length=100)),
                ('teacherSubjectName', models.CharField(max_length=300)),
                ('teacherFatherName', models.CharField(max_length=100)),
                ('teacherDateOfJoining', models.DateField()),
                ('teacherDateOfBirth', models.DateField()),
                ('teacherImage', models.ImageField(upload_to='')),
                ('teacherExperince', models.IntegerField(max_length=1)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
