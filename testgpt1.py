
# Import requests, time, datetime and pytz modules
import requests
import time
import datetime
import pytz

# Initialize four global variables to store the total sums of aum, followPnl, followerNum and historyFollowerNum values
total_aum_sum = 0
total_followPnl_sum = 0
total_followerNum_sum = 0
total_historyFollowerNum_sum = 0

# Define a function to get the sum of aum, followPnl, followerNum and historyFollowerNum values from one page
def get_sums(page):
    # Get the current time in Iran standard time using the pytz module
    iran_time = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
    # Convert the current time to a unix time stamp using the timestamp method
    unix_time = int(iran_time.timestamp())
    # Format the URL with the given page number and the current unix time stamp
    url = f"https://www.okx.com/priapi/v5/ecotrade/public/follow-rank?t={unix_time}&size=20&type=aum&sort=desc&start={page}"
    # Get the response from the URL
    response = requests.get(url)
    # Parse the JSON data from the response
    data = response.json()["data"][0]["ranks"]
    # Initialize four empty lists to store the values
    aum_list = []
    followPnl_list = []
    followerNum_list = []
    historyFollowerNum_list = []
    # Loop through the data and append the values to the lists
    for item in data:
        aum_list.append(float(item["aum"]))
        followPnl_list.append(float(item["followPnl"]))
        followerNum_list.append(int(item["followerNum"]))
        historyFollowerNum_list.append(int(item["historyFollowerNum"]))
    # Use the built-in sum function to find the sum of all values
    aum_sum = sum(aum_list)
    followPnl_sum = sum(followPnl_list)
    followerNum_sum = sum(followerNum_list)
    historyFollowerNum_sum = sum(historyFollowerNum_list)
    # Return a tuple of the results
    return (aum_sum, followPnl_sum, followerNum_sum, historyFollowerNum_sum)

# Define a function to run the script every five seconds
def run_script():
    # Use four global variables to access and modify the total sums of each value
    global total_aum_sum
    global total_followPnl_sum
    global total_followerNum_sum
    global total_historyFollowerNum_sum
    # Reset the total sums to zero
    total_aum_sum = 0
    total_followPnl_sum = 0
    total_followerNum_sum = 0
    total_historyFollowerNum_sum = 0
    # Loop through the page numbers from 1 to 63
    for page in range(1, 64):
        # Call the get_sums function with the current page number and unpack the results into four variables
        aum_sum, followPnl_sum, followerNum_sum, historyFollowerNum_sum = get_sums(page)
        # Add each variable to the corresponding total sum
        total_aum_sum += aum_sum
        total_followPnl_sum += followPnl_sum
        total_followerNum_sum += followerNum_sum
        total_historyFollowerNum_sum += historyFollowerNum_sum
    # Print the total sums of all values
    print(total_aum_sum)
    print(total_followPnl_sum)
    print(total_followerNum_sum)
    print(total_historyFollowerNum_sum)
    # Use the time.sleep function to wait for five seconds before running the script again
    time.sleep(5)
    # Call the run_script function recursively
    run_script()

# Call the run_script function for the first time
run_script()
