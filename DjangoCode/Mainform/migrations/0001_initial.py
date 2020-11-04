# Generated by Django 3.0.4 on 2020-05-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('ntitle', models.CharField(max_length=100)),
                ('ncontent', models.TextField()),
                ('ndatetime', models.DateTimeField(auto_now=True)),
                ('ncolumn', models.CharField(max_length=4)),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('ngood', models.IntegerField()),
                ('nread', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uid2', models.CharField(max_length=13, unique=True)),
                ('uname', models.CharField(max_length=20)),
                ('uintro', models.TextField(max_length=400)),
                ('usign_datetime', models.DateTimeField(auto_now_add=True)),
                ('upsg_count', models.IntegerField()),
                ('ucolumn', models.CharField(max_length=2)),
                ('upwd', models.CharField(max_length=20)),
                ('uhead', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('rcontent', models.TextField()),
                ('rgood', models.IntegerField()),
                ('rdatetime', models.DateTimeField(auto_now=True)),
                ('rauthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mainform.users')),
                ('rreply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mainform.notes')),
            ],
        ),
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pfile', models.ImageField(upload_to='')),
                ('pdatetime', models.DateTimeField()),
                ('ppsg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mainform.notes')),
            ],
        ),
        migrations.AddField(
            model_name='notes',
            name='nauthor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Mainform.users'),
        ),
    ]