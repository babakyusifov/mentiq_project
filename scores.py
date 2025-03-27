# Skorları saxlamaq üçün sadə bir lüğət
USER_SCORES = {}

# Skoru yeniləmək və göstərmək
def update_score(user_id):
    return USER_SCORES.get(user_id, 0)

def add_score(user_id, score):
    if user_id in USER_SCORES:
        USER_SCORES[user_id] += score
    else:
        USER_SCORES[user_id] = score
