import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'iqtestbot-881850c89916.json', scope
    )

    client = gspread.authorize(creds)
    return client

def get_sheet():
    client = authenticate_google_sheets()
    try:
        # Google Sheets faylına bağlantı qurma
        sheet = client.open_by_key("1wsiRD6lmqQntZrQL8VqLFFWKvJqbsl4OEPZOv99y090").sheet1
        print("Google Sheets faylı uğurla açıldı!")
        return sheet
    except gspread.exceptions.APIError:
        # API icazəsi ilə bağlı səhvləri idarə etmə
        print("Google Sheets faylına giriş hüququ yoxdur! İcazələri yoxlayın.")
    except Exception as e:
        # Digər növ səhvləri idarə etmə
        print(f"Başqa bir problem meydana gəldi: {e}")

# Məlumatları çap edirik (Test üçün)
if __name__ == "__main__":
    sheet = get_sheet()
    if sheet:
        questions = sheet.get_all_records()
        print(questions)
