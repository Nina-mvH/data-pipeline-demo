from pydantic import BaseModel, Field, ConfigDict
import csv
from typing import Optional

#defining the pydantic model with all columns represented
class Case(BaseModel):
    model_config = ConfigDict(from_attributes=True)
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
    undisburded_amount: Optional[str] = Field(None, alias="UndisbursedAmount")
    franchise_name: str = Field(..., alias="FranchiseName")
    servicing_lender_location_id: Optional[int] = Field(None, alias="ServicingLenderLocationId")
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
    jobs_reported: Optional[str] = Field(None, alias="JobsReported") #integer
    NAICS_code: str  = Field(..., alias="NAICSCode")
    race: str = Field(..., alias="Race")
    ethnicity: str = Field(..., alias="Ethnicity")
    utilities_proceed: Optional[str] = Field(None, alias="UtilitiesProceed")
    payroll_proceed: Optional[int] = Field(None, alias="PayrollProceed")
    mortgage_interest_proceed: Optional[str] = Field(None, alias="MortgageInterestProceed")
    rent_proceed: Optional[str] = Field(None, alias="RentProceed")
    refinance_eidl_proceed: Optional[str] = Field(None, alias="RefinanceEIDLProceed")
    health_care_proceed: Optional[str] = Field(None, alias="HealthCareProceed")
    debt_interest_proceed: Optional[str] = Field(None, alias="DebtInterestProceed")
    buisness_type: str = Field(..., alias="BusinessType")
    originating_lender_location_id: Optional[int] = Field(None, alias="OriginatingLenderLocationId")
    originating_lender: str = Field(..., alias="OriginatingLender")
    originating_lender_city: str = Field(..., alias="OriginatingLenderCity")
    originating_lender_state: str = Field(..., alias="OriginatingLenderState")
    gender: str = Field(..., alias="Gender")
    veteran: str = Field(..., alias="Veteran")
    non_profit: str = Field(..., alias="NonProfit")
    forgiveness_amount: Optional[str] = Field(None, alias="ForgivenessAmount")
    forgiveness_date: str = Field(..., alias="ForgivenessDate")

#read the csv file 
with open('public_150k_plus_240930-small.csv', newline='', encoding="cp850") as csvfile:
    reader = csv.DictReader(csvfile)
    records = []
    for record in reader:
        records.append(Case(**record))

print(records)
