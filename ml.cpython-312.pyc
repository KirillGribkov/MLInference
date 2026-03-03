from rest_framework.response import Response
from .serializers import *
from adrf.views import APIView
from adrf import viewsets
from asgiref.sync import sync_to_async
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import Data
from .models import DataModel, DataModelABTest
from .ml import model, model2

# Create your views here.
async def get_homepage(request:HttpRequest):
#def get_homepage(request:HttpRequest):
    if request.method == 'POST':
        #print(request.POST)
        form = Data(request.POST)
        if form.is_valid():
            data={
                'Год_рождения':form.cleaned_data['god_rojdeniya'],
                'Подписаны_документы':form.cleaned_data['podpisani_documenti'],
                'Пол':form.cleaned_data['pol'],
                'БылПростой':form.cleaned_data['bil_prostoy'],
                'ОпытВДолжности':form.cleaned_data['opit_v_doljnosti'],
                'Активность':form.cleaned_data['activnost'],
                'Знак_зодиака':form.cleaned_data['znak_zodiaka'],
                'Возраст':form.cleaned_data['vozrast'],
                'Оценка_HR':form.cleaned_data['ocenka_hr'],
                'УровеньОплаты':form.cleaned_data['uroven_oplati'],
                'Офлайн_участие':form.cleaned_data['oflain_meropriyatiya'],
                'Образование':form.cleaned_data['obrazovanie'],
                'Телефон':form.cleaned_data['telefon'],
                'Город':form.cleaned_data['gorod'],
                'Размер':form.cleaned_data['razmer'],
                'Закрытые_проекты':form.cleaned_data['zakritie_proekti'],
                'ГодНайма':form.cleaned_data['god_nayma'],
                'Курсы':form.cleaned_data['kursi'],
                }
            form_data={
                'god_rojdeniya':form.cleaned_data['god_rojdeniya'],
                'podpisani_documenti':form.cleaned_data['podpisani_documenti'],
                'pol':form.cleaned_data['pol'],
                'bil_prostoy':form.cleaned_data['bil_prostoy'],
                'opit_v_doljnosti':form.cleaned_data['opit_v_doljnosti'],
                'activnost':form.cleaned_data['activnost'],
                'znak_zodiaka':form.cleaned_data['znak_zodiaka'],
                'vozrast':form.cleaned_data['vozrast'],
                'ocenka_hr':form.cleaned_data['ocenka_hr'],
                'uroven_oplati':form.cleaned_data['uroven_oplati'],
                'oflain_meropriyatiya':form.cleaned_data['oflain_meropriyatiya'],
                'obrazovanie':form.cleaned_data['obrazovanie'],
                'telefon':form.cleaned_data['telefon'],
                'gorod':form.cleaned_data['gorod'],
                'razmer':form.cleaned_data['razmer'],
                'zakritie_proekti':form.cleaned_data['zakritie_proekti'],
                'god_nayma':form.cleaned_data['god_nayma'],
                'kursi':form.cleaned_data['kursi'],
                }
            otvet= await model(data)
            save_data={
                'god_rojdeniya':form.cleaned_data['god_rojdeniya'],
                'podpisani_documenti':form.cleaned_data['podpisani_documenti'],
                'pol':form.cleaned_data['pol'],
                'bil_prostoy':form.cleaned_data['bil_prostoy'],
                'opit_v_doljnosti':form.cleaned_data['opit_v_doljnosti'],
                'activnost':form.cleaned_data['activnost'],
                'znak_zodiaka':form.cleaned_data['znak_zodiaka'],
                'vozrast':form.cleaned_data['vozrast'],
                'ocenka_hr':form.cleaned_data['ocenka_hr'],
                'uroven_oplati':form.cleaned_data['uroven_oplati'],
                'oflain_meropriyatiya':form.cleaned_data['oflain_meropriyatiya'],
                'obrazovanie':form.cleaned_data['obrazovanie'],
                'telefon':form.cleaned_data['telefon'],
                'gorod':form.cleaned_data['gorod'],
                'razmer':form.cleaned_data['razmer'],
                'zakritie_proekti':form.cleaned_data['zakritie_proekti'],
                'god_nayma':form.cleaned_data['god_nayma'],
                'kursi':form.cleaned_data['kursi'],
                'otvet':otvet
                }
            
            form=Data(initial=form_data)
            ''''''

            
            serializer = DataSerializer(data=save_data)
            if serializer.is_valid():
                await serializer.asave()
            
            return render(
            request,
            "home.html",
            {'form':form, 'otvet': otvet},
            )
        else:
            return HttpResponse("False form.")
    elif request.method == 'GET':     
        form= Data()
        return render(
            request,
            "home.html",
            {'form':form}
        )

