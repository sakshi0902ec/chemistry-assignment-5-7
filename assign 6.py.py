def corrosion_risk_assessment():
    print("--- Simple Corrosion Risk Assessment Program ---")
    
    try:
        # Accepting environmental parameters
        rh = float(input("Enter Relative Humidity (%): "))
        temp = float(input("Enter Temperature (°C): "))
        ph = float(input("Enter pH level (0-14): "))
        salt = input("Is salt present? (Yes/No): ").strip().lower()
        
        # Logical Conditions for Classification
        # High Risk Conditions: Acidic environment, high salt + moisture, or extreme humidity/temp combination
        if (ph < 4.5) or (salt == 'yes' and rh > 50) or (rh > 80 and temp > 30):
            risk = "HIGH"
            reason = "Highly acidic environment, high moisture with salinity, or extreme heat & humidity."
            
        # Moderate Risk Conditions: Mildly acidic/basic, intermediate humidity or mild warmth
        elif (4.5 <= ph <= 5.5) or (8.5 <= ph <= 10.0) or (50 <= rh <= 80) or (temp > 20 and salt == 'yes'):
            risk = "MODERATE"
            reason = "Mild pH levels, moderate humidity levels, or presence of salt at lower temperatures."
            
        # Low Risk Conditions: Neutral pH, low moisture, cool environment, dry conditions
        else:
            risk = "LOW"
            reason = "Optimal neutral pH environment with low humidity and no catalytic corrosive agents."
            
        print("\n--- Assessment Results ---")
        print(f"Corrosion Risk Level: {risk}")
        print(f"Reasoning: {reason}")
        
    except ValueError:
        print("Invalid input! Please enter numerical values for Humidity, Temperature, and pH.")

# Run the program
if __name__ == "__main__":
    corrosion_risk_assessment()