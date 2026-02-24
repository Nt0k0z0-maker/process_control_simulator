"""
PROCESS CONTROL SYSTEM SIMULATOR

This script simulates an industrial process control system.
It monitors:
- Temperature
- Pressure
- Flow rate
"""

import random

print("=== PROCESS CONTROL SYSTEM SIMULATOR ===")

# Simulated sensor readings (like real industrial sensors)
temperature = random.randint(30, 120)  # °C
pressure = random.randint(1, 10)       # Bar
flow_rate = random.randint(50, 200)    # L/min

print(f"\nTemperature Sensor Reading: {temperature} °C")
print(f"Pressure Sensor Reading: {pressure} Bar")
print(f"Flow Rate Sensor Reading: {flow_rate} L/min")

# Control Logic (like PLC decision making)
if temperature > 100:
    print("\nALERT: High Temperature!")
    print("Action: Activate cooling system")

if pressure > 8:
    print("\nALERT: High Pressure!")
    print("Action: Open pressure relief valve")

if flow_rate < 80:
    print("\nWARNING: Low Flow Rate!")
    print("Action: Check pump or pipeline")

if temperature <= 100 and pressure <= 8 and flow_rate >= 80:
    print("\nSystem Status: STABLE")
    print("All process parameters within safe operating range.")
