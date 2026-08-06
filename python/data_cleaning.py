import pandas as pd


# Load raw dataset
input_file = "../data/raw/healthcare_data.csv"

df = pd.read_csv(input_file)


# Convert date columns
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])


# Create Length of Stay feature
df["Length_of_Stay"] = (
    df["Discharge Date"] - df["Date of Admission"]
).dt.days


# Remove unnecessary columns
df = df.drop(columns=["Name", "Room Number"])


# Save cleaned dataset
output_file = "../data/processed/healthcare_data_cleaned.csv"

df.to_csv(output_file, index=False)


print("Data cleaning completed successfully!")
print(f"Cleaned dataset saved at: {output_file}")