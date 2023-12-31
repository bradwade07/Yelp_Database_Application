import pyodbc
import string
import secrets
from datetime import datetime 

def stage2():
    num = str(input("Please enter your desired option number: \n1. Search Business \n2. Search User \n3. Make Friends \n4.Review Business \n"))
    while True:
        if num in ['1', '2', '3', '4']:
            if num == "1": searchBusiness()
            elif num == "2": searchUser()
            elif num == "3": makeFriends()
            elif num == "4": reviewBusiness()
            break
               
        else: ("Invalid choice. Please enter 1, 2, 3 or 4:")

def searchBusiness():
    num = str(input("Please choose from one of the following filters: \n1. Minimum Number of Stars \n2. City \n3. Name (or Part of the Name) \n"))
    queryStr = "Select B.business_id, B.name, B.address, B.city, B.stars FROM dbo.business B"
    while True:
        if num in ['1', '2', '3']:
            if num == "1": 
                stars = str(input("Please enter Number of Stars (leave blank if all wanted): "))
                if stars:
                  if not "WHERE" in queryStr:
                    queryStr = queryStr + " WHERE "
                  queryStr = queryStr + " B.stars >= " + stars
            if num == "2":
                city = str(input("Please enter Name of City (leave blank if all wanted): "))
                if city:
                  if not "WHERE" in queryStr:
                    queryStr = queryStr + " WHERE "
                  queryStr = queryStr + " B.city = '" + city + "'"
            if num == "3":
                name = str(input("Please enter Name or part of Name(leave blank if all wanted): "))
                if name:
                  if not "WHERE" in queryStr:
                    queryStr = queryStr + " WHERE "
                  queryStr = queryStr + " B.name = '" + name + "'"
            if num == "1": 
                queryStr = queryStr + " B.stars "
            if num == "2": 
                if "ORDER BY" in queryStr:
                    queryStr = queryStr + ","
                if not "ORDER BY" in queryStr:
                    queryStr = queryStr + " ORDER BY"
                queryStr = queryStr + " B.city "
            if num == "3":
                if "ORDER BY" in queryStr:
                    queryStr = queryStr + "," 
                if not "ORDER BY" in queryStr:
                    queryStr = queryStr + " ORDER BY"
                queryStr = queryStr + " B.name "
            queryStr = queryStr + ";"
            break
        else: 
            print("Invalid choice. Please enter 1, 2 or 3:")

    cur.execute(queryStr)
    row = cur.fetchone()
    if row is None:
        print("The resulting query is empty.")
    else:
        fileName = input("Please enter the file name: ")
        file = open(fileName, 'w')
        output = ""
        file.write(output)
        file.close()
        file = open('query_output.txt', 'a')
        for row in cur:
            output = (
                "Business ID: " + (row.business_id if row.business_id is not None else "N/A") +
                "\nName: " + (row.name if row.name is not None else "N/A") +
        	    "\nAddress: " + (row.address if row.address is not None else "N/A") +
        	    "\nCity: " + (row.city if row.city is not None else "N/A") +
            	"\nNumber of Stars: " + (str(row.stars) if str(row.stars) is not None else "N/A") +
            	"\n\n"
        	) 
        	file.write(output)
    	file.close()

