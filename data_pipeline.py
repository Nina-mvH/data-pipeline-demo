from pydantic import BaseModel, Field, ConfigDict
import csv
from datetime import datetime
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, insert, BigInteger
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

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
    undisbursed_amount: Optional[str] = Field(None, alias="UndisbursedAmount")
    franchise_name: str = Field(..., alias="FranchiseName")
    servicing_lender_location_id: Optional[int] = Field(None, alias="ServicingLenderLocationId")
    servicing_lender_name: str = Field(..., alias="ServicingLenderName")
    servicing_lender_address: str = Field(..., alias="ServicingLenderAddress")
    servicing_lender_city: str = Field(..., alias="ServicingLenderCity")
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
    business_type: str = Field(..., alias="BusinessType")
    originating_lender_location_id: Optional[int] = Field(None, alias="OriginatingLenderLocationId")
    originating_lender: str = Field(..., alias="OriginatingLender")
    originating_lender_city: str = Field(..., alias="OriginatingLenderCity")
    originating_lender_state: str = Field(..., alias="OriginatingLenderState")
    gender: str = Field(..., alias="Gender")
    veteran: str = Field(..., alias="Veteran")
    non_profit: str = Field(..., alias="NonProfit")
    forgiveness_amount: Optional[str] = Field(None, alias="ForgivenessAmount")
    forgiveness_date: str = Field(..., alias="ForgivenessDate")

#Base = declarative_base()
class Base(DeclarativeBase):
    pass

class CaseDB(Base):
    __tablename__='PPP_table'

    loan_number: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    #date_approved: Mapped[str] = mapped_column(String(20))
    date_approved: Mapped[str] = mapped_column(Date)
    SBA_office_code: Mapped[int] = mapped_column(Integer)
    processing_method: Mapped[str] = mapped_column(String(50))
    borrower_name: Mapped[str] = mapped_column(String(255))
    borrower_address: Mapped[str] = mapped_column(String(255))
    borrower_city: Mapped[str] = mapped_column(String(100))
    borrower_state: Mapped[str] = mapped_column(String(10))
    borrower_zip: Mapped[str] = mapped_column(String(20))
    loan_status_date: Mapped[str] = mapped_column(String(20))
    loan_status: Mapped[str] = mapped_column(String(50))
    term: Mapped[int] = mapped_column(Integer)
    SBA_guaranty_percentage: Mapped[float] = mapped_column(Float)
    initial_approval_amount: Mapped[float] = mapped_column(Float)
    current_approval_amount: Mapped[float] = mapped_column(Float)
    undisbursed_amount: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    franchise_name: Mapped[str] = mapped_column(String(255))
    servicing_lender_location_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    servicing_lender_name: Mapped[str] = mapped_column(String(255))
    servicing_lender_address: Mapped[str] = mapped_column(String(255))
    servicing_lender_city: Mapped[str] = mapped_column(String(100))
    servicing_lender_state: Mapped[str] = mapped_column(String(10))
    servicing_lender_zip: Mapped[str] = mapped_column(String(20))
    rural_urban_indicator: Mapped[str] = mapped_column(String(50))
    hubzone_indicator: Mapped[str] = mapped_column(String(50))
    LMI_indicator: Mapped[str] = mapped_column(String(50))
    business_age_description: Mapped[str] = mapped_column(String(255))
    project_city: Mapped[str] = mapped_column(String(100))
    project_county_name: Mapped[str] = mapped_column(String(255))
    project_state: Mapped[str] = mapped_column(String(10))
    project_zip: Mapped[str] = mapped_column(String(20))
    cd: Mapped[str] = mapped_column(String(50))
    jobs_reported: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    NAICS_code: Mapped[str] = mapped_column(String(50))
    race: Mapped[str] = mapped_column(String(50))
    ethnicity: Mapped[str] = mapped_column(String(50))
    utilities_proceed: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    payroll_proceed: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    mortgage_interest_proceed: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    rent_proceed: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    refinance_eidl_proceed: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    health_care_proceed: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    debt_interest_proceed: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    business_type: Mapped[str] = mapped_column(String(255))
    originating_lender_location_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    originating_lender: Mapped[str] = mapped_column(String(255))
    originating_lender_city: Mapped[str] = mapped_column(String(100))
    originating_lender_state: Mapped[str] = mapped_column(String(10))
    gender: Mapped[str] = mapped_column(String(50))
    veteran: Mapped[str] = mapped_column(String(50))
    non_profit: Mapped[str] = mapped_column(String(50))
    forgiveness_amount: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    forgiveness_date: Mapped[str] = mapped_column(String(20))

DATABASE_URL = "mysql+pymysql://nvhoo:pass@localhost:3306/PPP_data"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = SessionLocal()

#read the csv file 
with open('public_150k_plus_240930-small.csv', newline='', encoding="cp850") as csvfile:
    reader = csv.DictReader(csvfile)
    records = []
    for i, record in enumerate(reader):
        #if i == 0:
        #    continue
        case_data = Case(**record)
        case_dict = case_data.model_dump()
        case_dict["date_approved"] = datetime.strptime(case_dict["date_approved"], "%m/%d/%Y").date()
        case_orm=CaseDB(**case_dict)
        #case_orm = CaseDB(**case_data.model_dump())
        session.add(case_orm)
    session.commit()

session.close()
