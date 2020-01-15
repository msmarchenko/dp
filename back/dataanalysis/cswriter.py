import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back.back.settings")
# from models import Machine, KPI
from datetime import datetime
# s = pd.read_csv('C:\\Users\\Mteterin\\Desktop\\dp\\back\\overview_raw_data.csv')
with open('C:\\Users\\Mteterin\\Desktop\\dp\\back\\overview_raw_data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if index <= 67000 or row[22].replace(',','.') == 'no data':
            continue

        datetime_object = datetime.strptime(row[1], '%d.%m.%Y %H:%M')
        machine, created = Machine.objects.get_or_create(name=row[0])
        _, created = KPI.objects.get_or_create(date=datetime_object,
                                               werk=machine, kd_name=row[5],rezeptur=row[15],
                                               material=row[17], polymer=row[21], dicke=float(row[9]),
                                               menge= float(row[20].replace(',','.')), yields = float(row[22].replace(',','.')) )
        if index % 1000 == 0:
            print(index, row)