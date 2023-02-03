import requests

def transfer_data(patient):
    data={
        'name':patient.name,
        'age':patient.age,
        'gender':patient.gender,
        'address':patient.address,
        'medical_history':patient.medical_history,
    }

    response = requests.post('https://destination.server/api/patient/',data=data)
    if response.status_code==200:
        return "transfer successful"
    else:
        return "transfer failed"