(a) How you have implemented the scraper, what challenges you faced and how did you solve them?
1)Firstly i needed to know how the walmart website sorts it reviews (i.e. according to some ids or anything else) and 
i discovered not all the details are not uniquely identified by some id but can be identified by their xpaths having
some change at a particular position in their paths.
2)Also needed to think that there are not review titles for all reviews and the scraper i made at starting needed to
have review titles for all reviews so i tweaked it to use a try-except block which checks if there are review title
for the review and if there is not it will add N/A to the review title as default.


(b) What else you could do to improve your scraper?

Could have designed a GUI for the user to give the product page they want the scraper to scrape the details from and
can also implement a list which determines the date better for the scraper for determining the limit till which
the scraper needs to collect the data for.


(c) How would you design it to make it work on other retailers as well?
Just need to change the class names used by the websites for making the different elements of the review identifiable 
for the website.