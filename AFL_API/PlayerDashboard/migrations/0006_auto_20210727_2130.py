# Generated by Django 3.2.5 on 2021-07-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayerDashboard', '0005_auto_20210724_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('seasonId', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='matches',
            field=models.ManyToManyField(to='PlayerDashboard.Match'),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='dateOfBirth',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='debutYear',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='draftPosition',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='draftType',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='draftYear',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='givenName',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='kickingFoot',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='photoURL',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='position',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='recruitedFrom',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='stateOfOrigin',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='playerbio',
            name='surname',
            field=models.CharField(default='', max_length=200),
        ),
    ]
