# Trendy wzrostowe / spadkowe / boczne
#
# 1) Na podstawie wskaźnika RSI sklasyfikować każdy zasób i obok wykresu dodać informację
# (graficzną / tekstową) o typie trendu w jakim aktualnie się znajduje. (4pkt)
#
# 2) Pośród trzech wyświetlanych wykresów na bieżąco oznaczać zasób, który ma największy wolumen
# spośród zasobów nie będących w trendzie spadkowym.
# Przykładowo: wyświetlamy LTCBTC, DASHBTC, ETHBTC. Dwa pierwsze są w trendzie wzrostowym,
# ostatni w spadkowym. Pierwszy ma wyraźnie najwyższy wolumen. Oznaczamy go jako kandydata. (3pkt)
#
# 3) Do funkcjonalności wyświetlania zasobów na wykresach, klasyfikacji ich trendu i wyboru
# najbardziej interesującego dodać obserwację wartości transakcji oraz ofert w czasie rzeczywistym.
# Jeśli któryś z obserwowanych zasobów jest oznaczony jako kandydat - obserwujemy wartości
# zawieranych na nim transackji.
# a) jeśli w ciągu Y ostatnich próbek wystąpiły na nim wahania większe niż X % - podpisujemy go
# dodatkowo jako zmienny ('volatile asset'). (1.5pkt)
# b) jeśli różnica między ofertami kupna / sprzedaży jest mniejsza niż S % (spread)
# oznaczamy go dodatkowo jako 'liquid asset' (charakteryzujący się płynnym rynkiem). (1.5pkt)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests
import time
