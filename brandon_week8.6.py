#6) Temperature Entries Until “stop” (Min and Max)
def temp_stats():
    temps = []
    min_temp = 0
    max_temp = 0
    while True:
        temp = input('Enter a temperature (type stop to finish): ')
        if temp != 'stop':
            temps.append(float(temp))
            if float(temp) == min(temps):
                min_temp = float(temp)
            if float(temp) == max(temps):
                max_temp = float(temp)

        if temp == 'stop':
            if not temps:
                temps = ['No temperature entered']
                print(temps[0])
                break
            else:
                break
    print(f'Minimum: {min_temp:.1f}\nMaximum: {max_temp:.1f}')

temp_stats()