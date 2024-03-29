# Generated by Django 3.0.5 on 2020-04-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('birthday', models.DateField(auto_now=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('phone_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('FA', 'Film & Animation'), ('AV', 'Autos & Vehicles'), ('M', 'Music'), ('PA', 'Pets & Animals'), ('S', 'Sports'), ('TE', 'Travel & Events'), ('G', 'Gaming'), ('PB', 'People & Blogs'), ('C', 'Comedy'), ('En', 'Entertainment'), ('NP', 'News & Politics'), ('HS', 'Howto & Style'), ('Ed', 'Education'), ('ST', 'Science & Technology'), ('NA', 'Nonprofits & Activism')], default='FA', max_length=2)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('keywords', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Users')),
            ],
        ),
        migrations.CreateModel(
            name='UserViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Users')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Videos')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Users')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Videos')),
            ],
        ),
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Users')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Videos')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.TextField()),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Users')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_youtube.Videos')),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
    ]
