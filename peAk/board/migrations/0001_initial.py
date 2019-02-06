# Generated by Django 2.1.5 on 2019-02-06 19:15

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
            name='PeakUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=64)),
                ('user_firstName', models.CharField(max_length=64)),
                ('user_lastName', models.CharField(max_length=64)),
                ('user_fav_resort', models.CharField(blank=True, max_length=128)),
                ('user_date_of_birth', models.DateField()),
                ('user_profile_picture', models.FileField(blank=True, upload_to='uploads/')),
                ('user_date_joined', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=64)),
                ('resort_location_longitude', models.CharField(max_length=64)),
                ('resort_location_latitude', models.CharField(max_length=64)),
                ('resort_address_line1', models.CharField(max_length=64)),
                ('resort_address_line2', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('resort_address_city', models.CharField(max_length=64)),
                ('resort_address_zip_code', models.IntegerField()),
                ('resort_website_url', models.CharField(blank=True, max_length=128)),
                ('resort_altitude', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('AK', 'AK'), ('AS', 'AS'), ('AZ', 'AZ'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('GU', 'GU'), ('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'), ('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MP', 'MP'), ('MS', 'MS'), ('MT', 'MT'), ('NA', 'NA'), ('NC', 'NC'), ('ND', 'ND'), ('NE', 'NE'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('PR', 'PR'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VA', 'VA'), ('VI', 'VI'), ('VT', 'VT'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY')], max_length=2)),
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
                ('team_administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.PeakUser')),
                ('team_resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Resort')),
            ],
        ),
        migrations.AddField(
            model_name='resort',
            name='resort_address_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.State'),
        ),
        migrations.AddField(
            model_name='resort',
            name='resort_teams',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
        migrations.AddField(
            model_name='peakuser',
            name='user_groups_belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='message_board_teams',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
        migrations.AddField(
            model_name='message',
            name='message_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.PeakUser'),
        ),
    ]
