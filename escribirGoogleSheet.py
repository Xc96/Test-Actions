import gspread

gc = gspread.service_account("credentials.json")

sheet = gc.open_by_key("1G1Z6BY6ZvdiuBFmYREHkpKHOxI3E4mbVuCv06SP9-x4")
ws = sheet.worksheet("Hoja1")

textos = [
    "Texto 1",
    "Texto 2",
    "Texto 3",
    "Texto 4"
]

for i, texto in enumerate(textos, start=1):
    ws.update_cell(i, 1, texto)   # Columna A
