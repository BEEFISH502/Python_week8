##1) Enter Scores Until Done (Average)
scores = []

def score_count():
    while True:
        score = int(input('Enter a quiz score (-1 to stop): '))
        if score != -1:
            scores.append(score)
        elif score == -1:
            break

def averages():
    count = 0
    total = 0
    for i in scores:
        count += 1
        total = sum(scores)
        average = total / count
        if count == 0 or total == 0:
            print('Failed all quizzes')
            break
    print(f'Average score: {average:.1f}')


score_count()
averages()