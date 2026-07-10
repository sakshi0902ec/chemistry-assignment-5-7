def periodic_element_info():
    # Database containing info for requested elements
    element_db = {
        "Na": {
            "name": "Sodium", "atomic_number": 11, "atomic_mass": "22.99 u", 
            "group": 1, "period": 3, "config": "[Ne] 3s1", "oxidation": "+1",
            "application": "Used as a coolant in nuclear reactors and in manufacturing sodium vapor lamps."
        },
        "Fe": {
            "name": "Iron", "atomic_number": 26, "atomic_mass": "55.85 u", 
            "group": 8, "period": 4, "config": "[Ar] 3d6 4s2", "oxidation": "+2, +3",
            "application": "Primary structural material in engineering (steel fabrication, bridges, machinery)."
        },
        "Cl": {
            "name": "Chlorine", "atomic_number": 17, "atomic_mass": "35.45 u", 
            "group": 17, "period": 3, "config": "[Ne] 3s2 3p5", "oxidation": "-1",
            "application": "Extensively used in water purification, sewage treatment, and bleaching agents."
        },
        "Cu": {
            "name": "Copper", "atomic_number": 29, "atomic_mass": "63.55 u", 
            "group": 11, "period": 4, "config": "[Ar] 3d10 4s1", "oxidation": "+1, +2",
            "application": "Widely used in electrical wiring, heat exchangers, and integrated circuits due to high conductivity."
        }
    }

    print("--- Interactive Periodic Element Information Program ---")
    symbol = input("Enter the chemical symbol of an element (e.g., Na, Fe, Cl, Cu): ").strip()
    
    # Format input to match PascalCase/CamelCase style of elements (e.g., na -> Na)
    symbol = symbol.capitalize()

    if symbol in element_db:
        el = element_db[symbol]
        print(f"\nProperties of {el['name']} ({symbol}):")
        print(f"  • Atomic Number: {el['atomic_number']}")
        print(f"  • Atomic Mass: {el['atomic_mass']}")
        print(f"  • Group: {el['group']}")
        print(f"  • Period: {el['period']}")
        print(f"  • Electronic Configuration: {el['config']}")
        print(f"  • Common Oxidation State: {el['oxidation']}")
        print(f"  • Engineering Application: {el['application']}")
    else:
        print("\nElement not found in current database. Please try Na, Fe, Cl, or Cu.")

# Run the program
if __name__ == "__main__":
    periodic_element_info()