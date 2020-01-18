def convert(number):
    response = ''

    if number % 3 == 0:
        response = response + 'Pling'

    if number % 5 == 0:
        response = response + 'Plang'
 
    if number % 7 == 0:
        response = response + 'Plong'

    if response != '':
        return response
    else:
        return str(number)

