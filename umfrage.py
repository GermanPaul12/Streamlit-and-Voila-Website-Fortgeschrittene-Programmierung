import requests
import pandas as pd

class Credentials:
    api_url = "https://api.sheety.co/986330bc80cb53b1444abc4dc001bec9/answersFortgeschritteneProgrammierung/formResponses1"
def get_data():    
    response = requests.get(Credentials.api_url)
    data = response.json()
    df = pd.DataFrame([[0,0]], columns = [["Streamlit", "Voila"]])
    for i in data["formResponses1"]:
        if i["wasFindetIhrBesser?"] == "Streamlit":
            df.Streamlit += 1
        elif i["wasFindetIhrBesser?"] == "Voila":
            df.Voila += 1    
    df.to_csv("UmfrageDaten.csv", index = False)        