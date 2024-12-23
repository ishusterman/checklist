from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.conf import settings

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from db_checklist.models import *
from db_checklist.models import implant_detail
#import xlwt, xlrd
#from xlutils.copy import copy as xlcopy
from django.http import FileResponse
import openpyxl
from datetime import timedelta
from .form import *
from openpyxl.writer.excel import save_virtual_workbook

from django.contrib.auth.models import User
import numpy as np
from datetime import datetime

@login_required(login_url='/login/')
def index(request, id):
    wb = openpyxl.load_workbook(filename='list.xlsx')
    sheet = wb['Лист1']
    ChL = CheckList.objects.get(id=id)

    # вывод в шаблон логической переменной в виде + -
    log_var = (lambda x: "-" if not (x) else "+")

    sheet['AS1']= ChL.num_room
    sheet['AZ1']= ChL.number
    sheet['L6']= ChL.date
    sheet['O8']= ChL.time
    sheet['G9']= ChL.queue
    sheet['O10']= ChL.duration
    sheet['A11']= log_var (ChL.plan)
    sheet['K11']= log_var (ChL.vmp_rf)
    sheet['K12']= log_var (ChL.vmp_rb)
    sheet['AE6']= ChL.doctor
    sheet['AF7']= ChL.doctor2
    sheet['AF8']= ChL.assistent
    sheet['AH9']= ChL.anesthes
    sheet['AO10']= ChL.nurse
    sheet['AN11']= ChL.nurse_a
    sheet['AG12']= ChL.nurse2



    sheet['J14']= ChL.patient
    sheet['M16']= ChL.num_ib
    sheet['AF16'] = '-' if (ChL.dept_id is None) else s_dept.objects.get(id = int(ChL.dept_id)).dept
    sheet['I18']= ChL.gender
    sheet['X18']= ChL.age
    sheet['AN18']= log_var (ChL.allergy)
    #ChL.allergy
    sheet['F20']= log_var (ChL.rw)
    sheet['K20']= log_var (ChL.aids)
    sheet['P20']= log_var (ChL.vgv)
    sheet['U20']= log_var (ChL.vgs)
    sheet['Z20']= log_var (ChL.tbs)
    sheet['AO20']= log_var (ChL.anaerobic_b)
    sheet['AR20']= ChL.anaerobic_n


    sheet['I22']= '-' if (ChL.oper_id is None) else s_oper.objects.get(id = int(ChL.oper_id)).oper
    sheet['M26']= '-' if (ChL.position_id is None) else s_position.objects.get(id = int(ChL.position_id)).position


    sheet['AE26']= log_var (ChL.repeat_oper)
    sheet['AN28']= ChL.p_date
    sheet['T30']= ChL.p_organization
    sheet['T32']= ChL.p_oper
    sheet['T34']= ChL.after_oper_bag

    sheet['S36']= '-' if (ChL.technik_id is None) else s_technik.objects.get(id = int(ChL.technik_id)).technik


    sheet['S38']= '-' if (ChL.inf_id is None) else s_inf.objects.get(id = int(ChL.inf_id)).inf
    sheet['AD40']= '-' if (ChL.antiseptic_id is None) else s_antiseptic.objects.get(id = int(ChL.antiseptic_id)).antiseptic
    sheet['AL42']= '-' if (ChL.antiseptic_f_id is None) else s_antiseptic_f.objects.get(id = int(ChL.antiseptic_f_id)).antiseptic_f

    sheet['AC42']= log_var(ChL.restrict_f)
    sheet['AX44']= log_var (ChL.b_o_count)

    # выбирем все импланты этого чеклиста
    res = implant_detail.objects.filter(CheckList_id=int(ChL.id))
    # определеяем кол-во элементов
    l = len(res)
    if l >= 1:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['V46']= s_implant.objects.get(id=int(res[0].implant_id_id)).implant
    if l >= 2:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['V48']= s_implant.objects.get(id=int(res[1].implant_id_id)).implant

    if l >= 3:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['V50']= s_implant.objects.get(id=int(res[2].implant_id_id)).implant

    # выбирем все оборудование этого чеклиста
    res = equip_detail.objects.filter(CheckList_id=int(ChL.id))
    # определеяем кол-во элементов
    l = len(res)
    if l >= 1:
    # берем код ,по коду определяем имя, записываем в ячейку
        sheet['J52'] = s_equip.objects.get(id=int(res[0].equip_id_id)).equip
    if l >= 2:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AB52'] = s_equip.objects.get(id=int(res[1].equip_id_id)).equip
    if l >= 3:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['J54'] = s_equip.objects.get(id=int(res[2].equip_id_id)).equip

    if l >= 4:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AB54'] = s_equip.objects.get(id=int(res[3].equip_id_id)).equip


    sheet['AG57']= log_var (ChL.a_c_count)

    # выбирем все рассасыв материалы этого чеклиста
    res = resorption_mat_count.objects.filter(CheckList_id=int(ChL.id))
    # определеяем кол-во элементов
    l = len(res)
    if l >= 1:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AA59'] = s_resorption_mat.objects.get(id=int(res[0].resorption_mat_id_id)).resorption_mat
    if l >= 2:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AK59'] = s_resorption_mat.objects.get(id=int(res[1].resorption_mat_id_id)).resorption_mat
    if l >= 3:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AU59'] = s_resorption_mat.objects.get(id=int(res[2].resorption_mat_id_id)).resorption_mat

    # выбирем все рассасыв материалы этого чеклиста
    res = no_resorption_mat_count.objects.filter(CheckList_id=int(ChL.id))
    # определеяем кол-во элементов
    l = len(res)
    if l >= 1:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AA61'] = s_no_resorption_mat.objects.get(id=int(res[0].no_resorption_mat_id_id)).no_resorption_mat
    if l >= 2:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AK61'] = s_no_resorption_mat.objects.get(id=int(res[1].no_resorption_mat_id_id)).no_resorption_mat
    if l >= 3:
        # берем код ,по коду определяем имя, записываем в ячейку
        sheet['AU61'] = s_no_resorption_mat.objects.get(id=int(res[2].no_resorption_mat_id_id)).no_resorption_mat


    sheet['I65']= ChL.blade11
    sheet['I67']= ChL.drains
    sheet['I69']= ChL.bandage
    sheet['I71']= ChL.gem_mat

    sheet['W63']= ChL.clips
    sheet['W65']= ChL.filter
    sheet['W67']= ChL.cassete
    sheet['W69']= ChL.catheter
    sheet['W71']= ChL.band
    sheet['BA63']= ChL.napkin_big
    sheet['BA65']= ChL.napkin_avg
    sheet['BA67']= ChL.napkin_sml
    sheet['BA69']= ChL.gloves_st
    sheet['BA71']= ChL.gloves_no_st


    sheet['P85']= log_var (ChL.incident)
    sheet['B87']= log_var (ChL.inc_doctor)
    sheet['B89']= log_var (ChL.inc_anesthes)
    sheet['B91']= log_var (ChL.inc_nurse)
    sheet['B93']= log_var (ChL.inc_nurse_a)
    sheet['B95']= log_var (ChL.inc_nurse2)

    sheet['B97']= log_var (ChL.inc_cut)
    sheet['B102']= log_var (ChL.inc_blood_skin)
    sheet['B106']= log_var (ChL.inc_blood_lips)
    sheet['B111']= log_var (ChL.inc_blood_robe)
    sheet['B115']= log_var (ChL.inc_drugs)
    sheet['B118']= log_var (ChL.inc_action)
    sheet['B121']= log_var (ChL.inc_message)
    sheet['B124']= log_var (ChL.inc_act)
    sheet['B127']= log_var (ChL.inc_log)


    file_name = "checklist"+str(ChL.num_ib)+".xlsx"

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+file_name
    wb.save(response)
    return response

