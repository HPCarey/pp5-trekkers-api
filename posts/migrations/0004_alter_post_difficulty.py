# Generated by Django 3.2.18 on 2023-05-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Challenging', 'Challenging'), ('Difficult', 'Difficult')], default='Easy', max_length=300),
        ),
    ]
