# EDA on Indian_Restaurants
This project involves performing an EDA on a dataset of Indian restaurants to uncover insights and trends. The analysis covers various aspects such as restaurant chains, establishment types, cities, cuisines, ratings, and price distributions.
# Dataset
The dataset used for this analysis contains information about restaurants in India, including features such as restaurant ID, name, city, address, aggregate rating, votes, average cost for two, cuisines, and more.
# Installation
To run the analysis, you need to have Python and several libraries installed. Follow these steps to set up your environment:

## Clone the repository:
      git clone https://github.com/yourusername/indian-restaurants-eda.git
      cd indian-restaurants-eda

## Install the required libraries:
      pip install numpy pandas matplotlib seaborn

### Download the dataset and place it in the project directory.
Open the script file (eda_indian_restaurants.py).
##### Run the script :
       python eda_indian_restaurants.py

The script will perform various data preprocessing steps, generate visualizations, and provide insights based on the analysis.

# Project outline
### Importing 
### Preprocessing
-  Exploring data
-  Removing duplicates
-  Dealing with missing values
-  Omitting not useful 
### EDA
#### Restaurant Chains
- Chains vs Outlets
- Top Restaurant Chains (by number of outlets)
- Top Restaurant Chains (by average ratings)
#### Establishment Types
- Number of Restaurants 
- Average Rating, Votes, and Photo count
#### Cities
- Number of Restaurants 
- Average Rating, Votes, and Photo count
#### Cuisine
- Total number of unique cuisines
- Number of Restaurants
#### Rating and cost
- Average Cost for two distribution
- Relation between Average price for two and Rating
- Relation between Price Range and Rating

#  Conclusions
1- Approx. 35% of restaurants in India are part of some chain <br>
2- Domino's Pizza, Cafe Coffee Day, KFC are the biggest fast food chains in the country with most number of outlets <br>
3- Barbecues and Grill food chains have highest average ratings than other type of restaurants <br>
4- Quick bites and casual dining type of establishment have most number of outlets<br>
5- Establishments with alcohol availability have highest average ratings, votes and photo uploads<br>
6- Banglore has most number of restaurants <br>
7- Gurgaon has highest rated restaurants (average 3.83) whereas Hyderabad has more number of critics (votes). Mumbai and New Delhi dominates for most photo uploads per outlet<br>
8- After North Indian, Chinese is the 3rd most prefered cuisine in India<br>
9- International cuisines are better rated than local cuisines<br>
10- Gastro pub, Romantic Dining and Craft Beer features are well rated by customers<br>
11- Most restaurants are rated between 3 and 4<br>
12- Majority of restaurants are budget friendly with average cost of two between Rs.250 to Rs.800<br>
13- There are less number of restaurants at higher price ranges<br>
14- As the average cost of two increases, the chance of a restaurant having higher rating increases<br>
