import streamlit as st
import requests
st.title("🌧️My Whether App")

city_name=[
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow","Kanpur", 
    "Nagpur", "Indore", "Thane", "Bhopal","Visakhapatnam",  "Patna",
    "Pimpri-Chinchwad","Vadodara", "Ghaziabad","Ludhiana", "Agra", 
    "Nashik", "Faridabad", "Meerut","Rajkot", "Kalyan-Dombivli", 
    "Vasai-Virar", "Varanasi", "Srinagar","Aurangabad", "Dhanbad", 
    "Amritsar", "Allahabad", "Ranchi","Howrah", "Coimbatore", "Jabalpur",
    "Gwalior", "Vijayawada","Jodhpur", "Madurai", "Raipur", "Kota", "Guwahati",
    "Chandigarh", "Solapur", "Hubli-Dharwad", "Bareilly", "Moradabad",
    "Mysuru", "Gurgaon", "Aligarh", "Jalandhar", "Tiruchirappalli",
    "Bhubaneswar", "Salem", "Tiruppur", "Bhiwandi", "Amravati",
    "Noida", "Cuttack", "Kochi", "Thiruvananthapuram", "Guntur",
    "Bikaner", "Saharanpur", "Gorakhpur","Mohali","Bhabua","Mohania",
]


API_key = "0eaab23d0899337fc4f022e1dec8926b"

choice = st.selectbox("Choose your city name" ,city_name) 

if choice:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={choice}&appid={API_key}"
    
    responce = requests.get(url)
    
    if responce.status_code == 200:
        st.write("API Working")
    
        # st.json(responce.json())
    
        whether_info = responce.json()
        
        # col1, col2 = st.columns
        st.json(whether_info)
        
    else:
        st.write("something went wrong")
        
    
    st.write(f"{responce}")