def switch_case(case):
    return {
    'января' : "1",'Январь': "1",'январь': "1",
    'февраля' : "2", 'Февраль': "2", 'февраль': "2",
    'марта' : "3", 'Март': "3",'март': "3",
    'апреля': "4",'Апрель': "4", 'апрель': "4",
    'мая': "5",  'Май': "5", 'май': "5",
    'июня': "6",'Июнь': "6",'июнь': "6",
    'июля': "7", 'Июль': "7",'июль': "7",
    'августа': "8",'Август': "8", 'август': "8",
    'сентября':"9", 'Сентябрь': "9", 'сентябрь': "9",
    'октября': "10", 'Октябрь': "10", 'октябрь': "10",
    'ноября': "11",'Ноябрь': "11", 'ноябрь': "11",
    'декабря': "12",  'Декабрь': "12", 'декабрь': "12"
    }.get(case, "error")

def date_convert_to_usa(date):
    date = date.split()
    res=date[2]+"-"+switch_case(date[1])+"-"+date[0]
    return res

@login_required(login_url='/login/')
def save_checklist (request):
    id = request.POST['id']
    patient = request.POST['patient']
    num_room = request.POST['num_room']
    number = request.POST['number']
    doctor = request.POST['doctor']
    date1 = request.POST['date']
    date2 = date_convert_to_usa(date1)

    if id == "":
        rec = CheckList(patient=patient, doctor=doctor, num_room=int(num_room), number=int(number),
                        duration=timedelta(minutes=20), date=date2)
    if id != "":
        rec = CheckList(id=id, patient=patient, doctor=doctor, num_room=int(num_room), number=int(number),
                        duration=timedelta(minutes=20), date=date2)
    rec.save()
    id = str(rec.id)

    # добавление и удаление имплантов
    e = CheckList.objects.get(id=id)
    del_implant = request.POST.getlist('del_implant[]')

    for i in del_implant:
        instance = implant_detail.objects.filter(CheckList_id=id, implant_id=i)
        instance.delete()

    num_implant = request.POST['add_implant']
    if num_implant != "0":
        add_implant = s_implant.objects.get(id=num_implant)
        b = implant_detail(CheckList_id=e, implant_id=add_implant)
        b.save()
    return id



