# Generated by Django 2.1.5 on 2019-02-08 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            ],
        ),
        migrations.CreateModel(
            name='PeakUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstName', models.CharField(blank=True, max_length=64, null=True)),
                ('user_lastName', models.CharField(blank=True, max_length=64, null=True)),
                ('user_date_of_birth', models.DateField(blank=True, null=True)),
                ('user_team_belong', models.TextField(blank=True, default='[]', null=True, verbose_name='Team')),
                ('bio', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=64)),
                ('resort_location_latitude', models.CharField(max_length=64)),
                ('resort_location_longitude', models.CharField(max_length=64)),
                ('resort_address_line1', models.CharField(max_length=64)),
                ('resort_address_line2', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('resort_address_city', models.CharField(max_length=64)),
                ('resort_address_state', models.CharField(choices=[('AK', 'AK'), ('AS', 'AS'), ('AZ', 'AZ'), ('CO', 'CO'), ('CT', 'CT'), ('DC', 'DC'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('GU', 'GU'), ('HI', 'HI'), ('IA', 'IA'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('MA', 'MA'), ('MD', 'MD'), ('ME', 'ME'), ('MI', 'MI'), ('MN', 'MN'), ('MO', 'MO'), ('MP', 'MP'), ('MS', 'MS'), ('MT', 'MT'), ('NA', 'NA'), ('NC', 'NC'), ('ND', 'ND'), ('NE', 'NE'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NV', 'NV'), ('NY', 'NY'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('PR', 'PR'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VA', 'VA'), ('VI', 'VI'), ('VT', 'VT'), ('WA', 'WA'), ('WI', 'WI'), ('WV', 'WV'), ('WY', 'WY')], max_length=2)),
                ('resort_address_zip_code', models.IntegerField()),
                ('resort_website_url', models.CharField(blank=True, max_length=128)),
                ('resort_altitude', models.IntegerField(blank=True)),
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
                ('team_tags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('2BD', '2 black diamond'), ('1BD', '1 black diamond'), ('BS', 'blue square'), ('GS', 'green circle'), ('OP', 'off piste'), ('PH', 'party hardy'), ('FF', 'family friendly'), ('TP', 'terrain park')], max_length=25, null=True)),
                ('team_administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.PeakUser')),
                ('team_resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='board.Resort')),
            ],
        ),
        migrations.AddField(
            model_name='resort',
            name='resort_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='message_board_teams',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='board.Team'),
        ),
        migrations.AddField(
            model_name='message',
            name='message_board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.MessageBoard'),
        ),
        migrations.AddField(
            model_name='message',
            name='message_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.PeakUser'),
        ),
    ]
