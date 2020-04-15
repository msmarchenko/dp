# Generated by Django 2.2.8 on 2020-04-15 17:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('definitionid', models.IntegerField()),
                ('position', models.CharField(choices=[('Control', 'Control'), ('Quality', 'Quality')], default='Quality', max_length=10)),
            ],
            options={
                'unique_together': {('name', 'definitionid')},
            },
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rollenNumber', models.IntegerField()),
                ('value', models.FloatField()),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataanalysis.Composition')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataanalysis.Machine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataanalysis.Order')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataanalysis.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('kd_name', models.CharField(default='None', max_length=80)),
                ('rezeptur', models.CharField(max_length=80)),
                ('material', models.CharField(max_length=80)),
                ('polymer', models.CharField(max_length=20)),
                ('dicke', models.FloatField()),
                ('menge', models.FloatField()),
                ('yields', models.FloatField()),
                ('werk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataanalysis.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='measurements',
            index=models.Index(fields=['date'], name='dataanalysi_date_c5875d_idx'),
        ),
    ]
