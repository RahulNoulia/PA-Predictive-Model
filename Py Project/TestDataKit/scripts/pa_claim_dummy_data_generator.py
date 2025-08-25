import pandas as pd
import random
from faker import Faker


def generate_dummy_ncpdp_data(num_records: int = 20000, output_file: str = "ncpdp_dummy_data.csv"):
    """
    Generate synthetic NCPDP-style pharmacy claim dataset for PA prediction model training.

    Args:
        num_records (int): Number of records to generate.
        output_file (str): Path to save CSV file.

    Returns:
        pd.DataFrame: Generated dataset.
    """
    fake = Faker()

    # Sample lookup values
    ndc_codes = ["0002-8215-01", "0009-5178-19", "0015-4500-11", "0045-1234-22"]
    drug_names = ["Atorvastatin", "Metformin", "Adalimumab", "Trastuzumab"]
    drug_classes = ["Statin", "Antidiabetic", "Immunosuppressant", "Oncology"]
    reject_codes = ["00", "75", "76", "79", "88"]  # 75/76 = PA required
    diagnosis_codes = ["E11.9", "I10", "C50.9", "M06.9"]
    specialties = ["Oncologist", "Cardiologist", "Endocrinologist", "General Practitioner"]
    daw_codes = ["0", "1", "2", "3", "4", "5", "6"]  # Dispense as written etc.
    scc_pool = ["AB", "CD", "EF", "GH", "IJ"]  # Submission Clarification Codes (example)
    bins = ["610011", "004336", "011155", "006378", "004583", "009845"]
    pcns = ["PCN1", "PCN2", "PCN3", "PCN-A", "PCN-B"]

    records = []

    for i in range(num_records):
        patient_id = f"{random.randint(100000, 9999999)}"
        dob = fake.date_of_birth(minimum_age=1, maximum_age=90)
        gender = random.choice(["M", "F"])
        cardholder_id = f"ST:{random.randint(10000, 99999)}"
        payer_id = f"{random.randint(100, 999)}"
        bin_number = random.choice(bins)
        pcn = random.choice(pcns)
        group_id = f"ST:{random.randint(1000, 9999)}"
        person_code = random.choice(["01", "02", "03"])  # person code on card

        prescriber_id = f"{random.randint(1000, 9999)}"
        prescriber_specialty = random.choice(specialties)
        pharmacy_id = f"{random.randint(1000, 9999)}"

        ndc = random.choice(ndc_codes)
        drug = random.choice(drug_names)
        drug_class = random.choice(drug_classes)
        strength = f"{random.choice([10, 20, 40, 100])}mg"
        quantity = random.randint(10, 90)
        days_supply = random.choice([7, 14, 30, 60, 90])
        refills = random.randint(0, 5)
        diagnosis = random.choice(diagnosis_codes)

        # DAW and SCC
        daw = random.choice(daw_codes)
        # choose 0-2 SCC codes and join
        scc = ",".join(random.sample(scc_pool, k=random.choice([0, 1, 2])))


        reject_code = random.choice(reject_codes)
        if reject_code in ["75", "76"]:
            response_status = "Reject"
            pa_required = "Yes"
        elif reject_code == "00":
            response_status = "Approve"
            pa_required = "No"
        else:
            response_status = "Reject"
            pa_required = "No"

        records.append({
            "Patient_ID": patient_id,
            "DateOfBirth": dob,
            "Gender": gender,
            "Cardholder_ID": cardholder_id,
            "Payer_ID": payer_id,
            "Submission_Clarification_Code":scc,
            "Daw_Code": daw,
            "BIN": bin_number,
            "PCN": pcn,
            "Group_ID": group_id,
            "Person_Code": person_code,
            "Prescriber_ID": prescriber_id,
            "Prescriber_Specialty": prescriber_specialty,
            "Pharmacy_ID": pharmacy_id,
            "NDC_Code": ndc,
            "Drug_Name": drug,
            "Drug_Class": drug_class,
            "Strength": strength,
            "Quantity": quantity,
            "Days_Supply": days_supply,
            "Refills": refills,
            "Diagnosis_Code": diagnosis,
            "RejectCode": reject_code,
            "ResponseStatus": response_status,
            "PA_Required": pa_required
        })

    df = pd.DataFrame(records)
    df.to_csv(output_file, index=False)

    print(f"✅ Dummy dataset generated: {output_file} ({num_records} records)")
    return df
