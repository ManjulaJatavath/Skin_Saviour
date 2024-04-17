from typing import Any
from django.http import HttpRequest
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin 
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin
from skin_treatment.models.treatment import *
from skin_treatment.models.face_wash import FaceWashModel
from skin_treatment.models.serum import SerumModel
from skin_treatment.models.moisturizer import MoisturizerModel
from skin_treatment.models.sunscreen import SunscreenModel
from skin_treatment.models.natural_products_facemask import NaturalProductsFacemaskModel
from skin_treatment.models.natural_products_facewash import NaturalProductsFacewashModel
from skin_treatment.models.natural_products_serum import NaturalProductsSerumModel
from skin_treatment.models.natural_products_moisturizer import NaturalProductsMoisturizerModel
from skin_treatment.models.natural_products_scrub import NaturalProductsScrubModel
from django.contrib import admin

# admin.py
@admin.register(NaturalProductsFacemaskModel)
class NaturalProductFacemaskAdmin(ImportExportModelAdmin):
    list_display = ['treatment', 'facemask1', 'facemask1_image', 'facemask2_image', 'is_active', 'created_at']
    list_filter = ['treatment', 'facemask1', 'facemask2']


@admin.register(NaturalProductsFacewashModel)
class NaturalProductFacewashAdmin(ImportExportModelAdmin):
    list_display = ['treatment', 'facewash1', 'facewash1_image', 'facewash2_image', 'is_active', 'created_at']
    list_filter = ['treatment', 'facewash1', 'facewash2']


@admin.register(NaturalProductsScrubModel)
class NaturalProductScrubAdmin(ImportExportModelAdmin):
    list_display = ['treatment', 'scrub1', 'scrub1_image', 'scrub2_image', 'is_active', 'created_at']
    list_filter = ['treatment', 'scrub1', 'scrub2']


@admin.register(NaturalProductsMoisturizerModel)
class NaturalProductMoisturizerAdmin(ImportExportModelAdmin):
    list_display = ['treatment', 'moisturizer1', 'moisturizer1_image', 'moisturizer2_image', 'is_active', 'created_at']
    list_filter = ['treatment', 'moisturizer1', 'moisturizer2']


@admin.register(NaturalProductsSerumModel)
class NaturalProductSerumAdmin(ImportExportModelAdmin):
    list_display = ['treatment', 'serum1', 'serum1_image', 'serum2_image', 'is_active', 'created_at']
    list_filter = ['treatment', 'serum1', 'serum2']


@admin.register(TreatmentModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'treatment', 'is_active', 'created_at']
    list_filter = ['treatment', 'is_active']


@admin.register(SkinTypeModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'skin_type', 'is_active', 'created_at']
    list_filter = ['skin_type', 'is_active']


@admin.register(AgeModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'age', 'is_active', 'created_at']
    list_filter = ['age', 'is_active']


@admin.register(SkinConernModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'skin_concern', 'is_active', 'created_at']
    list_filter = ['skin_concern', 'is_active']


@admin.register(ReactToNewProductsModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'react_to_new_products', 'is_active', 'created_at']
    list_filter = ['react_to_new_products', 'is_active']


@admin.register(SleepCycleModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'sleep_cycle', 'is_active', 'created_at']
    list_filter = ['sleep_cycle', 'is_active']


@admin.register(SkinCareTextureModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'skin_texture', 'is_active', 'created_at']
    list_filter = ['skin_texture', 'is_active']


@admin.register(FaceWashModel)
class FacewashAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    

@admin.register(SerumModel)
class SerumAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    

@admin.register(MoisturizerModel)
class MoisturizerAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    

@admin.register(SunscreenModel)
class SunscreenAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']


    