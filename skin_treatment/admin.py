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
    list_display = ['id', 'treatment']
@admin.register(SkinTypeModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'skin_type']
@admin.register(AgeModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'age']
@admin.register(SkinConernModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'skin_concern']
@admin.register(ReactToNewProductsModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'react_to_new_products']
@admin.register(SleepCycleModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'sleep_cycle']
@admin.register(SkinCareTextureModel)
class TreatmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'skin_texture']



# class FacewashResource(resources.ModelResource):
    # treatment = fields.Field(
    #     column_name='treatment',
    #     attribute='treatment',
    #     widget=ForeignKeyWidget(FaceWashModel, "treatment"),

    # )
    # age = fields.Field(
    #     column_name='age',
    #     attribute='age',
    #     widget=ForeignKeyWidget(FaceWashModel, "age"),

    # )
    # skin_type = fields.Field(
    #     column_name='skin_type',
    #     attribute='skin_type',
    #     widget=ForeignKeyWidget(FaceWashModel, "skin_type"),

    # )
    # skin_concern = fields.Field(
    #     column_name='skin_concern',
    #     attribute='skin_concern',
    #     widget=ForeignKeyWidget(FaceWashModel, "skin_concern"),

    # )
    # react_to_new_products = fields.Field(
    #     column_name='react_to_new_products',
    #     attribute='react_to_new_products',
    #     widget=ForeignKeyWidget(FaceWashModel, "react_to_new_products"),

    # )
    # # senstive = fields.Field(
    # #     column_name='senstive',
    # #     attribute='senstive',
    # #     widget=ForeignKeyWidget(FaceWashModel, "senstive"),

    # # )
    # sleep_cycle = fields.Field(
    #     column_name='sleep_cycle',
    #     attribute='sleep_cycle',
    #     widget=ForeignKeyWidget(FaceWashModel, "sleep_cycle"),

    # )
    # skincare_texture = fields.Field(
    #     column_name='skincare_texture',
    #     attribute='skincare_texture',
    #     widget=ForeignKeyWidget(FaceWashModel, "skincare_texture"),

    # )
    # class Meta:
    #     model = FaceWashModel
@admin.register(FaceWashModel)
class FacewashAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    # resource_class = FacewashResource

# class SerumResource(resources.ModelResource):
#     treatment = fields.Field(
#         column_name='treatment',
#         attribute='treatment',
#         widget=ForeignKeyWidget(FaceWashModel, "treatment"),

#     )
#     age = fields.Field(
#         column_name='age',
#         attribute='age',
#         widget=ForeignKeyWidget(FaceWashModel, "age"),

#     )
#     skin_type = fields.Field(
#         column_name='skin_type',
#         attribute='skin_type',
#         widget=ForeignKeyWidget(FaceWashModel, "skin_type"),

#     )
#     skin_concern = fields.Field(
#         column_name='skin_concern',
#         attribute='skin_concern',
#         widget=ForeignKeyWidget(FaceWashModel, "skin_concern"),

#     )
#     react_to_new_products = fields.Field(
#         column_name='react_to_new_products',
#         attribute='react_to_new_products',
#         widget=ForeignKeyWidget(FaceWashModel, "react_to_new_products"),

#     )
#     # senstive = fields.Field(
#     #     column_name='senstive',
#     #     attribute='senstive',
#     #     widget=ForeignKeyWidget(FaceWashModel, "senstive"),

#     # )
#     sleep_cycle = fields.Field(
#         column_name='sleep_cycle',
#         attribute='sleep_cycle',
#         widget=ForeignKeyWidget(FaceWashModel, "sleep_cycle"),

#     )
#     skincare_texture = fields.Field(
#         column_name='skincare_texture',
#         attribute='skincare_texture',
#         widget=ForeignKeyWidget(FaceWashModel, "skincare_texture"),

