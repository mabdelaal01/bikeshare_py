import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("""
          \033[1m \t-----------------------------------------------------------\n
          \t\tHello! Let\'s explore some US bikeshare data!\n \n
          \tThis program will allow you to filter by one or more of the following variables:\n
          \t1- City: (Chigaco - New York - Washington)\n
          \t2- Month: (January through June), you can choose 'All' for no filter.\n
          \t3- Day: (Monday through Sunday), you can choose 'All' for no filter.\n
          \tNote: All inputs are case insensitive.\n
          \tLooking forward to sharing some interesting insights with you!\033[0m\n
          \t---------------------------------------------------------------\n""")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please select one of the following cities to explore:\nChicago\nNew York City\nWashington\n--").lower()
        if city in ['chicago','new york city','washington']:
            city = city
            print("\033[1m {} \033[0m Selected!\n".format(city.title()))
            break
        else:
            print("Invalid choice please choose a valid city from (Chicago, New York City or Washington).\n--")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter month between January and June. Type 'All' for no filter.\n--").lower()
        if month in ['january','february','march','april','may','june','all']:
            month = month
            print("\033[1m {} \033[0m Selected!\n".format(month.title()))
            break
        else:
            print("Invalid choice please choose a valid month between January and June. Select 'All' for no filter.\n--")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please select a day. Type 'All' for no filter.\n--").lower()
        if day in ['sunday','monday','tuesday','wednesday','thursdat','friday','saturday','all']:
            day = day
            print("\033[1m {} \033[0m  Selected!\n".format(day.title()))
            break
        else:
            print("Invalid choice please choose a valid day. Type 'All' for no filter.\n--")
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and fichlters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading city data into dataframe df
    df = pd.read_csv(CITY_DATA[city])
    
    #read formatted month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #add month column and day column
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
   
    #filter by month    
    if month != 'all':
       months = ['january','february','march','april','may','june']
       month = months.index(month) + 1 
       df = df[df['Month'] == month]
       #print(df.head())
    else:
        month = 'all'
    
    #filter by day
    if day != 'all':
        #days = ['sunday','monday','tuesday','wednesday','thursdat','friday','saturday']
        df = df[df['Day'] == day.title()]
        #print(df.head())
    else:
        day = 'all'  
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January','February','March','April','May','June']
    index = df['Month'].mode()[0]
    
    print("Most Common Month is: \033[1m {} \033[0m.\n".format(months[index - 1]))
    
    # TO DO: display the most common day of week
    print("Most Common Day is: \033[1m {} \033[0m.\n".format(df['Day'].mode()[0]))
   
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print("Most Common Hour is: \033[1m {} \033[0m.".format(df['Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Commonly used Start Station is:\033[1m {} \033[0m Station.".format(df['Start Station'].mode()[0]))
    print("It was used \033[1m {} \033[0m times".format((df['Start Station'].value_counts().max())))

    # TO DO: display most commonly used end station
    print("Most Commonly used End Station is: \033[1m {} \033[0m Station.".format(df['End Station'].mode()[0]))
    print("It was used \033[1m {}\033[0m times".format((df['End Station'].value_counts().max())))
    # TO DO: display most frequent combination of start station and end station trip
    df['Stations'] = "\nStarting at: " + df['Start Station'] + " and Stopping at: " + df['End Station']
    print("Most Commonly used Combination of Start and End Stations is: {} Station.".format(df['Stations'].mode()[0]))
    print("It was used \033[1m {} \033[0m times".format(df['Stations'].value_counts().max()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time was:\033[1m {} \033[0m seconds".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("Mean Travel Time was: \033[1m {} \033[0m seconds".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count for User Types is:\n\033[1m{} \033[0m".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nCount for User Gender is:\n\033[1m{} \033[0m".format(df['Gender'].value_counts()))
    else:
        print("\nGender data is not available for selected City.\n")
        
    # TO DO: Display earliest, most recent, and most common year of birth-
    if 'Birth Year' in df.columns:
        print("\nEarliest Year of Birth: \033[1m {} \033[0m".format(int(df['Birth Year'].min())))
        print("\nMost Recent Year of Birth: \033[1m {} \033[0m".format(int(df['Birth Year'].max())))
        print("\nMost Common Year of Birth: \033[1m {} \033[0m".format(int(df['Birth Year'].mode()[0])))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_display(df):
    i = 1
    ip = input("Would you like to view a subset of raw data (Y/N) ?\n").lower()
    while True:
        if ip == "y":
            print(df[i:i+5])
            i += 5
            ip = input("Would you like to view more (Y/N) ?\n").lower()
        elif ip == 'n':
            print('-'*40)
            break
        else:
            print("Please enter a valid input.\n")
            ip = input("Would you like to view more (Y/N) ?\n").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_display(df)
        
        restart = input('\nWould you like to restart? Enter (Y/N).\n')
        if restart.lower() != 'y':
            print("\033[1m Thank you for using this program, hope you enjoyed it!\033[0m")
            break


if __name__ == "__main__":
	main()

