import requests

def add_patient(name, age, gender, address, medical_history):
    data = {
        'name': name,
        'age': age,
        'gender':gender,
        'address': address,
        'medical_history': medical_history,
    }
    response = requests.post('http://localhost:8000/patients/', data=data)
    if response.status_code == 201:
        print('Patient added successfully')
    else:
        print('Failed to add patient')

if __name__ == '_main_':
    add_patient('Aditya', 25, 'Male','Thane', 'None')
    add_patient('Vikas', 24, 'Male','Vikroli', 'None')
    add_patient('Karan', 23, 'Male','Worli', 'None')
    add_patient('Pritesh', 22, 'Male','Kanjur Marg', 'None')


