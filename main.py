import csv

def calculate_com():
    """Calculate Monthly Operational Cost (COM) from MONTHLY.csv"""
    com = 0
    with open('MONTHLY.csv', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(' | ')
            if len(parts) == 2:
                cost_str = parts[1].replace('$', '').replace('.', '').strip()
                try:
                    com += int(cost_str)
                except ValueError:
                    print(f"Warning: Could not parse cost '{cost_str}'")
    return com

def calculate_tpp():
    """Calculate Total Project Points (TPP) from HU.csv"""
    tpp = 0
    with open('HU.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader, None)  # Skip header if exists
        for row in reader:
            if len(row) >= 5:
                try:
                    esfuerzo = int(row[4].strip())
                    tpp += esfuerzo
                except ValueError:
                    print(f"Warning: Could not parse effort '{row[4]}' in row {row}")
    return tpp

def main():
    # Constants
    V = 16  # Velocity: points per sprint
    sprint_days = 15  # Days per sprint

    # Calculations
    COM = calculate_com()
    TPP = calculate_tpp()
    CEPHU = COM / V if V != 0 else 0
    CEP = TPP * CEPHU
    total_days = (TPP / V) * sprint_days if V != 0 else 0

    # Output results
    print("=== Project Cost Calculation ===")
    print(f"Total Project Points (TPP): {TPP}")
    print(f"Monthly Operational Cost (COM): ${COM:,}")
    print(f"Sprint Velocity (V): {V} points/sprint")
    print(f"Cost per Effort Hour Unit (CEPHU): ${CEPHU:,.2f}")
    print(f"Total Project Cost (CEP): ${CEP:,.2f}")
    print(f"Total Time Required: {total_days:.2f} days")

if __name__ == "__main__":
    main()