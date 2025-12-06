import streamlit as st
import requests



def get_cordinates (name):


    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

    response=requests.get(url)

    # st.write(response.status_code)
    # st.write(response.text)
    # st.write(response.json())

    res=requests.get(url).json()



    if "results" in res:

        lat=res["results"][0]["latitude"]
        long=res["results"][0]["longitude"]
        return lat,long
    else: 
        return None,None


def get_weather(lat,long):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
    response = requests.get(url).json()
    return response["current_weather"]

            

st.title("Weather Application")


city=st.text_input("Enter the city name ")

if st.button("Get weather"):

    if city : 

        lat ,long= get_cordinates(city)


        if lat:

            weather=get_weather(lat,long)

            st.success(f"Weather in {city}")
            st.write(f"🌡 Temperature: **{weather['temperature']}°C**")
            st.write(f"💨 Wind Speed: **{weather['windspeed']} km/h**")
            st.write(f"📍 Wind Direction: **{weather['winddirection']}°**")
            st.write(f"⌚ Time: **{weather['time']}**")

        else :
           st.error(f"{city} doest found ")    

    else :
         st.write("Please enter the city ") 