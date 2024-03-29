# Generated by Django 4.2.7 on 2024-01-24 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enxibitation_Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exhibition', models.TextField(verbose_name='Календарь выставок')),
                ('period', models.CharField(max_length=100, verbose_name='Период')),
                ('data_of_participation', models.CharField(max_length=100, verbose_name='Дата участия')),
                ('location', models.CharField(max_length=100, verbose_name='Место проведения выставки')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Календарь выставки',
                'verbose_name_plural': 'Календарь выставок',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='События')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('image', models.CharField(max_length=150, verbose_name='Картинка')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Событиe',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Публикации')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('image', models.CharField(max_length=200, verbose_name='Картинка')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='New_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Имя продукта')),
                ('slug', models.SlugField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Новинка')),
            ],
            options={
                'verbose_name': 'Новинка',
                'verbose_name_plural': 'Новинки',
            },
        ),
    ]
