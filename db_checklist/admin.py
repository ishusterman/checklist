from django.contrib import admin
from .models import  *
from django.utils.html import format_html
from django.contrib.auth.models import User
#from easy_select2 import select2_modelform
#from advanced_filters.admin import AdminAdvancedFiltersMixin

# Register your models here.

class equip_Inline(admin.TabularInline):
    model = equip_detail
    extra = 1

class implant_Inline(admin.TabularInline):
    model = implant_detail
    extra = 1


class resorption_mat_Inline(admin.TabularInline):
    model = resorption_mat_count
    extra = 1

class no_resorption_mat_Inline(admin.TabularInline):
    model = no_resorption_mat_count
    extra = 1

class Oper_Admin (admin.ModelAdmin):
    list_display = ['oper']
    search_fields = ['oper']
    list_per_page = 40


class Checklist_Admin(admin.ModelAdmin):

    #admin.AdminSite.site_header = 'Заголовок админки'

    inlines = (resorption_mat_Inline, no_resorption_mat_Inline, implant_Inline, equip_Inline)

    # вывод информации о тревоге
    def get_warning(self):
        res =  self.incident or self.inc_doctor or self.inc_anesthes or self.inc_nurse or \
               self.inc_nurse_a or self.inc_nurse2 or self.inc_cut or self.inc_blood_skin or \
               self.inc_blood_lips or self.inc_blood_robe or self.inc_drugs or self.inc_action or self.inc_message or self.inc_act or self.inc_log or \
               self.rw or self.aids or self.vgv or self.vgs or self.anaerobic_b or self.tbs
        if res:
            return format_html(' <span style="color: red"><b>Тревога</b></span>')

    get_warning.short_description = "Авария"
    get_warning.allow_tags = True

    # вывод информации для печати
    def get_print(self):
        #res= format_html(' <span><a href=/print/' + str(self.id)+'> <img src="http://192.168.1.16:8008/img/print.png" width="20" height="20" title="Печать"></img></a></span>')
        res = format_html(' <span><a href=/print/' + str(self.id) + '> <img src="/static/print.png" width="20" height="20" title="Печать"></img></a></span>')
        return res

    get_print.short_description = 'Картинка'
    get_print.allow_tags = True
    #< link  rel = "stylesheet"   href ="{% static " css / styles.css" %}" / >

    get_print.short_description = "Печать"
    get_print.allow_tags = True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(Checklist_Admin, self).get_queryset(request)
        else:
            return super(Checklist_Admin, self).get_queryset(request).filter(Add = request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'Add', None) is None:
            obj.Add = request.user
        obj.save()

    message_warn = format_html(' <span style="color: red"><b>Авария</b></span>')
    fieldsets = [
            ('', {'fields': [('num_room','number'),
                             'date', 'time', ('oper_start', 'oper_finish'),('doctor_come_time','anesthes_come_time'),'queue', 'duration', ('plan', 'vmp_rf', 'vmp_rb')
                             ]}),
            ('Операционная бригада', {'fields': [('doctor','doctor2','assistent','anesthes','nurse','nurse_a', 'nurse2')]}),
            ('', {'fields': ['patient',('num_ib', 'dept'), ('gender','age', 'allergy'),
                            ('rw', 'aids', 'vgv', 'vgs', 'tbs', 'anaerobic_b', 'anaerobic_n'), 'oper',('position','repeat_oper')
                                                            ]}),
            ('О предыдущей операции',{ 'classes': ('collapse',),'fields': ['p_date', 'p_organization', 'p_oper', 'after_oper_bag']}),
            ('', {'classes': ('wide',),
                'fields': [ 'technik', 'inf', 'antiseptic', ('restrict_f', 'antiseptic_f'),'b_o_count',
                            #(  'implant',
                              #('implant1','implant2','implant3'),
                             #   'equip'),

                              #('equip1','equip2', 'equip3','equip4'),
                             'a_c_count',
                            #('resorption_mat1', 'resorption_mat1_count'),('resorption_mat2','resorption_mat2_count'),('resorption_mat3','resorption_mat3_count'),
                            #('no_resorption_mat1','no_resorption_mat1_count'),('no_resorption_mat2','no_resorption_mat2_count'),('no_resorption_mat3','no_resorption_mat3_count')
                         ]}),
            ('Расходный материал', {'classes': ('collapse',),
                                    'fields': [('blade11', 'blade15', 'blade23'),( 'drains', 'bandage', 'gem_mat'), ('clips', 'filter','cassete'),
                                               ('catheter','band'),('napkin_big','napkin_avg','napkin_sml'),
                                               ('gloves_st', 'gloves_no_st'),
                                               ('chain_gloves', 'disposable_underwear')
                         ]}),

            ('Авария', {'classes': ('collapse',),
                                       'fields': ['incident', 'inc_doctor', 'inc_anesthes','inc_nurse','inc_nurse_a','inc_nurse2',
                                                  'inc_cut', 'inc_blood_skin', 'inc_blood_lips', 'inc_blood_robe',
                                                  'inc_drugs', 'inc_action', 'inc_message', 'inc_act','inc_log'

                         ]}),

            ]
    readonly_fields = ('get_print',)
    list_display = ('num_room','number','date', 'patient', 'doctor', 'dept', 'oper', get_warning, get_print)
    search_fields = ['patient', 'doctor', 'oper__oper', 'dept__dept']
    #list_filter = ['oper']
    #advanced_filter_fields = ['patient']
    list_per_page = 20
    view_on_site = True
    date_hierarchy = 'date'
    list_display_links= ('num_room','number','date', 'patient', 'doctor', 'dept', 'oper')




admin.site.register(CheckList, Checklist_Admin)
admin.site.register(s_oper, Oper_Admin)
admin.site.register(s_antiseptic)
admin.site.register(s_antiseptic_f)
admin.site.register(s_dept)
admin.site.register(s_equip)
admin.site.register(s_implant)
admin.site.register(s_inf)
admin.site.register(s_no_resorption_mat)
admin.site.register(s_position)
admin.site.register(s_resorption_mat)
admin.site.register(s_technik)
admin.site.index_title = ''


#admin.site.register(s_position)
