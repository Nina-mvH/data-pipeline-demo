DROP TABLE IF EXISTS PPP_table;
CREATE TABLE PPP_table (
    LoanNumber Integer,
    DateApproved varchar(255),
    SBAOfficeCode Integer,
    ProcessingMethod Integer,
    BorrowerName varchar(255),
    BorrowerAddress varchar(255),
    BorrowerCity varchar(255),
    BorrowerState varchar(255),
    BorrowerZip varchar(255),
    LoanStatusDate varchar(255),
    LoanStatus varchar(255),
    Term Integer,
    SBAGuarantyPercentage Float,
    InitialApprovalAmount Float,
    CurrentApprovalAmount Float,
    UndisbursedAmount varchar(255),
    FranchiseName varchar(255),
    ServicingLenderLocationId Integer,
    ServicingLenderName varchar(255),
    ServicingLenderAddress varchar(255),
    ServicingLenderCity varchar(255),
    ServicingLenderState varchar(255),
    ServicingLenderZip varchar(255),
    RuralUrbanIndicator varchar(255),
    HubzoneIndicator varchar(255),
    LMIIndicator varchar(255),
    BusinessAgeDescription varchar(255),
    ProjectCity varchar(255),
    ProjectCountyName varchar(255),
    ProjectState varchar(255),
    ProjectZip varchar(255),
    CD varchar(255),
    JobsReported Integer,
    NAICSCode varchar(255),
    Race varchar(255),
    Ethnicity varchar(255),
    UtilitiesProceed varchar(255),
    PayrollProceed Integer,
    MortgageInterestProceed varchar(255),
    RentProceed varchar(255),
    RefinanceEIDLProceed varchar(255),
    HealthCareProceed varchar(255),
    DebtInterestProceed varchar(255),
    BusinessType varchar(255),
    OriginatingLenderLocationId Integer,
    OriginatingLender varchar(255),
    OriginatingLenderCity varchar(255),
    OriginatingLenderState varchar(255),
    Gender varchar(255),
    Veteran varchar(255),
    NonProfit varchar(255),
    ForgivenessAmount varchar(255),
    ForgivenessDate varchar(255)
);

