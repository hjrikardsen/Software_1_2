biological_gender = input("Enter biological gender (male/female): ")
hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

if biological_gender.lower() == "male":
    if hemoglobin_value > 167:
        print("Your hemoglobin is high.")
    elif hemoglobin_value >= 134:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is low.")

elif biological_gender.lower() == "female":
    if hemoglobin_value > 155:
        print("Your hemoglobin is high.")
    elif hemoglobin_value >= 117:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is low.")
else:
    print("Invalid gender.")