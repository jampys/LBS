__author__ = 'Titan'

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = 15, 8  #ancho, alto

n_groups=12 #cantidad de grupos

media_cr = [1, 5, 8, 9, 7, 6, 9, 1, 9, 6, 4, 4]

media_co = [1, 5, 8, 9, 7, 6, 9, 1, 9, 6, 4, 4]

plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35 #ancho de cada barra



plt.bar(index, media_cr, bar_width,
                 color='b',
                 label='CR')

plt.bar(index + bar_width, media_co, bar_width,
                 color='r',
                 label='CO')


plt.xlabel('Mes') #etiqueta eje x
plt.ylabel('Temperatura media') #etiqueta eje y
plt.title('Temperatura media CR CO por mes CR-CO año 20') #titulo del grafico
plt.xticks(index + bar_width, ('Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic'))
#plt.legend()

#plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#plt.tight_layout()
plt.show()

