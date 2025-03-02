import streamlit as st

st.title("Unit Converter")
st.markdown("Convert Length, Weight, Temperature and Time Instantly!")

# Input for value
value = st.number_input("Enter value to convert:")

# Select unit type (Length, Wight, Temperature and Time)
unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Time"])

# Function to convert units
def convert_unit(value, from_unit, to_unit, unit_type):
    #Length conversion
    if unit_type == "Length":
       if from_unit == "Kilometer" and to_unit == "Meter":
           return value * 1000
       elif from_unit == "Meter" and to_unit == "Kilometer":
           return value / 1000
       elif from_unit == "Kilometer" and to_unit == "Centimeter":
           return value * 100000
       elif from_unit == "Centimeter" and to_unit == "Kilometer":
           return value / 100000
       elif from_unit == "Meter" and to_unit == "Centimeter":
           return value * 100
       elif from_unit == "Centimeter" and to_unit == "Meter":
           return value / 100
       elif from_unit == "Mile" and to_unit == "Meter":
           return value * 1609.34
       elif from_unit == "Meter" and to_unit == "Mile":
           return value / 1609.34
       elif from_unit == "Mile" and to_unit == "Kilometer":
           return value * 1.60934
       elif from_unit == "Kilometer" and to_unit == "Mile":
           return value / 1.60934
       elif from_unit == "Yard" and to_unit == "Meter":
           return value * 0.9144
       elif from_unit == "Meter" and to_unit == "Yard":
           return value / 0.9144
       elif from_unit == "Foot" and to_unit == "Meter":
           return value * 0.3048
       elif from_unit == "Meter" and to_unit == "Foot":
           return value / 0.3048
       elif from_unit == "Inch" and to_unit == "Meter":
           return value * 0.0254
       elif from_unit == "Meter" and to_unit == "Inch":
           return value / 0.0254
       elif from_unit == "Yard" and to_unit == "Foot":
           return value * 3
       elif from_unit == "Foot" and to_unit == "Yard":
           return value / 3
       elif from_unit == "Foot" and to_unit == "Inch":
           return value * 12
       elif from_unit == "Inch" and to_unit == "Foot":
           return value / 12
       elif from_unit == "Yard" and to_unit == "Inch":
           return value * 36
       elif from_unit == "Inch" and to_unit == "Yard":
           return value / 36
       
    # Weight Conversion
    elif unit_type == "Weight":
        if from_unit == "Kilogram" and to_unit == "Gram":
            return value * 1000
        elif from_unit == "Gram" and to_unit == "Kilogram":
            return value / 1000
        elif from_unit == "Kilogram" and to_unit == "Milligram":
            return value * 1000000
        elif from_unit == "Milligram" and to_unit == "Kilogram":
            return value / 1000000
        elif from_unit == "Gram" and to_unit == "Milligram":
            return value * 1000
        elif from_unit == "Milligram" and to_unit == "Gram":
            return value / 1000
        
    # Temperature Conversion
    elif unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        
    # Time Conversion
    elif unit_type == "Time":
        if from_unit == "Minutes" and to_unit == "Seconds":
            return value * 60
        elif from_unit == "Seconds" and to_unit == "Minutes":
            return value / 60
        elif from_unit == "Hours" and to_unit == "Minutes":
            return value * 60
        elif  from_unit == "Minutes" and to_unit == "Hours":
            return value / 60
        elif from_unit == "Hours" and to_unit == "Seconds":
            return value * 3600
        elif  from_unit == "Seconds" and to_unit == "Hours":
            return value / 3600
        
    # If no conversion found
    else:
        return "Conversion not supported"
    
# Select units based on unit type
if unit_type == "Length":
    from_unit = st.selectbox("From Unit", ["Kilometer", "Meter", "Centimeter", "Mile", "Yard", "Foot", "Inch"])
    to_unit = st.selectbox("To Unit", ["Kilometer", "Meter", "Centimeter", "Mile", "Yard", "Foot", "Inch"])
elif unit_type == "Weight":
    from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram"])
    to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram"])
elif unit_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
elif unit_type == "Time":
    from_unit = st.selectbox("From Unit", ["Seconds", "Minutes", "Hours"])
    to_unit = st.selectbox("To Unit", ["Seconds", "Minutes", "Hours"])

# Button to calculate conversion
if st.button("Convert"):
    result = convert_unit(value, from_unit, to_unit, unit_type)
    st.write(f"Converted Value: {result} {to_unit}")