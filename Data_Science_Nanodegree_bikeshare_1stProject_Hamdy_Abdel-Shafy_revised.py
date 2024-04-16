#################################################
###             Hamdy Abdel-Shafy             ###
###   Data Science Track - Nanodegree - FWD   ###
###      The first project of Bikeshare       ###
#################################################


####### def in Python used to define a function. For example, def my_function(): #######
####### use break and continue statements to handle a loop when an external condition is triggered or there may also be a situation when you want to skip a part of the loop and start next execution  #######
###### break statement terminates the current loop and resumes execution at the next statement ######
###### continue statement returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop ######
### To make the code robust, you need to use .lower() function to make the code case-insensitive to handle multiple cases, for example, cHiCago, CHICAGO, Chicago, chicago, etc


## Import packages and functions
import time 
import tabulate
import pandas as pd 
import numpy as np 

## Files to be used
CITY_DATA = { 'chicago': 'chicago.csv', 
              'new york city': 'new_york_city.csv', 
              'washington': 'washington.csv' } 
              
def get_filters(): 
    """ Asks user to choose a city, month, and day from city's bike share data. 
    
    Returns: 
        (str) city - name of the city to be analyzed 
        (str) month - name of the month to be filtered, or "all" for no month filtering 
        (str) day - name of the day in the week to be filtered, or "all" for no day filtering 
    """ 
    
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 

    while True:
      city = input("\nWhich one of the following cities would you like to explore its bikeshare data? chicago, new york city, or washington?\n").lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("Sorry, the city you entered is not presented in the list. Please, try again.")
        continue
      else:
        break
 
    
    # TO DO: get user input for month (all, January, February, March, April, May, or June) 

    while True:
      month = input("\nWhich one of the following months would you like to filter? january, february, march, april, may, june or write 'all' if you do not have any preference?\n").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, the month you entered is not in the list. Please, try again.")
        continue
      else:
        break
        
    # TO DO: get user input for day of week (all, saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday) 

    while True:
      day = input("\nAre you looking for a certain day? If so, kindly enter the day as follows: saturday, sunday, monday, tuesday, wednesday, thursday, friday, or type 'all' if you do not have any preference.\n").lower()
      if day not in ('saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all'):
        print("Sorry, check your spelling and try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day    


def load_data(city, month, day): 
    """ Loads data for the specified city and filters by month and day if applicable. 
    Args: 
        (str) city - name of the city to analyze 
        (str) month - name of the month to filter by, or "all" to apply no month filter 
        (str) day - name of the day of week to filter by, or "all" to apply no day filter 
    Returns: 
        df - Pandas DataFrame containing city data filtered by month and day 
    """ 
    
    # load data into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert starting time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of the week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if needed
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df 


def time_stats(df): 
    """Displays statistics on the most frequent times of travel.""" 
    
    print('\nCalculating The Most Frequent Times of Travel...\n') 
    start_time = time.time() 
    
    # TO DO: display the most common month 

    popular_month = df['month'].mode()[0]
    print('The most common month:', popular_month)    
    
    # TO DO: display the most common day of the week 

    popular_day = df['day_of_week'].mode()[0]
    print('The most common day:', popular_day)    
    
    # TO DO: display the most common starting hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df): 
    """Displays statistics on the most popular stations and trip.""" 

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used starting station 

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('\nThe most commonly used station at starting point:', Start_Station)
    
    # TO DO: display most commonly used ending station 

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used station at ending point:', End_Station)
    
    # TO DO: display most frequent combination of starting and ending stations trip 

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most commonly used stations at starting and ending points for a trip:', Start_Station, " & ", End_Station)    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df): 
    """Displays statistics on the total and average trip duration.""" 
    
    print('\nCalculating Trip Duration...\n') 
    start_time = time.time() 
    
    # TO DO: display total travel time. The number of seconds in a day is 86400: 24*60*60 

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")
    
    # TO DO: display mean travel time 

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 


def user_stats(df): 
    """Displays statistics on bikeshare users.""" 
    
    print('\nCalculating User Stats...\n') 
    start_time = time.time() 
    
    # TO DO: Display counts of user types 

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
    
    # TO DO: Display counts of gender 

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender types:\n', gender_types)
    except KeyError:
      print("\nGender types:\nThe requested information is not available for this month.")
    
    # TO DO: Display earliest, most recent, and most common year of birth 

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nThe requested information is not available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nThe requested information is not available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nThe requested information is not available for this month.")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

# Ask user if he/she wants to to view the raw data and print 5 rows.
def ask_view(df):
    start_loc = 0
	while True:
	    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
	    if display_data.lower() != 'yes':
		    break
		print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
	    i+=5


def main(): 
    while True: 
        city, month, day = get_filters() 
        df = load_data(city, month, day) 
        
        time_stats(df) 
        station_stats(df) 
        trip_duration_stats(df) 
        user_stats(df) 
        
        restart = input('\nWould you like to restart? Enter yes or no.\n') 
        if restart.lower() != 'yes': 
            break 


if __name__ == "__main__": 
    main()