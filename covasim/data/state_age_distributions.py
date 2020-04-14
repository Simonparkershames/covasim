def state_age_distributions():
    """
    This data is translated from the US Census csv to
    the new json format expressed as a function
    """
    data = {'usa-alaska': {'0-5': 7.1, '5-9': 7.1, '10-14': 6.7, '15-19': 6.6, '20-24': 6.7, '25-29': 8.5, '30-34': 7.5, '35-39': 7.3, '40-44': 5.9, '45-49': 5.8, '50-54': 6.4, '55-59': 6.4, '60-64': 6.2, '65-69': 5.1, '70-74': 3.0, '75-79': 1.7, '80-84': 1.1, '85+': 1.0}, 'usa-maine': {'0-5': 4.7, '5-9': 5.1, '10-14': 5.4, '15-19': 5.8, '20-24': 5.5, '25-29': 6.0, '30-34': 6.0, '35-39': 6.0, '40-44': 5.5, '45-49': 6.3, '50-54': 7.1, '55-59': 7.9, '60-64': 8.1, '65-69': 6.9, '70-74': 5.3, '75-79': 3.4, '80-84': 2.3, '85+': 2.6}, 'usa-north carolina': {'0-5': 5.8, '5-9': 6.0, '10-14': 6.5, '15-19': 6.8, '20-24': 6.6, '25-29': 6.9, '30-34': 6.4, '35-39': 6.4, '40-44': 6.2, '45-49': 6.7, '50-54': 6.6, '55-59': 6.5, '60-64': 6.4, '65-69': 5.4, '70-74': 4.4, '75-79': 3.0, '80-84': 1.8, '85+': 1.7}, 'usa-missouri': {'0-5': 6.0, '5-9': 6.1, '10-14': 6.5, '15-19': 6.4, '20-24': 6.6, '25-29': 6.9, '30-34': 6.5, '35-39': 6.4, '40-44': 5.7, '45-49': 6.0, '50-54': 6.2, '55-59': 6.8, '60-64': 6.7, '65-69': 5.3, '70-74': 4.4, '75-79': 3.1, '80-84': 2.0, '85+': 2.0}, 'usa-pennsylvania': {'0-5': 5.5, '5-9': 5.5, '10-14': 6.1, '15-19': 6.4, '20-24': 6.3, '25-29': 6.8, '30-34': 6.5, '35-39': 6.1, '40-44': 5.6, '45-49': 6.3, '50-54': 6.7, '55-59': 7.2, '60-64': 7.0, '65-69': 5.8, '70-74': 4.5, '75-79': 3.3, '80-84': 2.3, '85+': 2.4}, 'usa-michigan': {'0-5': 5.7, '5-9': 5.9, '10-14': 6.2, '15-19': 6.6, '20-24': 6.9, '25-29': 6.9, '30-34': 6.0, '35-39': 6.0, '40-44': 5.6, '45-49': 6.3, '50-54': 6.6, '55-59': 7.0, '60-64': 7.0, '65-69': 5.7, '70-74': 4.4, '75-79': 3.1, '80-84': 2.0, '85+': 2.0}, 'usa-nebraska': {'0-5': 6.8, '5-9': 6.7, '10-14': 7.1, '15-19': 6.9, '20-24': 6.9, '25-29': 6.6, '30-34': 6.7, '35-39': 6.8, '40-44': 5.8, '45-49': 5.7, '50-54': 5.6, '55-59': 6.4, '60-64': 6.2, '65-69': 5.3, '70-74': 3.7, '75-79': 2.6, '80-84': 2.0, '85+': 2.2}, 'usa-oregon': {'0-5': 5.5, '5-9': 5.7, '10-14': 6.1, '15-19': 6.0, '20-24': 6.3, '25-29': 7.2, '30-34': 7.0, '35-39': 6.9, '40-44': 6.4, '45-49': 6.4, '50-54': 6.0, '55-59': 6.4, '60-64': 6.6, '65-69': 6.2, '70-74': 4.5, '75-79': 3.1, '80-84': 2.0, '85+': 1.9}, 'usa-wyoming': {'0-5': 6.1, '5-9': 6.0, '10-14': 7.0, '15-19': 7.1, '20-24': 5.7, '25-29': 6.7, '30-34': 6.6, '35-39': 6.8, '40-44': 5.7, '45-49': 5.8, '50-54': 5.9, '55-59': 6.6, '60-64': 7.2, '65-69': 6.2, '70-74': 4.1, '75-79': 3.0, '80-84': 1.8, '85+': 1.6}, 'usa-california': {'0-5': 6.1, '5-9': 6.1, '10-14': 6.7, '15-19': 6.5, '20-24': 6.9, '25-29': 7.9, '30-34': 7.4, '35-39': 7.0, '40-44': 6.3, '45-49': 6.5, '50-54': 6.3, '55-59': 6.3, '60-64': 5.8, '65-69': 4.7, '70-74': 3.6, '75-79': 2.5, '80-84': 1.7, '85+': 1.8}, 'usa-mississippi': {'0-5': 6.0, '5-9': 6.4, '10-14': 7.2, '15-19': 7.3, '20-24': 6.9, '25-29': 6.6, '30-34': 6.0, '35-39': 6.7, '40-44': 6.0, '45-49': 6.0, '50-54': 6.1, '55-59': 6.4, '60-64': 6.5, '65-69': 5.2, '70-74': 4.3, '75-79': 3.0, '80-84': 1.8, '85+': 1.6}, 'usa-connecticut': {'0-5': 5.1, '5-9': 5.4, '10-14': 6.3, '15-19': 6.8, '20-24': 6.7, '25-29': 6.2, '30-34': 6.3, '35-39': 6.0, '40-44': 5.9, '45-49': 6.6, '50-54': 7.3, '55-59': 7.3, '60-64': 7.1, '65-69': 5.2, '70-74': 4.4, '75-79': 3.1, '80-84': 2.0, '85+': 2.5}, 'usa-texas': {'0-5': 7.0, '5-9': 6.9, '10-14': 7.6, '15-19': 7.2, '20-24': 6.9, '25-29': 7.4, '30-34': 7.2, '35-39': 7.1, '40-44': 6.5, '45-49': 6.4, '50-54': 6.0, '55-59': 5.9, '60-64': 5.4, '65-69': 4.3, '70-74': 3.3, '75-79': 2.2, '80-84': 1.4, '85+': 1.3}, 'usa-idaho': {'0-5': 6.5, '5-9': 7.1, '10-14': 7.4, '15-19': 7.2, '20-24': 6.6, '25-29': 6.7, '30-34': 6.3, '35-39': 6.3, '40-44': 6.2, '45-49': 5.9, '50-54': 5.6, '55-59': 6.4, '60-64': 5.9, '65-69': 5.5, '70-74': 4.1, '75-79': 3.0, '80-84': 1.6, '85+': 1.7}, 'usa-maryland': {'0-5': 6.0, '5-9': 6.0, '10-14': 6.4, '15-19': 6.3, '20-24': 6.4, '25-29': 6.9, '30-34': 6.8, '35-39': 6.8, '40-44': 6.0, '45-49': 6.6, '50-54': 7.0, '55-59': 6.9, '60-64': 6.5, '65-69': 5.0, '70-74': 4.0, '75-79': 2.8, '80-84': 1.8, '85+': 1.8}, 'usa-new mexico': {'0-5': 5.7, '5-9': 6.1, '10-14': 7.2, '15-19': 6.8, '20-24': 6.6, '25-29': 6.7, '30-34': 6.6, '35-39': 6.5, '40-44': 5.7, '45-49': 5.7, '50-54': 5.8, '55-59': 6.5, '60-64': 6.5, '65-69': 5.8, '70-74': 4.7, '75-79': 3.1, '80-84': 2.0, '85+': 1.9}, 'usa-alabama': {'0-5': 5.9, '5-9': 5.9, '10-14': 6.6, '15-19': 6.8, '20-24': 6.5, '25-29': 6.8, '30-34': 6.2, '35-39': 6.0, '40-44': 6.1, '45-49': 6.3, '50-54': 6.5, '55-59': 6.8, '60-64': 6.5, '65-69': 5.5, '70-74': 4.6, '75-79': 3.1, '80-84': 2.0, '85+': 1.7}, 'usa-tennessee': {'0-5': 6.0, '5-9': 6.1, '10-14': 6.4, '15-19': 6.5, '20-24': 6.5, '25-29': 7.2, '30-34': 6.4, '35-39': 6.4, '40-44': 6.1, '45-49': 6.6, '50-54': 6.5, '55-59': 6.6, '60-64': 6.6, '65-69': 5.4, '70-74': 4.3, '75-79': 3.0, '80-84': 1.9, '85+': 1.7}, 'usa-vermont': {'0-5': 4.6, '5-9': 5.1, '10-14': 5.4, '15-19': 6.7, '20-24': 6.9, '25-29': 6.2, '30-34': 5.8, '35-39': 5.9, '40-44': 5.3, '45-49': 6.1, '50-54': 6.8, '55-59': 7.5, '60-64': 7.8, '65-69': 6.9, '70-74': 5.2, '75-79': 3.5, '80-84': 2.1, '85+': 2.1}, 'usa-nevada': {'0-5': 6.1, '5-9': 6.2, '10-14': 6.6, '15-19': 6.0, '20-24': 5.9, '25-29': 7.4, '30-34': 7.1, '35-39': 6.8, '40-44': 6.5, '45-49': 6.7, '50-54': 6.4, '55-59': 6.3, '60-64': 6.1, '65-69': 5.2, '70-74': 4.4, '75-79': 2.8, '80-84': 1.7, '85+': 1.5}, 'usa-west virginia': {'0-5': 5.2, '5-9': 5.4, '10-14': 5.9, '15-19': 6.2, '20-24': 6.3, '25-29': 6.0, '30-34': 5.6, '35-39': 5.9, '40-44': 6.2, '45-49': 6.4, '50-54': 6.5, '55-59': 7.1, '60-64': 7.3, '65-69': 7.1, '70-74': 4.9, '75-79': 3.6, '80-84': 2.3, '85+': 2.2}, 'usa-oklahoma': {'0-5': 6.5, '5-9': 6.6, '10-14': 7.1, '15-19': 6.9, '20-24': 6.8, '25-29': 7.1, '30-34': 6.6, '35-39': 6.6, '40-44': 5.8, '45-49': 5.9, '50-54': 5.8, '55-59': 6.5, '60-64': 6.0, '65-69': 5.1, '70-74': 4.1, '75-79': 2.8, '80-84': 1.9, '85+': 1.8}, 'usa-wisconsin': {'0-5': 5.7, '5-9': 5.9, '10-14': 6.4, '15-19': 6.5, '20-24': 6.8, '25-29': 6.4, '30-34': 6.3, '35-39': 6.5, '40-44': 5.7, '45-49': 6.0, '50-54': 6.7, '55-59': 7.2, '60-64': 7.0, '65-69': 5.7, '70-74': 4.2, '75-79': 2.9, '80-84': 2.1, '85+': 2.1}, 'usa-puerto rico': {'0-5': 3.9, '5-9': 5.2, '10-14': 5.7, '15-19': 6.6, '20-24': 7.0, '25-29': 6.5, '30-34': 5.5, '35-39': 5.8, '40-44': 6.6, '45-49': 6.4, '50-54': 6.8, '55-59': 6.7, '60-64': 6.6, '65-69': 5.9, '70-74': 5.5, '75-79': 4.0, '80-84': 2.8, '85+': 2.6}, 'usa-kansas': {'0-5': 6.4, '5-9': 6.5, '10-14': 7.2, '15-19': 7.0, '20-24': 7.2, '25-29': 6.6, '30-34': 6.3, '35-39': 6.4, '40-44': 5.9, '45-49': 5.8, '50-54': 5.9, '55-59': 6.5, '60-64': 6.3, '65-69': 5.4, '70-74': 3.7, '75-79': 2.7, '80-84': 1.9, '85+': 2.2}, 'usa-virginia': {'0-5': 5.9, '5-9': 6.0, '10-14': 6.3, '15-19': 6.6, '20-24': 6.8, '25-29': 6.9, '30-34': 6.9, '35-39': 6.8, '40-44': 6.3, '45-49': 6.5, '50-54': 6.6, '55-59': 6.7, '60-64': 6.2, '65-69': 5.2, '70-74': 3.9, '75-79': 2.8, '80-84': 1.8, '85+': 1.7}, 'usa-north dakota': {'0-5': 6.9, '5-9': 6.7, '10-14': 6.2, '15-19': 6.1, '20-24': 8.2, '25-29': 8.1, '30-34': 7.3, '35-39': 6.6, '40-44': 5.3, '45-49': 5.3, '50-54': 5.4, '55-59': 6.5, '60-64': 6.0, '65-69': 5.0, '70-74': 3.5, '75-79': 2.5, '80-84': 2.0, '85+': 2.4}, 'usa-new jersey': {'0-5': 5.8, '5-9': 5.8, '10-14': 6.4, '15-19': 6.2, '20-24': 6.2, '25-29': 6.5, '30-34': 6.4, '35-39': 6.6, '40-44': 6.3, '45-49': 6.7, '50-54': 7.1, '55-59': 7.1, '60-64': 6.6, '65-69': 5.1, '70-74': 4.1, '75-79': 2.9, '80-84': 1.9, '85+': 2.2}, 'usa-ohio': {'0-5': 5.9, '5-9': 5.9, '10-14': 6.4, '15-19': 6.6, '20-24': 6.4, '25-29': 6.8, '30-34': 6.3, '35-39': 6.2, '40-44': 5.8, '45-49': 6.3, '50-54': 6.5, '55-59': 7.0, '60-64': 6.8, '65-69': 5.6, '70-74': 4.2, '75-79': 3.1, '80-84': 2.0, '85+': 2.1}, 'usa-south carolina': {'0-5': 5.7, '5-9': 6.0, '10-14': 6.4, '15-19': 6.7, '20-24': 6.5, '25-29': 6.7, '30-34': 6.2, '35-39': 6.2, '40-44': 6.0, '45-49': 6.2, '50-54': 6.3, '55-59': 6.9, '60-64': 6.5, '65-69': 6.0, '70-74': 4.9, '75-79': 3.2, '80-84': 1.9, '85+': 1.7}, 'usa-georgia': {'0-5': 6.1, '5-9': 6.5, '10-14': 7.0, '15-19': 7.2, '20-24': 6.8, '25-29': 7.1, '30-34': 6.6, '35-39': 6.8, '40-44': 6.5, '45-49': 6.8, '50-54': 6.5, '55-59': 6.3, '60-64': 5.8, '65-69': 4.7, '70-74': 3.8, '75-79': 2.5, '80-84': 1.5, '85+': 1.4}, 'usa-colorado': {'0-5': 5.9, '5-9': 6.2, '10-14': 6.4, '15-19': 6.5, '20-24': 6.6, '25-29': 7.9, '30-34': 7.8, '35-39': 7.1, '40-44': 6.6, '45-49': 6.5, '50-54': 6.0, '55-59': 6.4, '60-64': 6.1, '65-69': 5.0, '70-74': 3.8, '75-79': 2.3, '80-84': 1.5, '85+': 1.5}, 'usa-hawaii': {'0-5': 6.2, '5-9': 5.9, '10-14': 6.0, '15-19': 5.5, '20-24': 6.4, '25-29': 7.3, '30-34': 6.9, '35-39': 6.7, '40-44': 6.1, '45-49': 6.0, '50-54': 6.0, '55-59': 6.1, '60-64': 6.6, '65-69': 6.0, '70-74': 4.6, '75-79': 2.9, '80-84': 2.2, '85+': 2.8}, 'usa-south dakota': {'0-5': 6.8, '5-9': 6.7, '10-14': 7.0, '15-19': 6.8, '20-24': 6.7, '25-29': 7.0, '30-34': 6.2, '35-39': 6.3, '40-44': 5.6, '45-49': 5.3, '50-54': 5.7, '55-59': 6.7, '60-64': 6.7, '65-69': 5.5, '70-74': 4.1, '75-79': 2.7, '80-84': 1.8, '85+': 2.5}, 'usa-indiana': {'0-5': 6.2, '5-9': 6.4, '10-14': 6.7, '15-19': 6.9, '20-24': 7.0, '25-29': 6.8, '30-34': 6.2, '35-39': 6.5, '40-44': 5.8, '45-49': 6.2, '50-54': 6.3, '55-59': 6.7, '60-64': 6.4, '65-69': 5.2, '70-74': 3.9, '75-79': 2.8, '80-84': 1.8, '85+': 1.9}, 'usa-kentucky': {'0-5': 6.1, '5-9': 6.3, '10-14': 6.4, '15-19': 6.5, '20-24': 6.7, '25-29': 6.9, '30-34': 6.1, '35-39': 6.3, '40-44': 6.1, '45-49': 6.4, '50-54': 6.5, '55-59': 6.8, '60-64': 6.6, '65-69': 5.5, '70-74': 4.3, '75-79': 2.9, '80-84': 2.0, '85+': 1.8}, 'usa-louisiana': {'0-5': 6.5, '5-9': 6.4, '10-14': 6.8, '15-19': 6.6, '20-24': 6.6, '25-29': 7.1, '30-34': 6.8, '35-39': 6.8, '40-44': 5.8, '45-49': 6.0, '50-54': 6.2, '55-59': 6.5, '60-64': 6.4, '65-69': 5.4, '70-74': 3.9, '75-79': 2.8, '80-84': 1.8, '85+': 1.6}, 'usa-washington': {'0-5': 6.1, '5-9': 6.2, '10-14': 6.2, '15-19': 6.0, '20-24': 6.3, '25-29': 7.8, '30-34': 7.5, '35-39': 7.2, '40-44': 6.2, '45-49': 6.3, '50-54': 6.1, '55-59': 6.5, '60-64': 6.3, '65-69': 5.3, '70-74': 4.2, '75-79': 2.7, '80-84': 1.6, '85+': 1.7}, 'usa-illinois': {'0-5': 6.0, '5-9': 6.0, '10-14': 6.6, '15-19': 6.6, '20-24': 6.6, '25-29': 7.1, '30-34': 6.8, '35-39': 6.6, '40-44': 6.3, '45-49': 6.4, '50-54': 6.4, '55-59': 6.7, '60-64': 6.4, '65-69': 5.0, '70-74': 3.9, '75-79': 2.8, '80-84': 1.8, '85+': 2.0}, 'usa-iowa': {'0-5': 6.3, '5-9': 6.3, '10-14': 6.8, '15-19': 7.0, '20-24': 7.0, '25-29': 6.4, '30-34': 6.1, '35-39': 6.6, '40-44': 5.5, '45-49': 5.8, '50-54': 5.9, '55-59': 6.8, '60-64': 6.5, '65-69': 5.4, '70-74': 4.1, '75-79': 3.0, '80-84': 2.2, '85+': 2.4}, 'usa-new hampshire': {'0-5': 4.6, '5-9': 5.1, '10-14': 5.7, '15-19': 6.8, '20-24': 6.3, '25-29': 6.3, '30-34': 6.1, '35-39': 5.9, '40-44': 5.6, '45-49': 6.6, '50-54': 7.4, '55-59': 8.2, '60-64': 7.5, '65-69': 6.1, '70-74': 4.7, '75-79': 3.1, '80-84': 1.9, '85+': 2.3}, 'usa-rhode island': {'0-5': 5.1, '5-9': 5.4, '10-14': 5.2, '15-19': 7.1, '20-24': 7.1, '25-29': 7.3, '30-34': 6.6, '35-39': 6.2, '40-44': 5.4, '45-49': 6.3, '50-54': 7.0, '55-59': 6.9, '60-64': 7.1, '65-69': 5.3, '70-74': 4.4, '75-79': 2.9, '80-84': 2.1, '85+': 2.5}, 'usa-arkansas': {'0-5': 6.2, '5-9': 6.4, '10-14': 6.8, '15-19': 6.9, '20-24': 6.6, '25-29': 6.8, '30-34': 6.3, '35-39': 6.3, '40-44': 5.9, '45-49': 6.1, '50-54': 6.2, '55-59': 6.5, '60-64': 6.2, '65-69': 5.4, '70-74': 4.5, '75-79': 3.2, '80-84': 1.9, '85+': 1.9}, 'usa-delaware': {'0-5': 5.6, '5-9': 5.4, '10-14': 6.5, '15-19': 6.1, '20-24': 6.2, '25-29': 6.8, '30-34': 6.3, '35-39': 6.1, '40-44': 5.5, '45-49': 6.0, '50-54': 6.7, '55-59': 7.1, '60-64': 7.0, '65-69': 6.2, '70-74': 5.0, '75-79': 3.8, '80-84': 1.8, '85+': 1.9}, 'usa-minnesota': {'0-5': 6.3, '5-9': 6.4, '10-14': 6.6, '15-19': 6.4, '20-24': 6.4, '25-29': 6.7, '30-34': 6.8, '35-39': 6.8, '40-44': 5.9, '45-49': 6.0, '50-54': 6.3, '55-59': 7.1, '60-64': 6.3, '65-69': 5.3, '70-74': 3.8, '75-79': 2.8, '80-84': 1.9, '85+': 2.1}, 'usa-montana': {'0-5': 5.8, '5-9': 5.8, '10-14': 6.4, '15-19': 6.3, '20-24': 6.4, '25-29': 6.5, '30-34': 6.1, '35-39': 6.5, '40-44': 5.6, '45-49': 5.6, '50-54': 5.8, '55-59': 6.8, '60-64': 7.5, '65-69': 6.5, '70-74': 4.9, '75-79': 3.5, '80-84': 2.0, '85+': 2.0}, 'usa-arizona': {'0-5': 6.1, '5-9': 6.2, '10-14': 6.8, '15-19': 6.7, '20-24': 6.8, '25-29': 7.2, '30-34': 6.5, '35-39': 6.3, '40-44': 6.0, '45-49': 6.0, '50-54': 5.8, '55-59': 6.0, '60-64': 6.1, '65-69': 5.5, '70-74': 4.7, '75-79': 3.4, '80-84': 2.1, '85+': 1.9}, 'usa-florida': {'0-5': 5.3, '5-9': 5.3, '10-14': 5.8, '15-19': 5.8, '20-24': 5.9, '25-29': 6.7, '30-34': 6.3, '35-39': 6.2, '40-44': 5.9, '45-49': 6.3, '50-54': 6.5, '55-59': 6.8, '60-64': 6.6, '65-69': 6.1, '70-74': 5.2, '75-79': 3.9, '80-84': 2.6, '85+': 2.6}, 'usa-massachusetts': {'0-5': 5.2, '5-9': 5.4, '10-14': 5.7, '15-19': 6.6, '20-24': 7.1, '25-29': 7.3, '30-34': 7.0, '35-39': 6.3, '40-44': 5.9, '45-49': 6.4, '50-54': 6.9, '55-59': 7.1, '60-64': 6.5, '65-69': 5.3, '70-74': 4.2, '75-79': 2.8, '80-84': 1.9, '85+': 2.2}, 'usa-district of columbia': {'0-5': 6.5, '5-9': 4.7, '10-14': 4.8, '15-19': 5.3, '20-24': 7.5, '25-29': 11.7, '30-34': 11.5, '35-39': 9.0, '40-44': 6.0, '45-49': 5.6, '50-54': 5.2, '55-59': 5.2, '60-64': 4.7, '65-69': 3.7, '70-74': 3.3, '75-79': 2.3, '80-84': 1.4, '85+': 1.6}, 'usa-utah': {'0-5': 7.9, '5-9': 8.1, '10-14': 8.6, '15-19': 7.9, '20-24': 8.2, '25-29': 7.8, '30-34': 6.9, '35-39': 7.2, '40-44': 6.7, '45-49': 5.5, '50-54': 4.6, '55-59': 4.8, '60-64': 4.7, '65-69': 3.8, '70-74': 2.9, '75-79': 1.9, '80-84': 1.4, '85+': 1.1}, 'usa-new york': {'0-5': 5.8, '5-9': 5.5, '10-14': 5.9, '15-19': 6.2, '20-24': 6.6, '25-29': 7.6, '30-34': 7.1, '35-39': 6.5, '40-44': 6.0, '45-49': 6.3, '50-54': 6.8, '55-59': 6.8, '60-64': 6.5, '65-69': 5.1, '70-74': 4.2, '75-79': 2.9, '80-84': 2.0, '85+': 2.2}}

    return data
