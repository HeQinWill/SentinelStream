import boto3
import re
import pandas as pd
from pathlib import Path
from tqdm import tqdm

s3 = boto3.resource('s3', 
                aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
                aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                endpoint_url='https://eodata.dataspace.copernicus.eu',
                )
bucket = s3.Bucket('eodata')

for bucket_object in bucket.objects.all():
   print(bucket_object.key)

for d in date:
    yyyy = str(d.year).zfill(4)
    mm = str(d.month).zfill(2)
    dd = str(d.day).zfill(2)
    print(yyyy, mm, dd)
  
    SPEC = 'NO2___'  # CH4___, NO2___, O3____, O3_TCL, SO2___, CO____, ...
  
    b_list = bucket.objects.filter(Prefix=f'Sentinel-5P/TROPOMI/L2__{SPEC}/{yyyy}/{mm}/{dd}')
    b_list = [i.key for i in list(b_list)]
    print(len(b_list))

    pattern = f"S5P_{TYPE}_L2__{SPEC}_{yyyy}{mm}{dd}T0[1-6].*nc"
    r_list = [i for i in b_list if re.search(pattern, i)]
    print(len(r_list))
  
    for r in tqdm(r_list[:]):
        obj = bucket.Object(r)
        target_folder = Path(f'./{yyyy}{mm}{dd}')
        target = target_folder/(r.split('/')[-1])
        if target.exists():
            print('Found file:', r)
        else:
            target_folder.mkdir(parents=True, exist_ok=True)
            obj.download_file(str(target))
        # (or using awscli directly)
        # !aws s3 cp s3://eodata/{r} {yyyy}{mm}{dd} --endpoint-url https://eodata.dataspace.copernicus.eu
