import pandas as pd

ALL_COLUMN_NAMES = ['Sale', 'SalesAmountInEuro', 'time_delay_for_conversion', 'click_timestamp',
                    'nb_clicks_1week', 'product_price', 'product_age_group', 'device_type',
                    'product_gender', 'product_brand','product_category(1)', 'product_category(2)',
                    'product_category(3)', 'product_category(4)','product_category(5)',
                    'product_category(6)', 'product_category(7)', 'product_country', 'product_id',
                    'product_title', 'partner_id', 'user_id']

PARTNER_ID = 'BD01BAFAE73CF38C403978BBB458300C'

df = pd.DataFrame()
for chunk in pd.read_csv("../CriteoSearchData", names=ALL_COLUMN_NAMES, sep='\t', low_memory=False, chunksize=10):
    filtered_chunk = chunk[chunk['partner_id'] == PARTNER_ID]
    print(chunk)
    break
