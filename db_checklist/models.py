from django.db import models
from datetime import date
from django.contrib.auth.models import User
import select2.fields
import select2.models

class s_oper(models.Model):
    id = models.AutoField(primary_key=True)
    oper = models.CharField(verbose_name="Операция", max_length=150, blank=True)

    def __str__(self):
        return self.oper

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

class s_antiseptic(models.Model):
    id = models.AutoField(primary_key=True)
    antiseptic = models.CharField(verbose_name="Обработка рук персонала проведена антисептиком", max_length=50,
                                  blank=True)

    def __str__(self):
        return self.antiseptic

    class Meta:
        verbose_name = 'Антисептик для обработки рук'
        verbose_name_plural = 'Антисептики для обработки рук'


class s_antiseptic_f(models.Model):
    id = models.AutoField(primary_key=True)
    antiseptic_f = models.CharField(verbose_name="Обработка операционного поля", max_length=50, blank=True)

    def __str__(self):
        return self.antiseptic_f

    class Meta:
        verbose_name = 'Антисептик для операционного поля'
        verbose_name_plural = 'Антисептики для операционного поля'


class s_dept(models.Model):
    id = models.AutoField(primary_key=True)
    dept = models.CharField(verbose_name="Отделение", max_length=50, blank=True)

    def __str__(self):
        return self.dept

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'


class s_equip(models.Model):
    id = models.AutoField(primary_key=True)
    equip = models.CharField(verbose_name="Оборудование", max_length=50, blank=True)

    def __str__(self):
        return self.equip

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class s_implant(models.Model):
    id = models.AutoField(primary_key=True)
    implant = models.CharField(verbose_name="Имплант", max_length=100, blank=True)

    def __str__(self):
        return self.implant

    class Meta:
        verbose_name = 'Имплант'
        verbose_name_plural = 'Импланты'


class s_inf(models.Model):
    id = models.AutoField(primary_key=True)
    inf = models.CharField(verbose_name="Степень инфицированности", max_length=50, blank=True)

    def __str__(self):
        return self.inf

    class Meta:
        verbose_name = 'Степень инфицированности'
        verbose_name_plural = 'Степени инфицированности'


class s_no_resorption_mat(models.Model):
    id = models.AutoField(primary_key=True)
    no_resorption_mat = models.CharField(verbose_name="Нерассасывающийся материал", max_length=50, blank=True)

    def __str__(self):
        return self.no_resorption_mat

    class Meta:
        verbose_name = 'Шовный материал не рассасывающийся'
        verbose_name_plural = 'Шовный материал не рассасывающийся'