def searchUser():
    num = str(input("Please choose from one of the following filters: \n1. Name (or Part of the Name) \n2. Minimum Review Count \n3. Minimum Average Stars:"))
    queryStr = "Select U.user_id, U.name, U.review_count, U.useful, U.funny, U.cool, U.average_stars, U.yelping_since FROM dbo.user_yelp U"
    while True:
        if num in ['1', '2', '3']:
            if num == "1": 
                name = str(input("Please enter Name or part of Name(leave blank if all wanted): "))
                if name:
                  if not "WHERE" in queryStr:
                    queryStr = queryStr + " WHERE"
                  queryStr = queryStr + " U.name = '" + name + "'"
            if num == "2":
                reviewCount = str(input("Please enter Minimum Number of Review Count (leave blank if all wanted): "))
                if reviewCount:
                  if not "WHERE" in queryStr:
                    queryStr = queryStr + " WHERE"
                  queryStr = queryStr + " U.review_count >= " + reviewCount
            if num == "3":
                averageStars = str(input("Please enter Minimum Number of Average Stars(leave blank if all wanted): "))
                if averageStars:
                  if not "WHERE" in queryStr:
                    queryStr = queryStr + " WHERE"
                  queryStr = queryStr + " U.average_stars >= " + averageStars
            if num == "1": 
                if not "ORDER BY" in queryStr:
                   queryStr = queryStr + " ORDER BY"
                queryStr = queryStr + " U.name "
            if num == "2": 
                if "ORDER BY" in queryStr:
                    queryStr = queryStr + ","
                if not "ORDER BY" in queryStr:
                    queryStr = queryStr + " ORDER BY"
                queryStr = queryStr + " U.review_count "
            if num == "3":
                if "ORDER BY" in queryStr:
                    queryStr = queryStr + ","
                if not "ORDER BY" in queryStr:
                    queryStr = queryStr + " ORDER BY"
                queryStr = queryStr + " U.average_stars "
            queryStr = queryStr + ";"
            break
        else: 
            print("Invalid choice. Please enter 1, 2 or 3:")
    cur.execute(queryStr)
    row = cur.fetchone()
    if row is None:
        print("The resulting query is empty.")
    else:
        fileName = input("Please enter the file name: ")
        file = open(fileName, 'w')
        output = ""
        file.write(output)
        file.close()
        file = open('query_output.txt', 'a')
        for row in cur:
            output = (
                "User ID: ", (row.user_id if row.user_id is not None else "N/A") + 
                  " \nName: " + (row.name if row.name is not None else "N/A") + 
                  " \nReview Count: " + (str(row.review_count) if str(row.review_count) is not None else "N/A") + 
                  " \nUseful: " + (str(row.useful) if str(row.useful) is not None else "N/A") + 
                  " \nFunny: " + (str(row.funny) if str(row.funny) is not None else "N/A") + 
                  " \nCool: " + (str(row.cool) if str(row.cool) is not None else "N/A") + 
                  " \nAverage Stars: " + (str(row.average_stars) if str(row.average_stars) is not None else "N/A") + 
                  " \nYelping Since: " + (str(row.yelping_since) if str(row.yelping_since) is not None else "N/A") + 
                 "\n"
        	) 
        	file.write(output)
    	file.close()

def makeFriends():
    userId = input("Please enter your user ID: ")
    searchUser()
    friendId = input("Please enter friend's user ID: ")
    queryStr = "INSERT INTO dbo.friendship (user_id, friend) VALUES ('" + userId + "', '" + friendId + "');"
    queryStr1 = "INSERT INTO dbo.friendship (user_id, friend) VALUES ('" + friendId + "', '" + userId + "');"
    cur.execute(queryStr)
    cur.execute(queryStr1)


def reviewBusiness():
    
    userId = input("Please enter your User ID: ")
    queryStr = "SELECT * FROM dbo.user_yelp U WHERE U.user_id = '" + str(userId) + "';"
    cur.execute(queryStr)
    row = cur.fetchone()
    if row is None:
        print("User ID " + str(userId) + " is not Found")
        return
    else:
        print("Hello " + str(row.name) + "!")
        businessId = input("Please enter the business ID: ")
        while True: 
            stars = input("Please enter the number of stars (Integer between 1 and 5): ")
            if not '1' <= stars <= '5':
                print("Please enter an integer between 1 and 5")
            else:
                break
        queryStr = "CREATE TRIGGER updateReviewsBusiness ON review AFTER INSERT AS BEGIN update business set review_count = (select count(*) from review where (select max(date) max_date from review r where r.user_id = review.user_id and business_id = inserted.business_id group by user_id) = review.date), stars = (select AVG(CAST(review.stars AS DECIMAL(2,1))) from review where (select max(date) max_date from review r where r.user_id = review.user_id and business_id = inserted.business_id group by user_id) = review.date) from business, inserted where business.business_id = inserted.business_id END;"
        cur.execute(queryStr)
        ch = string.ascii_letters + string.digits + string.punctuation
        reviewId = ''.join(secrets.choice(ch) for i in range (22))
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        queryStr1 = "INSERT INTO dbo.review (review_id, user_id, business_id, stars, useful, funny, cool, date) VALUES ('" + str(reviewId) + "', '" + userId + "', '" + businessId + "', '" + str(stars) + "', '1', '2', '3', '" +  str(time) + "');"
        cur.execute(queryStr1)
        print("Query Executed Successfully!")

def loginFn(login):
    queryStr = "SELECT U.name FROM dbo.user_yelp U WHERE U.name = " + "'" + login + "'"
    cur.execute(queryStr)
    row = cur.fetchone()
    if row is None:
        print("User not found. Please try again.")
        
    else:
        print("Welcome " + login)
        stage2()

def main():
    conn = pyodbc.connect('driver={ODBC Driver 18 for SQL Server};server=cypress.csil.sfu.ca;uid=s_tsa140;pwd=GHg2Ft3RNmy2E667;Encrypt=yes;TrustServerCertificate=yes')
    cur = conn.cursor() 
    print("Welcome To The Yelp Database.")
    login = input("Please enter your name: ")
    loginFn(login)
    cur.close()
    

if __name__== "__main__":
    main()