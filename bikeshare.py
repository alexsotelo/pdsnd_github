import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january','february','march','april','may','june']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        cities = ['chicago','new york city','washington']

        city = input('The first step is to select a city. Do you want to explore data from Chicago, New York City or Washington?\n').lower()
        if city not in cities:
            print("\nSorry, we don't have data from that city :-(\n")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:



        month = input('\nNow, is there a particular month you\'re interested in? Or you can type \'all\' to view data for all months.\n').lower()
        if month not in months:
            print("\nSorry, we don't have data for that month :-(. Choose a month between january and june.\n")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:



        day = input('\nFinally, is there a particular day of the week you\'re interested in? Or you can type \'all\' to view data for all days.\n').lower()
        if day not in days:
            print("\nSorry, we don't have data for that day :-(.\n")
        else:
            break

    print('-'*40)
    return city, month, day



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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most frecuent month is: ', months[common_month].title())

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most frecuent day of the week is: ', common_day.title())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most frecuent star hour is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: {}.'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most commonly used end station: {}.'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('Most frequent combination of start station and end station: {}.'.format(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: {:.2f} hours.'.format(df[['Trip Duration']].sum()[0]/60/60))

    # display mean travel time
    print('Mean travel time: {:.2f} minutes.'.format(df[['Trip Duration']].mean()[0]/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # Display counts of user types
        print('Counts of user types:\n\n{}'.format(df['User Type'].value_counts()))

        # Display counts of gender
        print('\nCounts of gender:\n\n{}'.format(df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest birth year: {:.0f}'.format(df['Birth Year'].min()))
        print('Most recent birth year: {:.0f}'.format(df['Birth Year'].max()))
        print('Most common birth year: {:.0f}'.format(df['Birth Year'].mode()[0]))
    except:
        print('\nSorry but this city does not have gender or year of birth data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #To print lines of raw data
        lines = 5
        show_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if show_data.lower() == 'yes':
            while True:
                print(df.head(lines))
                lines += 5
                show_data = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n')
                if show_data.lower() != 'yes':
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
