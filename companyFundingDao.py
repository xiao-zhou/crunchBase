

import sys



__author__ = 'xz'


class CompanyFundingDao():

    def __init__(self, database):

        self.db = database

        self.companyFunding = database.companyFunding



    def insert_entry(self, permalink, funded_year, funded_amount):
        company_funding = {"permalink": permalink,

                "funded_year": funded_year,

                "funded_amount": funded_amount}

        try:

            self.companyFunding.insert(company_funding)

        except:

            print "Error inserting CompanyFundingDao"

            print "Unexpected error:", sys.exc_info()[0]
        return permalink

    def parseJsonWithFunding(self,result):
        funding_dict = {}
        for item in result:
            funding_dict[item["_id"]["permalink"]] = item["total_funding"]
        return funding_dict

    def get_top_company_total_funding(self, num):
        company_funding = self.parseJsonWithFunding(self.companyFunding.aggregate( [{ "$group":{"_id" : {"permalink":"$permalink"}, "total_funding" : { "$sum" : "$funded_amount" } } }, {"$project":{ "permalink":1,"total_funding":1}}])["result"])
        i = 0
        for p in sorted(company_funding, key=company_funding.get, reverse=True):
            i += 1
            if i < 11:
                print p," - funding: ", company_funding[p]
        return company_funding

   

    def get_top_change_funding(self, base_year,compare_year):
        base_funding =  self.parseJsonWithFunding(self.companyFunding.aggregate([{"$match" : { "funded_year" : base_year }  }, {"$group" :{ "_id" : {"permalink":"$permalink", "funded_year":"$funding_year"},"total_funding" : { "$sum" : "$funded_amount" } } },{"$project":{ "permalink":1,"total_funding":1}}])["result"])
        compare_funding = self.parseJsonWithFunding(self.companyFunding.aggregate([{"$match" : { "funded_year" : compare_year }  }, {"$group" :{ "_id" : {"permalink":"$permalink", "funded_year":"$funding_year"},"total_funding" : { "$sum" : "$funded_amount" } } },{"$project":{ "permalink":1,"total_funding":1}}])["result"])
        diff_funding = {}
        base_key_set = base_funding.keys()
        for key in compare_funding.keys():
            if key in base_key_set:
                diff_funding[key] = compare_funding[key] - base_funding[key]
            else:
                diff_funding[key] = compare_funding[key]
        i = 0
        for p in sorted(diff_funding, key=diff_funding.get, reverse=True):
            i += 1
            if i < 11:
                print p," - increased funding from 2011 to 2012: ", diff_funding[p]
        return diff_funding

