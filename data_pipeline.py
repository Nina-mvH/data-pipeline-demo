from pydantic import BaseModel, Field
import csv
from typing import Optional

#defining the pydantic model with all columns represented
"""
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
"""
class Case(BaseModel):
    loan_number: int = Field(..., alias="LoanNumber")
    date_approved: str = Field(..., alias="DateApproved")  # Assuming DateType is still a string
    SBA_office_code: int = Field(..., alias="SBAOfficeCode")
    processing_method: str = Field(..., alias="ProcessingMethod")
    borrower_name: str = Field(..., alias="BorrowerName")
    borrower_address: str = Field(..., alias="BorrowerAddress")
    borrower_city: str = Field(..., alias="BorrowerCity")
    borrower_state: str = Field(..., alias="BorrowerState")
    borrower_zip: str = Field(..., alias="BorrowerZip")
    loan_status_date: str = Field(..., alias="LoanStatusDate")
    loan_status: str = Field(..., alias="LoanStatus")
    term: int = Field(..., alias="Term")
    SBA_guaranty_percentage: float = Field(..., alias="SBAGuarantyPercentage")
    initial_approval_amount: float = Field(..., alias="InitialApprovalAmount")
    current_approval_amount: float = Field(..., alias="CurrentApprovalAmount")
    undisburded_amount: float = Field(..., alias="UndisbursedAmount")
    franchise_name: str = Field(..., alias="FranchiseName")
    servicing_lender_location_id: int = Field(..., alias="ServicingLenderLocationId")
    servicing_lender_name: str = Field(..., alias="ServicingLenderName")
    servicing_lender_address: str = Field(..., alias="ServicingLenderAddress")
    serviceing_lender_city: str = Field(..., alias="ServicingLenderCity")
    servicing_lender_state: str = Field(..., alias="ServicingLenderState")
    servicing_lender_zip: str = Field(..., alias="ServicingLenderZip")
    rural_urban_indicator: str = Field(..., alias="RuralUrbanIndicator")
    hubzone_indicator: str = Field(..., alias="HubzoneIndicator")
    LMI_indicator: str = Field(..., alias="LMIIndicator")
    business_age_description: str = Field(..., alias="BusinessAgeDescription")
    project_city: str = Field(..., alias="ProjectCity")
    project_county_name: str = Field(..., alias="ProjectCountyName")
    project_state: str = Field(..., alias="ProjectState")
    project_zip: str = Field(..., alias="ProjectZip")
    cd: str = Field(..., alias="CD")
    jobs_reported: int = Field(..., alias="JobsReported")
    NAICS_code: int = Field(..., alias="NAICSCode")
    race: str = Field(..., alias="Race")
    ethnicity: str = Field(..., alias="Ethnicity")
    utilities_proceed: str = Field(..., alias="UtilitiesProceed")
    payroll_proceed: int = Field(..., alias="PayrollProceed")
    mortgage_interest_proceed: str = Field(..., alias="MortgageInterestProceed")
    rent_proceed: str = Field(..., alias="RentProceed")
    refinance_eidl_proceed: str = Field(..., alias="RefinanceEIDLProceed")
    health_care_proceed: str = Field(..., alias="HealthCareProceed")
    debt_interest_proceed: str = Field(..., alias="DebtInterestProceed")
    buisness_type: str = Field(..., alias="BusinessType")
    originating_lender_location_id: int = Field(..., alias="OriginatingLenderLocationId")
    originating_lender: str = Field(..., alias="OriginatingLender")
    originating_lender_city: str = Field(..., alias="OriginatingLenderCity")
    originating_lender_state: str = Field(..., alias="OriginatingLenderState")
    gender: str = Field(..., alias="Gender")
    veteran: str = Field(..., alias="Veteran")
    non_profit: str = Field(..., alias="NonProfit")
    forgiveness_amount: float = Field(..., alias="ForgivenessAmount")
    forgiveness_date: str = Field(..., alias="ForgivenessDate")

#read the csv file 
with open('public_150k_plus_240930.csv', newline='', encoding="cp850") as csvfile:
    reader = csv.DictReader(csvfile)
    records = {}
    for idx, record in enumerate(reader):
        records[idx] = Case.parse_obj(record)
    #for row in reader:
        #print(row)

print(records)
