# PA-Predictive-Model

<h3 align='center'>  🔥 End-to-End Approach for Prior Authorization (PA) Detection using ML </h3>

<h3 align='center'>  1. Problem Understanding </h3>

- &nbsp; Healthcare payers often reject claims with codes 75 (Prior Authorization Required) or 76 (Prior Authorization Not Obtained).

- &nbsp; Goal → Build a model that can predict upfront whether a prescription claim will require PA before submitting to payer.

- &nbsp; Benefit →

- &nbsp; Reduce payer rejections.

- &nbsp; Save prescriber/pharmacy time.

- &nbsp; Improve patient care by avoiding delays.

<h3 align='center'>  2. Data Sources </h3>

- &nbsp; We will use historical NCPDP pharmacy claim transactions (request + response).
From these, we will extract features like:

- &nbsp; Patient demographics: Age (from DOB), Gender.

- &nbsp; Insurance/Plan info: BIN, PCN, Group ID, Person Code.

- &nbsp; Prescriber: Prescriber specialty.

- &nbsp; Drug/Clinical info: NDC, Drug name, Drug class, Strength, Quantity, Days supply, Refills, Diagnosis code (ICD).

- &nbsp; Claim adjudication: Reject code, Response status.

- &nbsp; Target variable: PA_Required (derived from reject codes 75/76).

<h3 align='center'>  3. Feature Engineering </h3>

- &nbsp; Derive Age from DateOfBirth.

- &nbsp; Map NDC → Drug name → Drug class consistently.

- &nbsp; Align Diagnosis codes with drug classes (e.g., Metformin ↔ Diabetes ICD).

- &nbsp; Encode categorical fields (e.g., Gender, DAW, Specialty).

- &nbsp; Normalize numerical features (e.g., Quantity, Days supply).

<h3 align='center'>  4. Business Rule Layer vs ML Model </h3>

- &nbsp; Business Rules Layer (optional): deterministic checks (e.g., if RejectCode=75 → PA=Yes).

- &nbsp; ML Model: learns hidden patterns (drug class + specialty + diagnosis + plan + DAW → PA).

- &nbsp; Hybrid approach works best, but ML alone can also be used.

<h3 align='center'>  5. Dataset Preparation </h3>

- &nbsp; Dummy synthetic dataset created (using Faker + mappings) when real data unavailable.

<h3 align='center'>  Final dataset schema (columns): </h3>

<h4 align='center'> Feature	Description : - </h4>

- &nbsp;  Patient_ID	Unique patient identifier
- &nbsp; DateOfBirth	Patient DOB (used for Age)
- &nbsp; Gender	M/F
- &nbsp; Cardholder_ID, Payer_ID	Insurance identifiers
- &nbsp; BIN, PCN, Group_ID, Person_Code	Plan routing fields
- &nbsp; Prescriber_ID, Prescriber_Specialty	Prescriber info
- &nbsp; Pharmacy_ID	Pharmacy identifier
- &nbsp; NDC_Code, Drug_Name, Drug_Class, Strength	Drug info
- &nbsp; Quantity, Days_Supply, Refills	Prescription details
- &nbsp; Diagnosis_Code	Clinical ICD code
- &nbsp; Daw_Code, Submission_Clarification_Code	Claim submission details
- &nbsp; RejectCode, ResponseStatus	Claim outcome
- &nbsp; PA_Required	Target label (Yes/No)

          ┌───────────────────────┐
          │ Historical NCPDP Data │
          │ (Request + Response)  │
          └───────────┬───────────┘
                      │
                      ▼
         ┌──────────────────────────┐
         │ Data Preprocessing        │
         │ - Clean fields            │
         │ - Derive Age from DOB     │
         │ - Encode categorical vars │
         │ - Normalize numerics      │
         └───────────┬──────────────┘
                     │
                     ▼
        ┌───────────────────────────┐
        │ Feature Engineering        │
        │ - Drug ↔ Class ↔ Diagnosis │
        │ - Specialty mapping        │
        │ - Insurance (BIN, PCN)     │
        │ - DAW & SCC interpretation │
        └───────────┬───────────────┘
                    │
                    ▼
       ┌────────────────────────────┐
       │ Dataset Finalization        │
       │ Features + Label (PA_Y/N)   │
       └───────────┬────────────────┘
                   │
                   ▼
       ┌────────────────────────────┐
       │ ML Model Training           │
       │ (RandomForest / XGBoost)    │
       └───────────┬────────────────┘
                   │
                   ▼
       ┌────────────────────────────┐
       │ Model Evaluation            │
       │ Metrics: Accuracy, Recall,  │
       │ Precision, F1               │
       └───────────┬────────────────┘
                   │
                   ▼
       ┌────────────────────────────┐
       │ Deployment (API Service)    │
       │ - REST API (FastAPI/Flask)  │
       │ - Real-time Claim Check     │
       └───────────┬────────────────┘
                   │
                   ▼
       ┌────────────────────────────┐
       │ Pharmacy Workflow           │
       │ - Flag PA Needed upfront    │
       │ - Reduce payer rejects      │
       │ - Improve patient care      │
       └────────────────────────────┘

📊 NCPDP → Feature Mapping for PA Detection			


<img width="785" height="722" alt="image" src="https://github.com/user-attachments/assets/8bbf3555-5b13-4a06-84ad-4193f3a4c11f" />
