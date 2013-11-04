import sys



__author__ = 'xz'



class CompanyDao:

    def __init__(self, database):

        self.db = database

        self.companies = database.companies

        self.company_attr_list = ["name","homepage_url", "blog_url", "description", "founded_year", "number_of_employees","permalink"]



    def insert_entry(self, data):
        if data is not None:
            print "inserting company_dao", data["name"]
            company_dao = {}
            key_set = data.keys()
            for attr in self.company_attr_list :
                if attr in key_set:
                    company_dao[attr] = data[attr]

            try:
                self.companies.insert(company_dao)
            except:
                print "Error inserting company_dao"
                print "Unexpected error:", sys.exc_info()[0]
            return data['permalink']