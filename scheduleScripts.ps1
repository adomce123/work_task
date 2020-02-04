SCHTASKS /CREATE /SC ONCE /TN "MICROSOFT\BiggestLowest6" /TR "C:\Users\bd6612\Scripts\grafana_sound.py" /ST 12:11 /RU "BD6612" /RL HIGHEST
SCHTASKS /QUERY /TN "MICROSOFT\BiggestLowest6"