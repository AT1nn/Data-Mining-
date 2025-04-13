import pandas as pd
from faker import Faker
import random
import numpy as np
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate 10,000 records
records = []
for _ in range(10000):
    age = random.randint(1, 90)

    # 1. Age & Life Stage
    if age < 13:
        age_group = 'child'
        hormonal_stage = 'pre-puberty'
    elif age < 20:
        age_group = 'teen'
        hormonal_stage = random.choice(['puberty', 'post-puberty'])
    elif age < 65:
        age_group = 'adult'
        hormonal_stage = random.choice(['none', 'menstrual cycle', 'pregnancy', 'post-pregnancy'] if
                                       random.choice([True, False]) else ['none'])
    else:
        age_group = 'senior'
        hormonal_stage = random.choice(['menopause', 'andropause', 'none'])

    # 2. Diet & Nutritional Factors
    sugar_intake = round(random.uniform(0.5, 8), 1)
    acidic_food = round(random.uniform(0, 10), 1)
    calcium_level = round(random.uniform(2, 15), 1)  # mg/dL
    processed_food = random.choice(['low', 'medium', 'high'])
    fluoridated_water = random.choice([True, False])

    # 3. Oral Hygiene Behavior
    brushing_freq = random.randint(0, 3)
    brushing_duration = random.randint(30, 180) if brushing_freq > 0 else 0
    brushing_tech = random.choice(['Bass method', 'circular', 'horizontal scrub', 'none'])
    flossing_freq = random.randint(0, 7)
    mouthwash_use = random.choice([True, False])
    tongue_cleaning = random.choice([True, False])
    toothbrush_type = random.choice(['manual-soft', 'manual-medium', 'manual-hard', 'electric'])

    # 4. Smoking & Substance Use
    smoking_status = random.choices(
        ['current', 'former', 'never'],
        weights=[0.2, 0.3, 0.5]
    )[0]

    pack_years = round(random.uniform(0, 50), 1) if smoking_status in ['current', 'former'] else 0
    vaping_freq = random.choice(['never', 'occasional', 'daily']) if smoking_status != 'never' else 'never'
    alcohol_consumption = random.randint(0, 21)
    betel_nut_use = random.choices([True, False], weights=[0.1, 0.9])[0]

    # 5. Previous Dental Issues & Medical History
    cavities = random.randint(0, 20)
    gum_disease = random.choices(
        ['none', 'gingivitis', 'periodontitis'],
        weights=[0.6, 0.3, 0.1]
    )[0]
    tooth_loss = random.randint(0, 32)
    root_canals = random.randint(0, 10)
    bruxism = random.choices(
        ['none', 'mild', 'moderate', 'severe'],
        weights=[0.7, 0.15, 0.1, 0.05]
    )[0]
    dry_mouth = random.choices(
        ['none', 'occasional', 'frequent'],
        weights=[0.6, 0.3, 0.1]
    )[0]
    diabetes = random.choices(
        ['none', 'prediabetes', 'type 1', 'type 2'],
        weights=[0.8, 0.1, 0.05, 0.05]
    )[0]
    autoimmune = random.choice([True, False])

    # 6. Advanced Biomarkers & Genetic Factors
    salivary_ph = round(random.uniform(5.5, 7.5), 1)
    s_mutans = round(random.uniform(0, 1e6), 0)  # CFU/mL
    p_gingivalis = round(random.uniform(0, 1e5), 0)  # CFU/mL
    genetic_risk = random.randint(1, 10)

    # 7. Behavioral & Socioeconomic Factors
    dental_visits = random.randint(0, 4)
    last_checkup = random.randint(0, 60)  # months
    insurance = random.choice([True, False])
    stress_level = random.randint(1, 10)
    education = random.choice([
        'less than high school',
        'high school',
        'college',
        'graduate degree'
    ])

    # 8. Environmental & Lifestyle Factors
    occupation = fake.job()
    medication = random.choice([True, False])

    record = {
        # 1. Age & Life Stage
        'Chronological_Age': age,
        'Age_Group': age_group,
        'Hormonal_Stage': hormonal_stage,

        # 2. Diet & Nutritional Factors
        'Sugar_Intake_Frequency': sugar_intake,
        'Acidic_Food_Consumption': acidic_food,
        'Calcium_VitaminD_Level': calcium_level,
        'Processed_Food_Intake': processed_food,
        'Water_Fluoridation': fluoridated_water,

        # 3. Oral Hygiene Behavior
        'Brushing_Frequency': brushing_freq,
        'Brushing_Duration': brushing_duration,
        'Brushing_Technique': brushing_tech,
        'Flossing_Frequency': flossing_freq,
        'Mouthwash_Use': mouthwash_use,
        'Tongue_Cleaning': tongue_cleaning,
        'Toothbrush_Type': toothbrush_type,

        # 4. Smoking & Substance Use
        'Smoking_Status': smoking_status,
        'Pack_Years': pack_years,
        'Vaping_Frequency': vaping_freq,
        'Alcohol_Consumption': alcohol_consumption,
        'Betel_Nut_Use': betel_nut_use,

        # 5. Previous Dental Issues & Medical History
        'Cavities_Count': cavities,
        'Gum_Disease_Status': gum_disease,
        'Tooth_Loss_Count': tooth_loss,
        'RootCanals_Fillings_Count': root_canals,
        'Bruxism_Status': bruxism,
        'Dry_Mouth_Frequency': dry_mouth,
        'Diabetes_Status': diabetes,
        'Autoimmune_Condition': autoimmune,

        # 6. Advanced Biomarkers & Genetic Factors
        'Salivary_pH': salivary_ph,
        'S_mutans_Level': s_mutans,
        'P_gingivalis_Level': p_gingivalis,
        'Genetic_Risk_Score': genetic_risk,

        # 7. Behavioral & Socioeconomic Factors
        'Dental_Visit_Frequency': dental_visits,
        'Last_Dental_Checkup': last_checkup,
        'Dental_Insurance': insurance,
        'Stress_Level': stress_level,
        'Education_Level': education,

        # 8. Environmental & Lifestyle Factors
        'Occupation': occupation,
        'Medication_Use': medication
    }

    records.append(record)

# Create DataFrame
df = pd.DataFrame(records)

# Save to Excel
excel_filename = "comprehensive_dental_health_dataset.xlsx"
df.to_excel(excel_filename, index=False, sheet_name="Dental Health Data")

print(f"✅ Successfully generated and saved {len(df)} records to '{excel_filename}'")
print(f"Dataset dimensions: {df.shape[0]} rows × {df.shape[1]} columns")