@login_required(login_url='/login/')
def save(request):

    action = request.POST['action']
    if action == "К списку чеклистов":
        return redirect('/cool_view/')
    if action == "Сохранить":
        id = save_checklist(request)
        return redirect('/cool_view/edit/' + id)

@login_required(login_url='/login/')
def save_model(request):

    id = request.POST['id']
    if id != "0":
        a = CheckList.objects.get(id=id)
    else:
        a = CheckList()
    fs1_1 = fs1(request.POST, request.FILES, instance=a)
    fs2_1 = fs2(request.POST, request.FILES, instance=a)
    fs3_1 = fs3(request.POST, request.FILES, instance=a)
    fs4_1 = fs4(request.POST, request.FILES, instance=a)

    action = request.POST['action']

    if action == "К списку чеклистов":
        return redirect('/cool_view/')
    if action == "Сохранить":

        f = ChecklistForm(request.POST, instance=a)
        if f.is_valid() and fs1_1.is_valid() and fs2_1.is_valid() and fs3_1.is_valid() and fs4_1.is_valid():
            res = f.save()
            id = str(res.id)

            fs1_1.save()
            fs2_1.save()
            fs3_1.save()
            fs4_1.save()
            #print("inc_cut - " + request.POST['inc_cut'])
            print("save ok")
        else:
            print("save error")
            print (f.errors)

    return redirect('/cool_view/test_model/' + id)

@login_required(login_url='/login/')
def edit(request, id):
    if id !="0":
        Data = CheckList.objects.get(id=id)
        Oper_id = Data.oper_id

    if id == "0":
        Data = {}
        Oper_id = 0

    Oper_list = s_oper.objects.order_by('oper')
    Implant_list = s_implant.objects.order_by('implant') # справочник имплантов
    Implant_display = implant_detail.objects.filter(CheckList_id = id)# импланты данного чеклиста для отображения

    context = {'CheckList': Data, 'Oper': Oper_list, 'Implant_display': Implant_display, 'Implant': Implant_list, 'Oper_id': Oper_id, 'Username': request.user}

    if id == "0":
        return render(request, 'cool_view_edit.html', context)

    # если автор или админ
    if ((request.user == Data.Add) or request.user.groups.filter(name='admin').exists()):
        return render(request, 'cool_view_edit.html', context)
    else:
        return redirect('/auth/user/?next=/cool_view/')


def logoff(request):
    logout(request)
    return redirect('/auth/user/?next=/cool_view/')

def password_change(request):
    password_change(request)
    #return redirect('/auth/user/?next=/cool_view/')

@login_required(login_url='/login/')
def cool_view(request):
    #CheckList2 = CheckList.objects.order_by('id')

    if request.user.groups.filter(name='user').exists():
        CheckList2 = CheckList.objects.filter(Add=request.user)
    else:
        CheckList2 = CheckList.objects.all()

    context = {'CheckList': CheckList2, 'User': request.user}
    return render(request, 'cool_view.html', context)



def get_ChecklistForm(request,id):
    if id != "0":
        ChL = CheckList.objects.get(id=id)
        form = ChecklistForm(instance=ChL)
    else:
        ChL = CheckList()
        form = ChecklistForm()


    #ChL = CheckList.objects.get(id=id)
    eq_formset = fs2(instance=ChL)
    im_formset = fs1(instance=ChL)
    resorpt_formset = fs3(instance=ChL)
    no_resorpt_formset = fs4(instance=ChL)

    return render(request, 'model_edit.html',
                  {'form': form, 'id': id, 'eq_formset': eq_formset, 'im_formset': im_formset,'resorpt_formset': resorpt_formset,'no_resorpt_formset': no_resorpt_formset})

