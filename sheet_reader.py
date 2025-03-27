import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API üçün icazələr
def authenticate_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    # JSON açarını istifadə edirik
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'iqtestbot-881850c89916.json', scope
    )

    # API ilə əlaqə qururuq
    client = gspread.authorize(creds)
    return client

# Google Sheets faylından məlumatları əldə etmək
def get_questions_from_sheet():
    client = authenticate_google_sheets()

    # Google Sheets faylını ID ilə açırıq
    sheet = client.open_by_key("1wsiRD6lmqQntZrQL8VqLFFWKvJqbsl4OEPZOv99y090").sheet1  # Google Sheets faylının ID-si
    questions = sheet.get_all_records()  # Cədvəldəki bütün məlumatları oxuyur
    return questions

# Məlumatları çap edirik (Test üçün)
if __name__ == "__main__":
    questions = get_questions_from_sheet()
    print(questions)
