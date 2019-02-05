# Generated by Django 2.1.5 on 2019-02-05 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=128)),
                ('message_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_board_name', models.CharField(max_length=16)),
                ('message_board_description', models.CharField(max_length=128)),
                ('message_board_messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Message')),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=64)),
                ('resort_location_lat', models.IntegerField()),
                ('resort_location_long', models.IntegerField()),
                ('resort_address_line1', models.CharField(max_length=64)),
                ('resort_address_line2', models.CharField(max_length=64)),
                ('resort_address_city', models.CharField(max_length=64)),
                ('resort_address_zip_code', models.IntegerField()),
                ('resort_website_url', models.CharField(max_length=128)),
                ('resort_altitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('states', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=128)),
                ('team_meet_date', models.DateField()),
                ('team_max_capacity', models.IntegerField()),
                ('team_description', models.CharField(max_length=128)),
                ('team_status', models.CharField(default='Active', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=128)),
                ('user_name_first', models.CharField(max_length=64)),
                ('user_name_last', models.CharField(max_length=64)),
                ('user_fav_resort', models.CharField(max_length=128)),
                ('user_date_of_birth', models.DateField()),
                ('user_profile_picture', models.FileField(upload_to='uploads/')),
                ('user_date_joined', models.DateField()),
                ('user_groups_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='team_administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.User'),
        ),
        migrations.AddField(
            model_name='team',
            name='team_resort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Resort'),
        ),
        migrations.AddField(
            model_name='resort',
            name='resort_address_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.State'),
        ),
        migrations.AddField(
            model_name='resort',
            name='resort_teams',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='message_board_teams',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
    ]
