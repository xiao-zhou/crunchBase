import sys
import pymongo

import investorDao

__author__ = 'xz'


class InvestorFundingDao:

    def __init__(self, database):

        self.db = database

        self.investorsFunding = database.investorsFunding

    def insert_entry(self, permalink, funded_year, funded_amount):

        investor_funding = {"permalink": permalink,"funding_year": funded_year,"funding_amount": funded_amount}

        try:
            print "insert investor_funding", investor_funding
            self.investorsFunding.insert(investor_funding)
        except:
            print "Error inserting InvestorFundingDao"
            print "Unexpected error:", sys.exc_info()[0]

    def parseJsonWithFunding(self,result):
        funding_dict = {}
        for item in result:
            funding_dict[item["_id"]["permalink"]] = item["total_funding"]
        return funding_dict

    def get_top_total_funding(self, num):
        investor_funding = self.parseJsonWithFunding(self.investorsFunding.aggregate( [{ "$group":{"_id" : {"permalink":"$permalink"}, "total_funding" : { "$sum" : "$funding_amount" } } }, {"$project":{ "permalink":1,"total_funding":1}}])["result"])
        i = 0
        for p in sorted(investor_funding, key=investor_funding.get, reverse=True):
            i += 1
            if i < 11:
                print "Investor: " , p," - total funding: ", investor_funding[p]
        return investor_funding


    def get_top_change_funding(self, base_year,compare_year):
        connection_string = "mongodb://localhost"
        connection = pymongo.MongoClient(connection_string)
        database = connection.crunchBase
        investor = investorDao.InvestorDao(database)
        base_funding =  self.parseJsonWithFunding(self.investorsFunding.aggregate([{"$match" : { "funding_year" : base_year }  }, {"$group" :{ "_id" : {"permalink":"$permalink", "funded_year":"$funding_year"},"total_funding" : { "$sum" : "$funding_amount" } } },{"$project":{ "permalink":1,"total_funding":1}}])["result"])
        compare_funding = self.parseJsonWithFunding(self.investorsFunding.aggregate([{"$match" : { "funding_year" : compare_year }  }, {"$group" :{ "_id" : {"permalink":"$permalink", "funded_year":"$funding_year"},"total_funding" : { "$sum" : "$funding_amount" } } },{"$project":{ "permalink":1,"total_funding":1}}])["result"])
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
                print "Investor:" , p,"- increased funding from 2011 to 2012: ", diff_funding[p]
                #print investor.get_investor(p)


