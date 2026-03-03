import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

df_path= os.path.join(BASE_DIR,'model/static/X_test.csv')
cm_path= os.path.join(BASE_DIR,'model/static/catboost_model_096.cbm')
catmodel = CatBoostClassifier() 
catmodel.load_model(cm_path) 

catmodel1 = CatBoostClassifier() 
catmodel1.load_model(cm_path) 
catmodel2 = CatBoostClassifier() 
catmodel2.load_model(cm_path) 
df_test=pd.read_csv(df_path)
Chooser=0

async def model(quary):
    global catmodel 
    global df_test
    dt=df_test.copy(deep=True)
    dt.loc[len(dt)] = quary
    dt=dt.drop(['Подписаны_документы'],axis=1)
    dt=dt.drop(['Год_рождения'],axis=1)
    dt=dt.drop(['Телефон'],axis=1)



    from sklearn.preprocessing import LabelEncoder, StandardScaler, OrdinalEncoder
    le = LabelEncoder()
    ss=StandardScaler()

    numerical_features = ['ОпытВДолжности', 'Активность', 'Возраст', 'Оценка_HR', 'УровеньОплаты','Закрытые_проекты','ГодНайма','Курсы']

    from sklearn.compose import ColumnTransformer

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features)
        ],
        remainder='passthrough'
    )

    scaled_data = preprocessor.fit_transform(dt)

    dt = pd.DataFrame(scaled_data, columns=preprocessor.get_feature_names_out())

    dt=dt.rename(columns={'num__ОпытВДолжности': 'ОпытВДолжности',
                                            'num__Активность': 'Активность', 
                                            'num__Возраст': 'Возраст', 
                                            'num__Оценка_HR': 'Оценка_HR', 
                                            'num__УровеньОплаты': 'УровеньОплаты', 
                                            'num__Закрытые_проекты': 'Закрытые_проекты', 
                                            'num__ГодНайма': 'ГодНайма', 
                                            'num__Курсы': 'Курсы', 
                                            'remainder__Подписаны_документы': 'Подписаны_документы', 
                                            'remainder__Пол': 'Пол',
                                            'remainder__БылПростой': 'БылПростой', 
                                            'remainder__Знак_зодиака': 'Знак_зодиака', 
                                            'remainder__Офлайн_участие': 'Офлайн_участие',
                                            'remainder__Образование': 'Образование', 
                                            'remainder__Город': 'Город', 
                                            'remainder__Размер': 'Размер'})
    new_order= ['Подписаны_документы',
    'Пол',
    'БылПростой',
    'ОпытВДолжности',
    'Активность',
    'Знак_зодиака',
    'Возраст',
    'Оценка_HR',
    'УровеньОплаты',
    'Офлайн_участие',
    'Образование',
    'Город',
    'Размер',
    'Закрытые_проекты',
    'ГодНайма',
    'Курсы']
    encoder = OrdinalEncoder(categories=[['M', 'XS', 'L', 'XL', 'S', 'XXL']])
    dt['Размер'] = encoder.fit_transform(dt[['Размер']])
    encoder = OrdinalEncoder(categories=[['Bachelors', 'Masters', 'PHD']])
    dt['Образование'] = encoder.fit_transform(dt[['Образование']])
    encoder = OrdinalEncoder(categories=[['Pune', 'New Delhi', 'Bangalore']])
    dt['Город'] = encoder.fit_transform(dt[['Город']])
    encoder = OrdinalEncoder(categories=[['Male', 'Female']])
    dt['Пол'] = encoder.fit_transform(dt[['Пол']])
    encoder = OrdinalEncoder(categories=[['No', 'Yes']])
    dt['БылПростой'] = encoder.fit_transform(dt[['БылПростой']])
    encoder = OrdinalEncoder(categories=[['Рыбы','Козерог','Близнецы','Рак','Телец','Дева','Стрелец','Весы','Овен','Водолей','Лев', 'Скорпион']])
    dt['Знак_зодиака'] = encoder.fit_transform(dt[['Знак_зодиака']])

    dt['Пол']=dt['Пол'].astype(int)
    dt['БылПростой']=dt['БылПростой'].astype(int)
    dt['Знак_зодиака']=dt['Знак_зодиака'].astype(int)
    dt['Офлайн_участие']=dt['Офлайн_участие'].astype(int)
    dt['Размер']=dt['Размер'].astype(int)
    dt['Образование']=dt['Образование'].astype(int)
    dt['Город']=dt['Город'].astype(int)

    dt['ОпытВДолжности']=dt['ОпытВДолжности'].astype(float)
    dt['Активность']=dt['Активность'].astype(float)
    dt['Возраст']=dt['Возраст'].astype(float)
    dt['Оценка_HR']=dt['Оценка_HR'].astype(float)
    dt['УровеньОплаты']=dt['УровеньОплаты'].astype(float)
    dt['Закрытые_проекты']=dt['Закрытые_проекты'].astype(float)
    dt['ГодНайма']=dt['ГодНайма'].astype(float)
    dt['Курсы']=dt['Курсы'].astype(float)
    quary=	dt.iloc[-1]

    return catmodel.predict(quary)

