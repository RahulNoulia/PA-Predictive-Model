# PA-Predictive-Model

📊 NCPDP → Feature Mapping for PA Detection			
Category	Field Name	NCPDP/Source	Why Needed?
			
Patient	Age (derived from DOB)	304-C4	Age cutoffs (e.g., pediatric vs adult drugs)
	Gender	305-C5	Some drugs are gender-specific
	Diagnosis_Code	424-DO	ICD code → clinical justification
Insurance	BIN	101-A1	Payer routing
	PCN	104-A4	Payer routing
	Group_ID	301-C1	Employer/plan-level rules
Prescription/Drug	NDC_Code	407-D7	Unique drug identifier
	Drug_Name	Derived	Interpretability
	Drug_Class	Derived (ATC/therapeutic class)	Class-level PA rules
	Strength	Derived from NDC	PA may depend on strength (e.g., >20mg needs PA)
	Quantity	442-E7	Large qty may need PA
	Days_Supply	405-D5	Long days supply may need PA
	Refills	403-D3	High refill count → PA trigger
	DAW_Code	408-D8	Brand vs generic substitution rules
	Submission_Clarification_Code	420-DK	Special cases (lost meds, vacation, etc.)
Prescriber	Prescriber_Specialty	427-DR	Certain drugs only approved if specialist prescribes
Claim Outcome	RejectCode	511-FB	Rejection reason (e.g., 75, 76 → PA required)
	ResponseStatus	503-F3	Approved/Rejected
	PA_Required (Target)	461-EU / 498-H9	Model output label
<img width="785" height="722" alt="image" src="https://github.com/user-attachments/assets/8bbf3555-5b13-4a06-84ad-4193f3a4c11f" />
