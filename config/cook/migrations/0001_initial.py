# Generated by Django 3.2.7 on 2021-09-24 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('photo', models.ImageField(upload_to='recipe', verbose_name='사진 photo')),
                ('ingredients_list', models.CharField(max_length=200, verbose_name='재료 리스트 저장 ingredients_list')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(blank=True, max_length=200, null=True, verbose_name='재료 이름 ingredients')),
                ('ingredients_count', models.CharField(blank=True, max_length=200, null=True, verbose_name='재료개수 ingredients_count')),
                ('method', models.TextField(verbose_name='조리 방법 method')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cook.recipe', verbose_name='요리 제목 foreignkey title')),
            ],
        ),
    ]
