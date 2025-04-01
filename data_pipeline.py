from pydantic import BaseModel
import csv

#defining the pydantic model with all columns represented
class Case(BaseModel):
    loan_number: int #
    date_approved: str # to DatType object
    SBA_office_code: int
    processing_method: str
    borrower_name: str
    borrower_address: str
    borrower_city: str
    borrower_state: str
    borrower_zip: str 
    loan_status_date: str
    loan_status: str
    term: int
    SBA_guaranty_percentage: float
    initial_approval_amount: float
    current_approval_amount: float
    undisburded_amount: float
    franchise_name: str
    servicing_lender_location_id: int
    servicing_lender_name: str
    servicing_lender_address: str
    serviceing_lender_city: str
    servicing_lender_state: str
    servicing_lender_zip: str
    rural_urban_indicator: str
    hubzone_indicator: str
    LMI_indicator: str
    business_age_description: str
    project_city:str
    project_county_name: str
    project_state: str
    project_zip: str
    cd: str
    jobs_reported: int
    NAICS_code:int
    race: str
    ethnicity: str
    utilities_proceed: str #check
    payroll_proceed: int #check
    mortgage_interest_proceed: str #check
    rent_proceed: str #check
    refinance_eidl_proceed: str #check
    health_care_proceed: str #check
    debt_interest_proceed: str #check
    buisness_type: str
    originating_lender_location_id: int
    originating_lender: str
    originating_lender_city: str
    originating_lender_state: str
    gender: str
    veteran: str
    non_profit: str
    forgiveness_amount:float
    forgiveness_date: str

#read the csv file 
with open('public_150k_plus_240930.csv', newline='', encoding="cp850") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
