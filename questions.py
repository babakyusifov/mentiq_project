from data_retriever import get_sheet

# Google Sheets-dən sualları alırıq
def get_questions_from_sheet():
    sheet = get_sheet()
    if sheet:
        questions = sheet.get_all_records()
        return questions
    return []

QUESTIONS = get_questions_from_sheet()

def get_question(level='normal'):
    # Çətinlik səviyyəsinə əsaslanaraq sualları qaytarırıq
    # Bu nümunədə sadəcə normal səviyyəni seçirik
    question_data = QUESTIONS[0]  # İlk sualı götürürük
    question = question_data['Sual']
    options = [question_data[f'Cavab {i}'] for i in range(1, 6)]
    correct_answer = question_data['Doğru Cavab']
    
    return question, options, correct_answer
