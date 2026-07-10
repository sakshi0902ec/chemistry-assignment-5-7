def plastic_identifier():
    # Database containing data for standard SPI codes 1 to 7
    recycling_codes = {
        1: {
            "name": "PETE or PET (Polyethylene Terephthalate)",
            "products": "Water bottles, soft drink bottles, juice containers, salad dressing jars.",
            "recyclability": "Widely Recyclable (Most commonly accepted plastic).",
            "remarks": "Safe for single-use. Can leach antimony if reused or exposed to high heat over time."
        },
        2: {
            "name": "HDPE (High-Density Polyethylene)",
            "products": "Milk jugs, detergent bottles, shampoo bottles, grocery bags, toys.",
            "recyclability": "Widely Recyclable (Highly accepted).",
            "remarks": "Very safe plastic; low risk of chemical leaching. Extremely durable."
        },
        3: {
            "name": "PVC (Polyvinyl Chloride)",
            "products": "Plumbing pipes, cable insulation, credit cards, medical tubing, vinyl flooring.",
            "recyclability": "Rarely Recyclable (Difficult to process commercially).",
            "remarks": "Contains toxic chemicals (phthalates, dioxins) dangerous throughout its lifecycle. Hazardous to burn."
        },
        4: {
            "name": "LDPE (Low-Density Polyethylene)",
            "products": "Squeeze bottles, cling wraps, sandwich bags, bubble wrap, flexible container lids.",
            "recyclability": "Sometimes Recyclable (Check local programs; plastic films jam sorting machines).",
            "remarks": "Relatively safe for reuse, durable, and chemically inert."
        },
        5: {
            "name": "PP (Polypropylene)",
            "products": "Yogurt containers, syrup bottles, medicine bottles, tupperware, car bumpers.",
            "recyclability": "Increasingly Recyclable (Gradually accepted by more municipalities).",
            "remarks": "High melting point makes it excellent for hot-liquid containers and dishwasher-safe items."
        },
        6: {
            "name": "PS (Polystyrene / Styrofoam)",
            "products": "Disposable coffee cups, take-out clam shells, plastic cutlery, packing peanuts.",
            "recyclability": "Rarely Recyclable (Bulky, structurally weak, economically non-viable).",
            "remarks": "Can leach styrene (a suspected carcinogen), structurally breaks down easily into microplastics."
        },
        7: {
            "name": "OTHER (Acrylic, Polycarbonate, Nylon, Fiberglass, Polylactic Acid)",
            "products": "Baby bottles (older polycarbonate ones), sunglasses, compact discs, 3D printer filaments.",
            "recyclability": "Virtually Non-Recyclable (A catch-all mix of miscellaneous or layered resins).",
            "remarks": "Polycarbonate variants can leach Bisphenol A (BPA), an endocrine disruptor. Bio-plastics like PLA also fall here."
        }
    }

    print("--- Plastic Identification System Using Recycling Codes ---")
    print("Select a Resin Identification Code from the options below:")
    for code in recycling_codes:
        print(f"[{code}] Code {code}")
    
    try:
        choice = int(input("\nEnter code number (1-7): "))
        
        if choice in recycling_codes:
            plastic = recycling_codes[choice]
            print(f"\n================= CODE {choice} INFORMATION =================")
            print(f"• Polymer Name:         {plastic['name']}")
            print(f"• Common Products:      {plastic['products']}")
            print(f"• Recyclability:        {plastic['recyclability']}")
            print(f"• Environmental Remarks: {plastic['remarks']}")
            print("==========================================================")
        else:
            print("Invalid Selection! Please enter a number between 1 and 7.")
            
    except ValueError:
        print("Invalid Input! Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    plastic_identifier()