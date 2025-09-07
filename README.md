# PA-Predictive-Model

<h3 align='center'>  🔥 End-to-End Approach for Prior Authorization (PA) Detection using ML </h3>

<h3 align='center'>  1. Problem Understanding </h3>

Healthcare payers often reject claims with codes 75 (Prior Authorization Required) or 76 (Prior Authorization Not Obtained).

Goal → Build a model that can predict upfront whether a prescription claim will require PA before submitting to payer.

Benefit →

Reduce payer rejections.

Save prescriber/pharmacy time.

Improve patient care by avoiding delays.

<h3 align='center'>  2. Data Sources </h3>

We will use historical NCPDP pharmacy claim transactions (request + response).
From these, we will extract features like:

Patient demographics: Age (from DOB), Gender.

Insurance/Plan info: BIN, PCN, Group ID, Person Code.

Prescriber: Prescriber specialty.

Drug/Clinical info: NDC, Drug name, Drug class, Strength, Quantity, Days supply, Refills, Diagnosis code (ICD).

Claim adjudication: Reject code, Response status.

Target variable: PA_Required (derived from reject codes 75/76).

<h3 align='center'>  3. Feature Engineering </h3>

Derive Age from DateOfBirth.

Map NDC → Drug name → Drug class consistently.

Align Diagnosis codes with drug classes (e.g., Metformin ↔ Diabetes ICD).

Encode categorical fields (e.g., Gender, DAW, Specialty).

Normalize numerical features (e.g., Quantity, Days supply).

<h3 align='center'>  4. Business Rule Layer vs ML Model </h3>

Business Rules Layer (optional): deterministic checks (e.g., if RejectCode=75 → PA=Yes).

ML Model: learns hidden patterns (drug class + specialty + diagnosis + plan + DAW → PA).

Hybrid approach works best, but ML alone can also be used.

<h3 align='center'>  5. Dataset Preparation </h3>

Dummy synthetic dataset created (using Faker + mappings) when real data unavailable.

<h3 align='center'>  Final dataset schema (columns): </h3>

Feature	Description : - 
Patient_ID	Unique patient identifier
DateOfBirth	Patient DOB (used for Age)
Gender	M/F
Cardholder_ID, Payer_ID	Insurance identifiers
BIN, PCN, Group_ID, Person_Code	Plan routing fields
Prescriber_ID, Prescriber_Specialty	Prescriber info
Pharmacy_ID	Pharmacy identifier
NDC_Code, Drug_Name, Drug_Class, Strength	Drug info
Quantity, Days_Supply, Refills	Prescription details
Diagnosis_Code	Clinical ICD code
Daw_Code, Submission_Clarification_Code	Claim submission details
RejectCode, ResponseStatus	Claim outcome
PA_Required	Target label (Yes/No)

📊 NCPDP → Feature Mapping for PA Detection			


<img width="785" height="722" alt="image" src="https://github.com/user-attachments/assets/8bbf3555-5b13-4a06-84ad-4193f3a4c11f" />