async def get_homepageABTest(request:HttpRequest):
#def get_homepage(request:HttpRequest):
    if request.method == 'POST':
        #print(request.POST)
        form = Data(request.POST)
        if form.is_valid():
            data={
                'Год_рождения':form.cleaned_data['god_rojdeniya'],
                'Подписаны_документы':form.cleaned_data['podpisani_documenti'],
                'Пол':form.cleaned_data['pol'],
                'БылПростой':form.cleaned_data['bil_prostoy'],
                'ОпытВДолжности':form.cleaned_data['opit_v_doljnosti'],
                'Активность':form.cleaned_data['activnost'],
                'Знак_зодиака':form.cleaned_data['znak_zodiaka'],
                'Возраст':form.cleaned_data['vozrast'],
                'Оценка_HR':form.cleaned_data['ocenka_hr'],
                'УровеньОплаты':form.cleaned_data['uroven_oplati'],
                'Офлайн_участие':form.cleaned_data['oflain_meropriyatiya'],
                'Образование':form.cleaned_data['obrazovanie'],
                'Телефон':form.cleaned_data['telefon'],
                'Город':form.cleaned_data['gorod'],
                'Размер':form.cleaned_data['razmer'],
                'Закрытые_проекты':form.cleaned_data['zakritie_proekti'],
                'ГодНайма':form.cleaned_data['god_nayma'],
                'Курсы':form.cleaned_data['kursi'],
                }
            form_data={
                'god_rojdeniya':form.cleaned_data['god_rojdeniya'],
                'podpisani_documenti':form.cleaned_data['podpisani_documenti'],
                'pol':form.cleaned_data['pol'],
                'bil_prostoy':form.cleaned_data['bil_prostoy'],
                'opit_v_doljnosti':form.cleaned_data['opit_v_doljnosti'],
                'activnost':form.cleaned_data['activnost'],
                'znak_zodiaka':form.cleaned_data['znak_zodiaka'],
                'vozrast':form.cleaned_data['vozrast'],
                'ocenka_hr':form.cleaned_data['ocenka_hr'],
                'uroven_oplati':form.cleaned_data['uroven_oplati'],
                'oflain_meropriyatiya':form.cleaned_data['oflain_meropriyatiya'],
                'obrazovanie':form.cleaned_data['obrazovanie'],
                'telefon':form.cleaned_data['telefon'],
                'gorod':form.cleaned_data['gorod'],
                'razmer':form.cleaned_data['razmer'],
                'zakritie_proekti':form.cleaned_data['zakritie_proekti'],
                'god_nayma':form.cleaned_data['god_nayma'],
                'kursi':form.cleaned_data['kursi'],
                }
            otvet, model_number= await model2(data)
            save_data={
                'model_number':model_number,
                'god_rojdeniya':form.cleaned_data['god_rojdeniya'],
                'podpisani_documenti':form.cleaned_data['podpisani_documenti'],
                'pol':form.cleaned_data['pol'],
                'bil_prostoy':form.cleaned_data['bil_prostoy'],
                'opit_v_doljnosti':form.cleaned_data['opit_v_doljnosti'],
                'activnost':form.cleaned_data['activnost'],
                'znak_zodiaka':form.cleaned_data['znak_zodiaka'],
                'vozrast':form.cleaned_data['vozrast'],
                'ocenka_hr':form.cleaned_data['ocenka_hr'],
                'uroven_oplati':form.cleaned_data['uroven_oplati'],
                'oflain_meropriyatiya':form.cleaned_data['oflain_meropriyatiya'],
                'obrazovanie':form.cleaned_data['obrazovanie'],
                'telefon':form.cleaned_data['telefon'],
                'gorod':form.cleaned_data['gorod'],
                'razmer':form.cleaned_data['razmer'],
                'zakritie_proekti':form.cleaned_data['zakritie_proekti'],
                'god_nayma':form.cleaned_data['god_nayma'],
                'kursi':form.cleaned_data['kursi'],
                'otvet':otvet
                }
            
            form=Data(initial=form_data)
            ''''''
            
            
            serializer = DataSerializerABTest(data=save_data)
            if serializer.is_valid():
                await serializer.asave()
            
            return render(
            request,
            "home.html",
            {'form':form, 'otvet': otvet,'model': model_number},
            )
        else:
            return HttpResponse("False form.")
    elif request.method == 'GET':     
        form= Data()
        return render(
            request,
            "home.html",
            {'form':form}
        )
    

class DataViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = ViewDataSerializer

class DataViewSetABTest(viewsets.ModelViewSet):
    queryset = DataModelABTest.objects.all()
    serializer_class = ViewDataSerializerABTest

class DataAPIView(APIView):
    async def get(self, request):
        try:
            otvet=  await model(request.data)
            save_data={
                'god_rojdeniya':request.data['Год_рождения'],
                'podpisani_documenti':request.data['Подписаны_документы'],
                'pol':request.data['Пол'],
                'bil_prostoy':request.data['БылПростой'],
                'opit_v_doljnosti':request.data['ОпытВДолжности'],
                'activnost':request.data['Активность'],
                'znak_zodiaka':request.data['Знак_зодиака'],
                'vozrast':request.data['Возраст'],
                'ocenka_hr':request.data['Оценка_HR'],
                'uroven_oplati':request.data['УровеньОплаты'],
                'oflain_meropriyatiya':request.data['Офлайн_участие'],
                'obrazovanie':request.data['Образование'],
                'telefon':request.data['Телефон'],
                'gorod':request.data['Город'],
                'razmer':request.data['Размер'],
                'zakritie_proekti':request.data['Закрытые_проекты'],
                'god_nayma':request.data['ГодНайма'],
                'kursi':request.data['Курсы'],
                'otvet':otvet
                }
            serializer = DataSerializer(data=save_data)
            if serializer.is_valid():
                await serializer.asave()
            return Response(otvet, status=201)
        except Exception:
                return Response(status=404)

class DataURLAPIView(APIView):
    async def get(self, request):
        try:
            data={
                'Год_рождения':float(request.query_params.get('god_rojdeniya')),
                'Подписаны_документы':request.query_params.get('podpisani_documenti'),
                'Пол':request.query_params.get('pol'),
                'БылПростой':request.query_params.get('bil_prostoy'),
                'ОпытВДолжности':float(request.query_params.get('opit_v_doljnosti')),
                'Активность':float(request.query_params.get('activnost')),
                'Знак_зодиака':request.query_params.get('znak_zodiaka'),
                'Возраст':float(request.query_params.get('vozrast')),
                'Оценка_HR':float(request.query_params.get('ocenka_hr')),
                'УровеньОплаты':float(request.query_params.get('uroven_oplati')),
                'Офлайн_участие':float(request.query_params.get('oflain_meropriyatiya')),
                'Образование':request.query_params.get('obrazovanie'),
                'Телефон':float(request.query_params.get('telefon')),
                'Город':request.query_params.get('gorod'),
                'Размер':request.query_params.get('razmer'),
                'Закрытые_проекты':float(request.query_params.get('zakritie_proekti')),
                'ГодНайма':float(request.query_params.get('god_nayma')),
                'Курсы':float(request.query_params.get('kursi'))
                }
            otvet= await model(data)
            save_data={
                'god_rojdeniya':float(request.query_params.get('god_rojdeniya')),
                'podpisani_documenti':request.query_params.get('podpisani_documenti'),
                'pol':request.query_params.get('pol'),
                'bil_prostoy':request.query_params.get('bil_prostoy'),
                'opit_v_doljnosti':float(request.query_params.get('opit_v_doljnosti')),
                'activnost':float(request.query_params.get('activnost')),
                'znak_zodiaka':request.query_params.get('znak_zodiaka'),
                'vozrast':float(request.query_params.get('vozrast')),
                'ocenka_hr':float(request.query_params.get('ocenka_hr')),
                'uroven_oplati':float(request.query_params.get('uroven_oplati')),
                'oflain_meropriyatiya':float(request.query_params.get('oflain_meropriyatiya')),
                'obrazovanie':request.query_params.get('obrazovanie'),
                'telefon':float(request.query_params.get('telefon')),
                'gorod':request.query_params.get('gorod'),
                'razmer':request.query_params.get('razmer'),
                'zakritie_proekti':float(request.query_params.get('zakritie_proekti')),
                'god_nayma':float(request.query_params.get('god_nayma')),
                'kursi':float(request.query_params.get('kursi')),
                'otvet':int(otvet) 
                }
            
            serializer = DataSerializer(data=save_data)
            if serializer.is_valid():
                await serializer.asave()
            return Response(otvet, status=201)
        except Exception:
                return Response(status=404)

