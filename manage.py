



import pymongo

import util

import companyDao

import companyFundingDao

import investorDao

import InvestorFundingDao



__author__ = "xz"





connection_string = "mongodb://localhost"

connection = pymongo.MongoClient(connection_string)

database = connection.crunchBase



companies = companyDao.CompanyDao(database)

companiesFunding = companyFundingDao.CompanyFundingDao(database)

investor = investorDao.InvestorDao(database)

investorFunding = InvestorFundingDao.InvestorFundingDao(database)



e = util.Util()



# funding_data will be array

def parseFundingRoundsUtil(funding_data, company_permalink):
	for round in funding_data:
		companiesFunding.insert_entry(company_permalink, round["funded_year"],round["raised_amount"])
		for a_investor in round["investments"]:
			# print a_investor
			parseInvestorUtil(a_investor,round["funded_year"],round["raised_amount"])


# Investment data will be dictionary

def parseInvestorUtil(investor_data, funded_year, funding_amount):
    if investor_data["company"] is not None :
    	plink = investor_data["company"]["permalink"]
    	investor.insert_entry(e.getCompanyJsonFromUrl(plink),"company")
    	investorFunding.insert_entry(investor_data["company"]["permalink"], funded_year, funding_amount)
    elif investor_data["person"] is not None :
    	plink = investor_data["person"]["permalink"]
    	investor.insert_entry(e.getPersonJsonFromUrl(plink),"person")
    	investorFunding.insert_entry(investor_data["person"]["permalink"], funded_year, funding_amount)
    elif investor_data["financial_org"] is not None :
    	plink = investor_data["financial_org"]["permalink"]
    	investor.insert_entry(e.getFinancialOrgJsonFromUrl(plink),"financial_org")
    	investorFunding.insert_entry(investor_data["financial_org"]["permalink"], funded_year, funding_amount)


with open("download.txt") as f:
    content = f.readlines()
    for plink in content:
        company_data = e.getCompanyJsonFromUrl(plink.replace("\n", "").replace(" ",""))
        if company_data is not None:
        	companies.insert_entry(company_data)
        	parseFundingRoundsUtil(company_data["funding_rounds"], company_data["permalink"])









