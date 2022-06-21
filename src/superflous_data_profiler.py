import base64
import pandas as pd
import math

def encode_image(file_name):
    data_uri = base64.b64encode(open(file_name, 'rb').read()).decode('utf-8')
    img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
    return(img_tag)


def create_test_data():
    data = {'name': ['Skipper', 'Fish', 'Dragon'],
        'name_tag': ['Skipper_dog', 'Fish_cat', 'Dragon_cat'],
        'n': [10000000, 500, 400],
        'missing': [99, 9, 0],
        'nonmissing': [901, 491, 400],
        'missing_ratio': [0.001, 0.2, 0],
        'unique': [100, 50, 40],
        'unique_ratio': [0.5, 0.4, 0.3],
        'pct_5': [.001, 1, 3],
        'cv': [1,2,3],
        'mean': [11,22,33],
        'std_dev': [1.1,2.2,3.3],
        'median': [5,7,11],
        'iqr': [2.3,4,2.5], 
        'pct_95': [44,55,66],
        'mad': [3,4,5],
        'outlier_floor': [0.001,23,44],
        'outlier_floor_pct': [1,3,2],
        'outlier_ceiling': [444333222, 14440, 2000],
        'outlier_ceiling_pct': [0.99, 0.98, 0.96],
        'outliers': [4, 22, 13],
        'outlier_ratio': [0.01, 0.2, 0.13],
        'proportions': [dict(zip([0.1,23,3,4,5], [0.2, 0.2, 0.1, 0.04, 0])),
                   dict(zip([10, 20, 30], [0.33, 0.22, 0.11])),
                   dict(zip([100, 200, 300], [0.6, 0.5, 0.4]))],
        'values': [[121, 1, 44, 234, 19, 249, '...', 234, 44, 11, 22, 66],
                  [1,2,3,4,5,'...',6,7,8,9,10],
                  [92, 92, 92, 92, 92, '...', 92, 92, 92, 92, 92]],
        'is_unique': [False, False, True],
        'is_zero_variance': [True, True, False]
       }
    df = pd.DataFrame(data)
    return(df)


def number_eda_round(x):
    magnitude = math.log10(abs(x)  + 0.0000001) # small number to prevent log10(0) error
    digits = max(0, math.floor(3 - magnitude))
    x = round(x, digits)
    if x >= 100:
        x = int(x)
    return(x)


def pretty_format(x, round = True, nbsp = True):
    if round:
        x = number_eda_round(x)
    remove_dot = False
    # new
    # x = f'{x:13.3f}'.rstrip('0').rstrip('.')  # without commas
    # x = f'{x:15,.3f}'.rstrip('0').rstrip('.') # with comma, but throughs off alignment
    x = f'{x:15,.3f}'.rstrip('0')
    if x[-1:]=='.':
        remove_dot = True
    x = x.ljust(15, ' ')
    
    if nbsp:
        dot_replacement = '&nbsp;'
    else:
        dot_replacement = ' '
        
    if nbsp:
        x =  x.replace(' ', '&numsp;')
        if remove_dot:
            x =  x.replace('.', '&nbsp;')
    else:
        if remove_dot:
            x =  x.replace('.', ' ')
    
    return(x)

# numbers = [-123.03033, 1.3203, 0.456781, -70000002.18, 50000000, 13.1231, 0.1, .6666, 100.222, -4000000.1231]
# for number in numbers:
#     print(number_eda_format(number))
