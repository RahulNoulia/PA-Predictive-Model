import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "scripts"))

from pa_claim_dummy_data_generator import generate_dummy_ncpdp_data  # import function from script

def main():
    print("🚀 Project Started!")
    generate_dummy_ncpdp_data(num_records=20000, output_file="ncpdp_dummy_data.csv")

if __name__ == "__main__":
    main()


