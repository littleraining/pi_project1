import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("raspberrytest-90985-firebase-adminsdk-1xbs3-3631547d0f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberrytest-90985-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('restricted_access/secret_document')
print(ref.get())