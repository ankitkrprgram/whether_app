import streamlit as st
import requests
from datetime import datetime

# App Configuration
st.set_page_config(page_title="Weather Forecast", page_icon="🌤️")

# CSS for styling
st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .metric-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .weather-icon {
        font-size: 50px;
        text-align: center;
    }
    .city-header {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🌤️ Weather Forecast App")
st.markdown("Get real-time weather information for cities across India")

# City selection
city_name = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Kanpur", 
    "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna",
    "Pimpri-Chinchwad", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", 
    "Nashik", "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", 
    "Vasai-Virar", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", 
    "Amritsar", "Allahabad", "Ranchi", "Howrah", "Coimbatore", "Jabalpur",
    "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Guwahati",
    "Chandigarh", "Solapur", "Hubli-Dharwad", "Bareilly", "Moradabad",
    "Mysuru", "Gurgaon", "Aligarh", "Jalandhar", "Tiruchirappalli",
    "Bhubaneswar", "Salem", "Tiruppur", "Bhiwandi", "Amravati",
    "Noida", "Cuttack", "Kochi", "Thiruvananthapuram", "Guntur",
    "Bikaner", "Saharanpur", "Gorakhpur", "Mohali", "Bhabua", "Mohania",
]

API_key = "0eaab23d0899337fc4f022e1dec8926b"

# Sidebar for city selection
with st.sidebar:
    st.header("Settings")
    choice = st.selectbox("Select a city", city_name)
    st.markdown("---")
     # st.markdown("**Weather Data Source:** OpenWeatherMap API")
    st.markdown("**Note:** Updates in real-time when city changes")

# Weather icons mapping
weather_icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "💨",
    "Haze": "🌫️",
    "Dust": "💨",
    "Fog": "🌁",
    "Sand": "💨",
    "Ash": "💨",
    "Squall": "🌬️",
    "Tornado": "🌪️"
}

if choice:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={choice}&appid={API_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_info = response.json()
        
        # Main weather display
        st.markdown(f"## <div class='city-header'>{choice}</div>", unsafe_allow_html=True)
        
        # Current date and time
        current_time = datetime.fromtimestamp(weather_info['dt']).strftime('%A, %B %d, %Y %I:%M %p')
        st.caption(f"Last updated: {current_time}")
        
        # Weather icon and main info
        weather_main = weather_info['weather'][0]['main']
        icon = weather_icons.get(weather_main, "🌤️")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"<div class='weather-icon'>{icon}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center;'>{weather_info['weather'][0]['description'].title()}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<div class='big-font'>{weather_info['main']['temp']:.1f}°C</div>", unsafe_allow_html=True)
            st.write(f"Feels like: {weather_info['main']['feels_like']:.1f}°C")
        
        # Weather metrics in columns
        col3, col4, col5 = st.columns(3)
        
        with col3:
            with st.container():
                st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
                st.metric("Humidity", f"{weather_info['main']['humidity']}%")
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col4:
            with st.container():
                st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
                st.metric("Wind Speed", f"{weather_info['wind']['speed']} m/s")
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col5:
            with st.container():
                st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
                st.metric("Pressure", f"{weather_info['main']['pressure']} hPa")
                st.markdown("</div>", unsafe_allow_html=True)
        
        # Additional weather details
        with st.expander("More Weather Details"):
            col6, col7 = st.columns(2)
            with col6:
                st.write(f"**Min Temperature:** {weather_info['main']['temp_min']}°C")
                st.write(f"**Max Temperature:** {weather_info['main']['temp_max']}°C")
                st.write(f"**Visibility:** {weather_info.get('visibility', 'N/A')} meters")
            
            with col7:
                st.write(f"**Sunrise:** {datetime.fromtimestamp(weather_info['sys']['sunrise']).strftime('%I:%M %p')}")
                st.write(f"**Sunset:** {datetime.fromtimestamp(weather_info['sys']['sunset']).strftime('%I:%M %p')}")
                if 'rain' in weather_info:
                    st.write(f"**Rain (1h):** {weather_info['rain'].get('1h', 'N/A')} mm")
        
        # Raw data (hidden by default)
        with st.expander("View Raw API Data"):
            st.json(weather_info)
        
    else:
        st.error("Failed to fetch weather data. Please try again later.")
        st.write(f"API Response Code: {response.status_code}")