class DataAPIViewABTest(APIView):
    async def get(self, request):
        try:
            otvet, model_number= await model2(request.data)
            save_data={
                 'model_number':int(model_number),
                'god_rojdeniya':request.data['Год_рождения'],
                'podpisani_documenti':request.data['Подписаны_документы'],
                'pol':request.data['Пол'],
                'bil_prostoy':request.data['БылПростой'],
                'opit_v_doljnosti':request.data['ОпытВДолжности'],
                'activnost':request.data['Активность'],
                'znak_zodiaka':request.data['Знак_зодиака'],
                'vozrast':request.data['Возраст'],
                'ocenka_hr':request.data['Оценка_HR'],
                'uroven_oplati':request.data['УровеньОплаты'],
                'oflain_meropriyatiya':request.data['Офлайн_участие'],
                'obrazovanie':request.data['Образование'],
                'telefon':request.data['Телефон'],
                'gorod':request.data['Город'],
                'razmer':request.data['Размер'],
                'zakritie_proekti':request.data['Закрытые_проекты'],
                'god_nayma':request.data['ГодНайма'],
                'kursi':request.data['Курсы'],
                'otvet':otvet
                }
            serializer = DataSerializerABTest(data=save_data)
            if serializer.is_valid():
                await serializer.asave()
            return Response(otvet, status=201)
        except Exception:
                return Response(status=404)

class DataURLAPIViewABTest(APIView):
    async def get(self, request):
        try:
            data={
                'Год_рождения':float(request.query_params.get('god_rojdeniya')),
                'Подписаны_документы':request.query_params.get('podpisani_documenti'),
                'Пол':request.query_params.get('pol'),
                'БылПростой':request.query_params.get('bil_prostoy'),
                'ОпытВДолжности':float(request.query_params.get('opit_v_doljnosti')),
                'Активность':float(request.query_params.get('activnost')),
                'Знак_зодиака':request.query_params.get('znak_zodiaka'),
                'Возраст':float(request.query_params.get('vozrast')),
                'Оценка_HR':float(request.query_params.get('ocenka_hr')),
                'УровеньОплаты':float(request.query_params.get('uroven_oplati')),
                'Офлайн_участие':float(request.query_params.get('oflain_meropriyatiya')),
                'Образование':request.query_params.get('obrazovanie'),
                'Телефон':float(request.query_params.get('telefon')),
                'Город':request.query_params.get('gorod'),
                'Размер':request.query_params.get('razmer'),
                'Закрытые_проекты':float(request.query_params.get('zakritie_proekti')),
                'ГодНайма':float(request.query_params.get('god_nayma')),
                'Курсы':float(request.query_params.get('kursi'))
                }
            otvet, model_number= await model2(data)
            save_data={
                'model_number':int(model_number),
                'god_rojdeniya':float(request.query_params.get('god_rojdeniya')),
                'podpisani_documenti':request.query_params.get('podpisani_documenti'),
                'pol':request.query_params.get('pol'),
                'bil_prostoy':request.query_params.get('bil_prostoy'),
                'opit_v_doljnosti':float(request.query_params.get('opit_v_doljnosti')),
                'activnost':float(request.query_params.get('activnost')),
                'znak_zodiaka':request.query_params.get('znak_zodiaka'),
                'vozrast':float(request.query_params.get('vozrast')),
                'ocenka_hr':float(request.query_params.get('ocenka_hr')),
                'uroven_oplati':float(request.query_params.get('uroven_oplati')),
                'oflain_meropriyatiya':float(request.query_params.get('oflain_meropriyatiya')),
                'obrazovanie':request.query_params.get('obrazovanie'),
                'telefon':float(request.query_params.get('telefon')),
                'gorod':request.query_params.get('gorod'),
                'razmer':request.query_params.get('razmer'),
                'zakritie_proekti':float(request.query_params.get('zakritie_proekti')),
                'god_nayma':float(request.query_params.get('god_nayma')),
                'kursi':float(request.query_params.get('kursi')),
                'otvet':int(otvet) 
                }
            
            serializer = DataSerializerABTest(data=save_data)
            if serializer.is_valid():
                await serializer.asave()
            return Response(otvet, status=201)
        except Exception:
                return Response(status=404)