async def model2(quary):
    global catmodel, catmodel1, catmodel2
    global df_test
    global Chooser
    ostatok=Chooser%2
    
    if ostatok==0:
        dt=df_test.copy(deep=True)
        dt.loc[len(dt)] = quary
        dt=dt.drop(['Подписаны_документы'],axis=1)
        dt=dt.drop(['Год_рождения'],axis=1)
        dt=dt.drop(['Телефон'],axis=1)



        from sklearn.preprocessing import LabelEncoder, StandardScaler, OrdinalEncoder
        le = LabelEncoder()
        ss=StandardScaler()

        numerical_features = ['ОпытВДолжности', 'Активность', 'Возраст', 'Оценка_HR', 'УровеньОплаты','Закрытые_проекты','ГодНайма','Курсы']

        from sklearn.compose import ColumnTransformer

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features)
            ],
            remainder='passthrough'
        )

        scaled_data = preprocessor.fit_transform(dt)

        dt = pd.DataFrame(scaled_data, columns=preprocessor.get_feature_names_out())

        dt=dt.rename(columns={'num__ОпытВДолжности': 'ОпытВДолжности',
                                                'num__Активность': 'Активность', 
                                                'num__Возраст': 'Возраст', 
                                                'num__Оценка_HR': 'Оценка_HR', 
                                                'num__УровеньОплаты': 'УровеньОплаты', 
                                                'num__Закрытые_проекты': 'Закрытые_проекты', 
                                                'num__ГодНайма': 'ГодНайма', 
                                                'num__Курсы': 'Курсы', 
                                                'remainder__Подписаны_документы': 'Подписаны_документы', 
                                                'remainder__Пол': 'Пол',
                                                'remainder__БылПростой': 'БылПростой', 
                                                'remainder__Знак_зодиака': 'Знак_зодиака', 
                                                'remainder__Офлайн_участие': 'Офлайн_участие',
                                                'remainder__Образование': 'Образование', 
                                                'remainder__Город': 'Город', 
                                                'remainder__Размер': 'Размер'})
        new_order= ['Подписаны_документы',
        'Пол',
        'БылПростой',
        'ОпытВДолжности',
        'Активность',
        'Знак_зодиака',
        'Возраст',
        'Оценка_HR',
        'УровеньОплаты',
        'Офлайн_участие',
        'Образование',
        'Город',
        'Размер',
        'Закрытые_проекты',
        'ГодНайма',
        'Курсы']
        encoder = OrdinalEncoder(categories=[['M', 'XS', 'L', 'XL', 'S', 'XXL']])
        dt['Размер'] = encoder.fit_transform(dt[['Размер']])
        encoder = OrdinalEncoder(categories=[['Bachelors', 'Masters', 'PHD']])
        dt['Образование'] = encoder.fit_transform(dt[['Образование']])
        encoder = OrdinalEncoder(categories=[['Pune', 'New Delhi', 'Bangalore']])
        dt['Город'] = encoder.fit_transform(dt[['Город']])
        encoder = OrdinalEncoder(categories=[['Male', 'Female']])
        dt['Пол'] = encoder.fit_transform(dt[['Пол']])
        encoder = OrdinalEncoder(categories=[['No', 'Yes']])
        dt['БылПростой'] = encoder.fit_transform(dt[['БылПростой']])
        encoder = OrdinalEncoder(categories=[['Рыбы','Козерог','Близнецы','Рак','Телец','Дева','Стрелец','Весы','Овен','Водолей','Лев', 'Скорпион']])
        dt['Знак_зодиака'] = encoder.fit_transform(dt[['Знак_зодиака']])

        dt['Пол']=dt['Пол'].astype(int)
        dt['БылПростой']=dt['БылПростой'].astype(int)
        dt['Знак_зодиака']=dt['Знак_зодиака'].astype(int)
        dt['Офлайн_участие']=dt['Офлайн_участие'].astype(int)
        dt['Размер']=dt['Размер'].astype(int)
        dt['Образование']=dt['Образование'].astype(int)
        dt['Город']=dt['Город'].astype(int)

        dt['ОпытВДолжности']=dt['ОпытВДолжности'].astype(float)
        dt['Активность']=dt['Активность'].astype(float)
        dt['Возраст']=dt['Возраст'].astype(float)
        dt['Оценка_HR']=dt['Оценка_HR'].astype(float)
        dt['УровеньОплаты']=dt['УровеньОплаты'].astype(float)
        dt['Закрытые_проекты']=dt['Закрытые_проекты'].astype(float)
        dt['ГодНайма']=dt['ГодНайма'].astype(float)
        dt['Курсы']=dt['Курсы'].astype(float)
        quary=	dt.iloc[-1]
        Chooser=Chooser+1
        return catmodel1.predict(quary), 1
    
    else:
        dt=df_test.copy(deep=True)
        dt.loc[len(dt)] = quary
        dt=dt.drop(['Подписаны_документы'],axis=1)
        dt=dt.drop(['Год_рождения'],axis=1)
        dt=dt.drop(['Телефон'],axis=1)



        from sklearn.preprocessing import LabelEncoder, StandardScaler, OrdinalEncoder
        le = LabelEncoder()
        ss=StandardScaler()

        numerical_features = ['ОпытВДолжности', 'Активность', 'Возраст', 'Оценка_HR', 'УровеньОплаты','Закрытые_проекты','ГодНайма','Курсы']

        from sklearn.compose import ColumnTransformer

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features)
            ],
            remainder='passthrough'
        )

        scaled_data = preprocessor.fit_transform(dt)

        dt = pd.DataFrame(scaled_data, columns=preprocessor.get_feature_names_out())

        dt=dt.rename(columns={'num__ОпытВДолжности': 'ОпытВДолжности',
                                                'num__Активность': 'Активность', 
                                                'num__Возраст': 'Возраст', 
                                                'num__Оценка_HR': 'Оценка_HR', 
                                                'num__УровеньОплаты': 'УровеньОплаты', 
                                                'num__Закрытые_проекты': 'Закрытые_проекты', 
                                                'num__ГодНайма': 'ГодНайма', 
                                                'num__Курсы': 'Курсы', 
                                                'remainder__Подписаны_документы': 'Подписаны_документы', 
                                                'remainder__Пол': 'Пол',
                                                'remainder__БылПростой': 'БылПростой', 
                                                'remainder__Знак_зодиака': 'Знак_зодиака', 
                                                'remainder__Офлайн_участие': 'Офлайн_участие',
                                                'remainder__Образование': 'Образование', 
                                                'remainder__Город': 'Город', 
                                                'remainder__Размер': 'Размер'})
        new_order= ['Подписаны_документы',
        'Пол',
        'БылПростой',
        'ОпытВДолжности',
        'Активность',
        'Знак_зодиака',
        'Возраст',
        'Оценка_HR',
        'УровеньОплаты',
        'Офлайн_участие',
        'Образование',
        'Город',
        'Размер',
        'Закрытые_проекты',
        'ГодНайма',
        'Курсы']
        encoder = OrdinalEncoder(categories=[['M', 'XS', 'L', 'XL', 'S', 'XXL']])
        dt['Размер'] = encoder.fit_transform(dt[['Размер']])
        encoder = OrdinalEncoder(categories=[['Bachelors', 'Masters', 'PHD']])
        dt['Образование'] = encoder.fit_transform(dt[['Образование']])
        encoder = OrdinalEncoder(categories=[['Pune', 'New Delhi', 'Bangalore']])
        dt['Город'] = encoder.fit_transform(dt[['Город']])
        encoder = OrdinalEncoder(categories=[['Male', 'Female']])
        dt['Пол'] = encoder.fit_transform(dt[['Пол']])
        encoder = OrdinalEncoder(categories=[['No', 'Yes']])
        dt['БылПростой'] = encoder.fit_transform(dt[['БылПростой']])
        encoder = OrdinalEncoder(categories=[['Рыбы','Козерог','Близнецы','Рак','Телец','Дева','Стрелец','Весы','Овен','Водолей','Лев', 'Скорпион']])
        dt['Знак_зодиака'] = encoder.fit_transform(dt[['Знак_зодиака']])

        dt['Пол']=dt['Пол'].astype(int)
        dt['БылПростой']=dt['БылПростой'].astype(int)
        dt['Знак_зодиака']=dt['Знак_зодиака'].astype(int)
        dt['Офлайн_участие']=dt['Офлайн_участие'].astype(int)
        dt['Размер']=dt['Размер'].astype(int)
        dt['Образование']=dt['Образование'].astype(int)
        dt['Город']=dt['Город'].astype(int)

        dt['ОпытВДолжности']=dt['ОпытВДолжности'].astype(float)
        dt['Активность']=dt['Активность'].astype(float)
        dt['Возраст']=dt['Возраст'].astype(float)
        dt['Оценка_HR']=dt['Оценка_HR'].astype(float)
        dt['УровеньОплаты']=dt['УровеньОплаты'].astype(float)
        dt['Закрытые_проекты']=dt['Закрытые_проекты'].astype(float)
        dt['ГодНайма']=dt['ГодНайма'].astype(float)
        dt['Курсы']=dt['Курсы'].astype(float)
        quary=	dt.iloc[-1]
        Chooser=Chooser+1
        return catmodel2.predict(quary), 2