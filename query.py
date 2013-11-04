import pymongo

import etlUtil

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



# Question 1:
#companiesFunding.get_top_company_total_funding(10)

# Question 2:
#companiesFunding.get_top_change_funding(2011,2012)


# Question 3:
#investorFunding.get_top_total_funding(10)

# Question 4:
investorFunding.get_top_change_funding(2011,2012)

