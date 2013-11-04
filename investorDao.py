import sys



class InvestorDao:

    def __init__(self, database):

        self.db = database

        self.investors = database.investors

        self.investor_attr_list = ["name","homepage_url", "blog_url", "description", "founded_year", "number_of_employees","permalink","degrees","first_name","last_name"]



    def insert_entry(self, data, type):

        if data is not None:

            print "inserting InvestorDao", data["permalink"]

            investor_dao = {"type":type}

            key_set = data.keys()

            for attr in self.investor_attr_list :

                if attr in key_set:

                    investor_dao[attr] = data[attr]
            try:
                self.investors.insert(investor_dao)
            except:

                print "Error inserting investor_dao"

                print "Unexpected error:", sys.exc_info()[0]

            return data['permalink']

    def get_investor(self, permalink):
        cursor =  self.investors.find({"permalink":permalink},{"_id":0})
        return dict((record['permalink'], record) for record in cursor)


