# Generated by Django 5.0.3 on 2024-04-12 12:13

import django.db.models.deletion
import utils.helpers.image_file_path
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReactToNewProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('react_to_new_products', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SensitiveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senstive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SkinCareTextureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_texture', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SkinConernModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_concern', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SkinTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SleepCycleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleep_cycle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SunscreenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('essentials', models.TextField()),
                ('image1', models.ImageField(upload_to=utils.helpers.image_file_path.sunscreen_image)),
                ('image2', models.ImageField(upload_to=utils.helpers.image_file_path.sunscreen_image)),
                ('description', models.TextField()),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.agemodel')),
                ('react_to_new_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.reacttonewproductsmodel')),
                ('senstive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sensitivemodel')),
                ('skin_concern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skinconernmodel')),
                ('skin_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skintypemodel')),
                ('skincare_texture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skincaretexturemodel')),
                ('sleep_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sleepcyclemodel')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.treatmentmodel')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SerumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('essentials', models.TextField()),
                ('image1', models.ImageField(upload_to=utils.helpers.image_file_path.serum_image)),
                ('image2', models.ImageField(upload_to=utils.helpers.image_file_path.serum_image)),
                ('description', models.TextField()),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.agemodel')),
                ('react_to_new_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.reacttonewproductsmodel')),
                ('senstive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sensitivemodel')),
                ('skincare_texture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skincaretexturemodel')),
                ('skin_concern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skinconernmodel')),
                ('skin_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skintypemodel')),
                ('sleep_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sleepcyclemodel')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.treatmentmodel')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MoisturizerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('essentials', models.TextField()),
                ('image1', models.ImageField(upload_to=utils.helpers.image_file_path.moisturizer_image)),
                ('image2', models.ImageField(upload_to=utils.helpers.image_file_path.moisturizer_image)),
                ('description', models.TextField()),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.agemodel')),
                ('react_to_new_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.reacttonewproductsmodel')),
                ('senstive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sensitivemodel')),
                ('skincare_texture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skincaretexturemodel')),
                ('skin_concern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skinconernmodel')),
                ('skin_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skintypemodel')),
                ('sleep_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sleepcyclemodel')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.treatmentmodel')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FaceWashModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('essentials', models.TextField()),
                ('image1', models.ImageField(upload_to=utils.helpers.image_file_path.facewash_image)),
                ('image2', models.ImageField(upload_to=utils.helpers.image_file_path.facewash_image)),
                ('description', models.TextField()),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.agemodel')),
                ('react_to_new_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.reacttonewproductsmodel')),
                ('senstive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sensitivemodel')),
                ('skincare_texture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skincaretexturemodel')),
                ('skin_concern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skinconernmodel')),
                ('skin_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.skintypemodel')),
                ('sleep_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.sleepcyclemodel')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_treatment.treatmentmodel')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
