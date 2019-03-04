import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

			  
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
	
    Returns: in lower case
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Choose a city from Chicago,New York City or Washington:')
    while(city.lower() not in CITY_DATA.keys()):
        city = input('Choose a city ONLY from Chicago,New York City or Washington:')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter a name of the month to filter by, or "all" to apply no month filter:')
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    while ((month.lower() not in months) and (month != 'all')):
        print(month.lower())
        print((month.lower() not in months))
        print(month!='all')
        month = input('Enter a VALID NAME of the MONTH to filter by, or "all" to apply no month filter:')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturaday','sunday']
    day = input('Enter a day of week or "all" for no filters:')
    while((day.lower() not in days) and (day!='all')):
        day = input('Enter a VALID DAY of WEEK or "all" for no filters:')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    # display the raw data by user's request
    user_request = input("Do you want to see 5 lines of raw data? Yes or No:")
    counter = 0;
    step = 5;
    while user_request.lower()=='yes':
        print(df.loc[counter:counter+step])
        user_request = input("Do you want to see another 5 lines of raw data? Yes or No:")
        counter +=step

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]+1
    months = ['january', 'february', 'march', 'april', 'may','june','july','august','september','october','november','december']
    print('The most commom month:{}'.format(months[most_common_month].title()))

    # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.dayofweek.mode()[0]
    days = ['monday','tuesday','wednesday','thursday','friday','saturaday','sunday']
    print('The most commom day of week:{}'.format(days[most_common_day].title()))
    # TO DO: display the most common start hour
    most_commom_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most commom start hour:{}'.format(most_commom_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commom_start_station = df['Start Station'].mode()[0]
    print('This most commly used start station is:{}'.format(most_commom_start_station))

    # TO DO: display most commonly used end station
    most_commom_end_station = df['End Station'].mode()[0]
    print('This most commly used end station is:{}'.format(most_commom_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination stations'] = df['Start Station']+' '+df['End Station']
    most_combination = df['Combination stations'].mode()[0]
    print('This most frequent combination of start station and end station is:{}'.format(most_combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:{} seconds'.format(total_travel_time))
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travle time is:{} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('-'*40)
        print('User types counts:')
        print(df['User Type'].value_counts())
        print('-'*40)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('-'*40)
        print('Counts of Gender:')
        print(df['Gender'].value_counts())
        print('~'*40)
    else:
        print('Gender data is not available in this dataset')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('-'*40)
        print('Earliest year of birth:')
        print(int(df['Birth Year'].min()))
        print('~'*40)
        
        print('-'*40)
        print('Most recent year of birth:')
        print(int(df['Birth Year'].max()))
        print('~'*40)
        
        print('-'*40)
        print('Most common year of birth:')
        print(int(df['Birth Year'].mode()[0]))
        print('~'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


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