#     )
#     class Meta:
#         model = SerumModel
@admin.register(SerumModel)
class SerumAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    # resource_class = SerumResource

# class MoisturizerResource(resources.ModelResource):
#     treatment = fields.Field(
#         column_name='treatment',
#         attribute='treatment',
#         widget=ForeignKeyWidget(FaceWashModel, "treatment"),

#     )
#     age = fields.Field(
#         column_name='age',
#         attribute='age',
#         widget=ForeignKeyWidget(FaceWashModel, "age"),

#     )
#     skin_type = fields.Field(
#         column_name='skin_type',
#         attribute='skin_type',
#         widget=ForeignKeyWidget(FaceWashModel, "skin_type"),

#     )
#     skin_concern = fields.Field(
#         column_name='skin_concern',
#         attribute='skin_concern',
#         widget=ForeignKeyWidget(FaceWashModel, "skin_concern"),

#     )
#     react_to_new_products = fields.Field(
#         column_name='react_to_new_products',
#         attribute='react_to_new_products',
#         widget=ForeignKeyWidget(FaceWashModel, "react_to_new_products"),

#     )
#     # senstive = fields.Field(
#     #     column_name='senstive',
#     #     attribute='senstive',
#     #     widget=ForeignKeyWidget(FaceWashModel, "senstive"),

#     # )
#     sleep_cycle = fields.Field(
#         column_name='sleep_cycle',
#         attribute='sleep_cycle',
#         widget=ForeignKeyWidget(FaceWashModel, "sleep_cycle"),

#     )
#     skincare_texture = fields.Field(
#         column_name='skincare_texture',
#         attribute='skincare_texture',
#         widget=ForeignKeyWidget(FaceWashModel, "skincare_texture"),

#     )
#     class Meta:
#         model = MoisturizerModel
@admin.register(MoisturizerModel)
class MoisturizerAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    # resource_class = MoisturizerResource

# class SunscreenResource(resources.ModelResource):
#     treatment = fields.Field(
#         column_name='treatment',
#         attribute='treatment',
#         widget=ForeignKeyWidget(FaceWashModel, "treatment"),

#     )
#     age = fields.Field(
#         column_name='age',
#         attribute='age',
#         widget=ForeignKeyWidget(FaceWashModel, "age"),

#     )
#     skin_type = fields.Field(
#         column_name='skin_type',
#         attribute='skin_type',
#         widget=ForeignKeyWidget(FaceWashModel, "skin_type"),

#     )
#     skin_concern = fields.Field(
#         column_name='skin_concern',
#         attribute='skin_concern',
#         widget=ForeignKeyWidget(FaceWashModel, "skin_concern"),

#     )
#     react_to_new_products = fields.Field(
#         column_name='react_to_new_products',
#         attribute='react_to_new_products',
#         widget=ForeignKeyWidget(FaceWashModel, "react_to_new_products"),

#     )
#     # senstive = fields.Field(
#     #     column_name='senstive',
#     #     attribute='senstive',
#     #     widget=ForeignKeyWidget(FaceWashModel, "senstive"),

#     # )
#     sleep_cycle = fields.Field(
#         column_name='sleep_cycle',
#         attribute='sleep_cycle',
#         widget=ForeignKeyWidget(FaceWashModel, "sleep_cycle"),

#     )
#     skincare_texture = fields.Field(
#         column_name='skincare_texture',
#         attribute='skincare_texture',
#         widget=ForeignKeyWidget(FaceWashModel, "skincare_texture"),

#     )
#     class Meta:
#         model = SunscreenModel
@admin.register(SunscreenModel)
class SunscreenAdmin(ImportExportModelAdmin):
    list_display = ['id','treatment', 'age', 'skin_type', 'skin_concern', 'react_to_new_products', 'sleep_cycle', 'skincare_texture', 'image1', 'image2', 'essentials', ]
    list_filter = ['treatment', 'skin_type']
    # resource_class = SunscreenResource

    