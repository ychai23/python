#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        self.month = init_month
        self.day = init_day
        self.year = init_year
        # add the necessary assignment statements below


    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####
    def advance_one(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29
        if days_in_month[self.month] == self.day:
            self.month += 1
            self.day = 1
            if self.month == 13:
                self.year += 1
                self.month = 1
        else:
            self.day += 1
            
                
    def advance_n(self, n):
        """ changes the called object so that it represents one calendar day 
            after the date that it originally represented.
            input n: number of days user wants to advance
        """
        print(self.__repr__())
        for days in range(n):
            self.advance_one()
            print(self.__repr__())
            
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) 
            represent the same calendar date
            input other: any date
        """
        if self.day == other.day and self.month== other.month and self.year == other.year:
            return True
        else:
            return False
        
    def is_before(self, other):
        """ returns True if the called object represents a calendar date that 
            occurs before the calendar date that is represented by other.
            input other: any date
        """
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year <= other.year:
            return True
        elif self.day < other.day and self.month <= other.month and self.year <= other.year:
            return True
        else:
            return False
          
    def is_after(self, other):
        """ returns True if the calling object represents a calendar date that 
            occurs after the calendar date that is represented by other.
            input other: any date
        """
        if self.__eq__(other) == True or self.is_before(other) == True:
            return False
        else:
            return True
        
    def days_between(self, other):
        """ returns an integer that represents the number of days between 
            self and other.
            input other: any date
        """
        days_bet = 0
        date1 = self.copy()
        date2 = other.copy()
        if date1.__eq__(date2) == True:
            return 0
        elif date1.is_before(date2) == True:
            while date1.__eq__(date2)==False:
                date1.advance_one()
                days_bet -= 1
        elif date1.is_after(date2) == True:
            while date1.__eq__(date2)==False:
                date2.advance_one()
                days_bet += 1
        return days_bet
            
    def day_name(self):
        """ returns a string that indicates the name of the day of the week of 
            the Date object that calls it.
            input other: any date
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        dayh = Date(11, 11, 2019)
        day_b = self.days_between(dayh)
        return day_names[day_b % 7]
        
            
