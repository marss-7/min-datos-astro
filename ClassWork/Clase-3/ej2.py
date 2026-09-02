import numpy as np
import pandas as pd

NaN = ""
datos = {
    'Objeto': ['M31', 'M33', 'NGC104', 'NGC6752', 'idk', 'MASdj', 'asas', 'Balatro'],
    'Bmag': [545, 76, None, None,45, None, 7.8, 96],
    'Vmag': [None, 850, None, 4.0, 4.5, 70, None, 45]}

df = pd.DataFrame(datos)

colors = np.array(datos['Bmag']) - np.array(datos['Vmag'])
df['Color'] = colors

print(df)
