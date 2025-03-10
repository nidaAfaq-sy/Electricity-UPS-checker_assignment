# Electricity and UPS Assignment

# Checker electricity availability
import streamlit as st
import time
from datetime import datetime
import random  # For demo purposes only

def check_power_status():
    # In a real implementation, you would interface with actual hardware
    # This is just a simulation
    return random.choice(['Main Power', 'UPS Power'])

def check_ups_battery():
    # Simulate UPS battery percentage
    return random.randint(0, 100)

def main():
    st.title("Electricity and UPS Status Checker")
    
    # Add a sidebar
    st.sidebar.header("System Information")
    last_check = st.sidebar.empty()
    
    # Main content
    status_container = st.empty()
    battery_container = st.empty()
    
    # Add a check interval selector
    check_interval = st.slider("Check interval (seconds)", 1, 30, 5)
    
    if st.button("Start Monitoring"):
        while True:
            # Get current power status
            power_status = check_power_status()
            battery_level = check_ups_battery()
            
            # Update timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            last_check.text(f"Last checked: {current_time}")
            
            # Display status with appropriate color
            if power_status == "Main Power":
                status_container.success(f"Current Power Source: {power_status}")
            else:
                status_container.warning(f"Current Power Source: {power_status}")
            
            # Display battery level with progress bar
            battery_container.text("UPS Battery Level:")
            battery_container.progress(battery_level / 100)
            
            # Add battery percentage text
            if battery_level < 20:
                battery_container.error(f"Battery Level: {battery_level}%")
            elif battery_level < 50:
                battery_container.warning(f"Battery Level: {battery_level}%")
            else:
                battery_container.info(f"Battery Level: {battery_level}%")
            
            time.sleep(check_interval)

if __name__ == "__main__":
    main() 



