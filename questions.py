from sheet_reader import get_questions_from_sheet

# Google Sheets-dən sualları alırıq
QUESTIONS = get_questions_from_sheet()

def get_question(level='normal'):
    # Çətinlik səviyyəsinə əsaslanaraq sualları qaytarırıq
    # Bu nümunədə sadəcə normal səviyyəni seçirik
    question_data = QUESTIONS[0]  # İlk sualı götürürük
    question = question_data['Sual']
    options = [question_data[f'Cavab {i}'] for i in range(1, 6)]
    correct_answer = question_data['Doğru Cavab']
    
    return question, options, correct_answer