class s_position(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.CharField(verbose_name="Положение пациента", max_length=50, blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Положение пациента'
        verbose_name_plural = 'Положения пациента'


class s_resorption_mat(models.Model):
    id = models.AutoField(primary_key=True)
    resorption_mat = models.CharField(verbose_name="Рассасывающийся материал", max_length=50, blank=True)

    def __str__(self):
        return self.resorption_mat

    class Meta:
        verbose_name = 'Шовный материал рассасывающийся'
        verbose_name_plural = 'Шовный материал рассасывающийся'

class s_technik(models.Model):
    id = models.AutoField(primary_key=True)
    technik = models.CharField(verbose_name="По технике выполнения", max_length=50, blank=True)

    def __str__(self):
        return self.technik

    class Meta:
        verbose_name = 'Техника выполнения'
        verbose_name_plural = 'Техника выполнения'

class CheckList(models.Model):

    GENDER_CHOICES = (
        ('муж', 'муж'),
        ('жен', 'жен'),
    )
    id = models.AutoField(primary_key=True)
    num_room = models.PositiveIntegerField(verbose_name="Номер операционной", blank=False)
    number = models.PositiveIntegerField(verbose_name="Номер по порядку", blank=False)
    date = models.DateField(verbose_name="Дата операции", default=date.today)
    time = models.TimeField(verbose_name="Время подачи пациента в операционную", default="10:00")

    oper_start = models.TimeField(verbose_name="Время начала операции", default="10:00")
    doctor_come_time = models.TimeField(verbose_name="Время прихода врачей", default="10:00")
    anesthes_come_time = models.TimeField(verbose_name="Время прихода анестезиолога", default="10:00")
    oper_finish = models.TimeField(verbose_name="Время завершения операции", default="10:00")

    queue = models.PositiveIntegerField(verbose_name="Очередь", default=0)
    duration = models.DurationField(verbose_name="Продолжительность", default=0)
    plan = models.BooleanField(verbose_name="Плановая", default=True)
    vmp_rf = models.BooleanField(verbose_name="ВМП РФ", default=False)
    vmp_rb = models.BooleanField(verbose_name="ВМП РБ", default=False)
    doctor = models.CharField(verbose_name="Хирург", max_length=50, blank=False)
    doctor2 = models.CharField(verbose_name="Второй хирург", max_length=50, blank=True, default= "")
    assistent = models.CharField(verbose_name="Ассистент", max_length=50, blank=True)
    anesthes = models.CharField(verbose_name="Анестезиолог", max_length=50, blank=True)
    nurse = models.CharField(verbose_name="Медсестра", max_length=50, blank=True)
    nurse_a = models.CharField(verbose_name="Медсестра анестезист", max_length=50, blank=True)
    nurse2 = models.CharField(verbose_name="Санитарка", max_length=50, blank=True)
    patient = models.CharField(verbose_name="ФИО пациента", max_length=50, blank=False)
    num_ib = models.PositiveIntegerField(verbose_name="№ истории болезни", default=0, blank=True)
    dept = models.ForeignKey(s_dept, verbose_name="Отделение", default=None, blank=True, null=True)
    gender = models.CharField(verbose_name="Пол",max_length=3, choices=GENDER_CHOICES, default='муж')
    age = models.IntegerField(verbose_name="Возраст", default=0, blank=True)
    allergy = models.BooleanField(verbose_name="Аллергия", default=False)
    rw = models.BooleanField(verbose_name="RW", default=False)
    aids = models.BooleanField(verbose_name="AIDS", default=False)
    vgv = models.BooleanField(verbose_name="VGV", default=False)
    vgs = models.BooleanField(verbose_name="VGS", default=False)
    tbs = models.BooleanField(verbose_name="TBS", default=False)
    anaerobic_b = models.BooleanField(verbose_name="Анаэробная инфекция", default=False)
    anaerobic_n = models.CharField(verbose_name="Анаэробная инфекция", max_length=50, blank=True)

    #oper = models.ForeignKey(s_oper, verbose_name="Операция", null=True, blank=False)

    oper = select2.fields.ForeignKey(s_oper, verbose_name="Операция", null=True, blank=True, default=None)

    position = models.ForeignKey(s_position, verbose_name="Положение пациента", default=None, blank=True, null=True)

    repeat_oper = models.BooleanField(verbose_name="Повторная опреация", default=False)
    p_date = models.DateField(verbose_name="Дата предыдущей операции", null=True, blank=True)
    p_organization = models.CharField(verbose_name="Название организации (предыдущ. операции)", max_length=50,
                                      blank=True)
    p_oper = models.CharField(verbose_name="Название предыдущей операции", max_length=50, blank=True)
    after_oper_bag = models.CharField(verbose_name="Послеоперационные осложнения предыдущей операции", max_length=50,
                                      blank=True)

    technik = models.ForeignKey(s_technik, verbose_name="Техника выполнения", default=None, blank=True, null=True)
    inf = models.ForeignKey(s_inf, verbose_name="Степень инфицированности", default=None, blank=True, null=True)
    antiseptic = models.ForeignKey(s_antiseptic, verbose_name="Обработка рук персонала проведена антисептиком", default=None,blank = True, null=True)
    antiseptic_f = models.ForeignKey(s_antiseptic_f, verbose_name="Обработка операционного поля", default=None, blank=True, null=True)
    restrict_f = models.BooleanField(verbose_name="Опер. поле огранич. однораз. стерил. бельем", default=False)
    b_o_count = models.BooleanField(verbose_name="До начала операции произведен подсчет кол-ва инструментов, салфеток и игл", default=False)

    #implant = models.ManyToManyField(s_implant, verbose_name="Импланты и протезы", blank=True)
    #equip = models.ManyToManyField(s_equip, verbose_name="Используемое оборудование", blank=True)

    implant = models.ManyToManyField(s_implant, through = 'implant_detail')
    equip = models.ManyToManyField(s_equip, through = 'equip_detail')

    a_c_count = models.BooleanField(verbose_name="Перед закрытием операционной раны произведен подсчет кол-ва инструментов, салфеток и игл", default=False)


    #, through = 'resorption_mat_count'
    resorption_mat = models.ManyToManyField(s_resorption_mat, through = 'resorption_mat_count')
    no_resorption_mat = models.ManyToManyField(s_no_resorption_mat, through='no_resorption_mat_count')



    blade11 = models.PositiveIntegerField(verbose_name="Лезвия №11", default=0, blank=True)
    blade15 = models.PositiveIntegerField(verbose_name="Лезвия №15", default=0, blank=True)
    blade23 = models.PositiveIntegerField(verbose_name="Лезвия №23", default=0, blank=True)
    drains = models.PositiveIntegerField(verbose_name="Дренажи", default=0, blank=True)
    bandage = models.PositiveIntegerField(verbose_name="Повязки", default=0, blank=True)
    gem_mat = models.PositiveIntegerField(verbose_name="Гем. мат.", default=0, blank=True)
    clips = models.PositiveIntegerField(verbose_name="Клипсы", default=0, blank=True)
    filter = models.PositiveIntegerField(verbose_name="Фильтры", default=0, blank=True)
    cassete = models.PositiveIntegerField(verbose_name="Кассеты", default=0, blank=True)
    catheter = models.PositiveIntegerField(verbose_name="Катеторы", default=0, blank=True)
    band = models.PositiveIntegerField(verbose_name="Бинты", default=0, blank=True)
    napkin_big = models.PositiveIntegerField(verbose_name="Салфетки большие", default=0, blank=True)
    napkin_avg = models.PositiveIntegerField(verbose_name="Салфетки средние", default=0, blank=True)
    napkin_sml = models.PositiveIntegerField(verbose_name="Салфетки маленькие", default=0, blank=True)
    gloves_st = models.PositiveIntegerField(verbose_name="Перчатки стерильные", default=0, blank=True)
    gloves_no_st = models.PositiveIntegerField(verbose_name="Перчатки нестерильные", default=0, blank=True)
    chain_gloves = models.PositiveIntegerField(verbose_name="Кольчужные перчатки", default=0, blank=True)
    disposable_underwear = models.PositiveIntegerField(verbose_name="Одноразовое белье", default=0, blank=True)

    incident = models.BooleanField(verbose_name="Авария", default=False)
    inc_doctor = models.BooleanField(verbose_name="Инцидент с хирургом", default=False)
    inc_anesthes = models.BooleanField(verbose_name="Инцидент с анестезиологом", default=False)
    inc_nurse_a = models.BooleanField(verbose_name="Инцидент с медсестрой-анестезист", default=False)
    inc_nurse = models.BooleanField(verbose_name="Инцидент с оперционной медсестрой", default=False)
    inc_nurse2 = models.BooleanField(verbose_name="Инцидент с санитаркой", default=False)

    inc_cut = models.BooleanField(verbose_name="Порез, укол", default=False)
    inc_blood_skin = models.BooleanField(verbose_name="Попадание крови или др. биологических метериалов на кожные покровы", default=False)
    inc_blood_lips = models.BooleanField(verbose_name="Попадание крови или др. биологических метериалов на слизистую глаз, носа,рта", default=False)
    inc_blood_robe = models.BooleanField(verbose_name="Попадание крови или др. биологических метериалов на кожные покровы",default = False)
    inc_drugs = models.BooleanField(verbose_name="Начат прием антиретровирусных препаратов в целях постконтактной профилактики заражения ВИЧ", default=False)
    inc_action = models.BooleanField(verbose_name="Проведены мероприятия при аварийной ситуации согласно приказа №174 от 30.01 .2012 \"Об экстренной профилактике заражения ВИЧ-инфекцией\"", default = False)
    inc_message = models.BooleanField(verbose_name="Сообщено руководителю подразделения, его заместителю или вышестоящему руководителю", default=False)
    inc_act = models.BooleanField(verbose_name="Составлен \"Акт о несчастном случае на производстве\"", default=False)
    inc_log = models.BooleanField(verbose_name="Заполнен \"Журнал регистрации несчастных случаев на производстве\"",default=False)

    # кто автор
    Add = models.ForeignKey(User, null=True, blank=True, default=None)

    tmp = models.PositiveIntegerField(verbose_name="временное поле для загрузки", default=0, blank=True)

    def __str__(self):
        return str(self.num_room) + " " +str(self.number) + " " + str(self.patient) + " " +str(self.doctor) + " " +str(self.oper)

    class Meta:
        verbose_name = 'Чеклист'
        verbose_name_plural = 'Чеклисты'

    def __unicode__(self):
        return self.id


class implant_detail(models.Model):
    CheckList_id = models.ForeignKey(CheckList)
    implant_id = models.ForeignKey(s_implant, verbose_name= "Импланты и протезы")

    def __str__(self):
        return " "

    class Meta:
        verbose_name = 'Имплант и протезы'
        verbose_name_plural = 'Имланты и протезы'


class equip_detail(models.Model):
    CheckList_id = models.ForeignKey(CheckList)
    equip_id = models.ForeignKey(s_equip, verbose_name="Используемое оборудование")

    def __str__(self):
        return " "

    class Meta:
        verbose_name = 'Используемое оборудование'
        verbose_name_plural = 'Используемое оборудование'

class no_resorption_mat_count(models.Model):
    CheckList_id = models.ForeignKey(CheckList)
    no_resorption_mat_id = models.ForeignKey(s_no_resorption_mat, verbose_name= "Нерассасывающийся шовный материал")
    count = models.PositiveIntegerField(verbose_name="Кол-во", default=0, blank=True)

    def __str__(self):
        return " "

    class Meta:
        verbose_name = 'Кол-во нерассасывающего шовного материала'
        verbose_name_plural = 'Кол-во нерассасывающего шовного материала'

class resorption_mat_count(models.Model):
    CheckList_id = models.ForeignKey(CheckList)
    resorption_mat_id = models.ForeignKey(s_resorption_mat, verbose_name= "Рассасывающийся шовный материал")
    count = models.PositiveIntegerField(verbose_name="Кол-во", default=0, blank=True)

    def __str__(self):
        return " "

    class Meta:
        verbose_name = 'Кол-во рассасывающего шовного материала'
        verbose_name_plural = 'Кол-во рассасывающего шовного материала'

# Create your models here.
