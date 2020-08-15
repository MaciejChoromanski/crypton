# Generated by Django 3.0.8 on 2020-08-11 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200727_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_friend_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_friend_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_new', models.BooleanField(default=True)),
                ('sent_on', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_message', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
