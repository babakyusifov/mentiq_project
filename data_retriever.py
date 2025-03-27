import gspread

try:
    # Google Sheets faylına bağlantı qurma
    sheet = client.open_by_key("1wsiRD6lmqQntZrQL8VqLFFWKvJqbsl4OEPZOv99y090").sheet1
    print("Google Sheets faylı uğurla açıldı!")
except gspread.exceptions.APIError:
    # API icazəsi ilə bağlı səhvləri idarə etmə
    print("Google Sheets faylına giriş hüququ yoxdur! İcazələri yoxlayın.")
except Exception as e:
    # Digər növ səhvləri idarə etmə
    print(f"Başqa bir problem meydana gəldi: {e}")
