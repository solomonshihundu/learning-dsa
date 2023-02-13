import pandas as pd
import numpy as np
import os.path

# Set the number of records you want to generate
num_records = 10000

#Where to save the generated data
save_path = 'D:\Shihundu\Personal\Data'


# Generate random data for the features
age = np.random.randint(18, 80, size=num_records)
income = np.random.randint(20, 100, size=num_records) * 1000
gender = np.random.choice(["Male", "Female"], size=num_records)

# Generate random data for the target
target = np.random.randint(0, 2, size=num_records)

# Create a pandas dataframe to store the data
data = pd.DataFrame({
    "Age": age,
    "Income": income,
    "Gender": gender,
    "Target": target
})

# Save the data to a CSV file
data.to_csv(save_path+"\data.csv", index=False)

