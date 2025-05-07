import numpy as np
import matplotlib.pyplot as plt

# Create 5000 fake customer ratings using a normal distribution. 
# Average(mean) is 7.5 with spread (standard deviation) is 2.4.
ratings = np.random.normal(loc=7.5, scale=2.4, size=5000)

# Make sure all ratings are between 1 and 10
ratings = np.clip(ratings, 1, 10)
# print(ratings[:10])

# Calculate basic statistics
mean = np.mean(ratings) # The average rating
std = np.std(ratings) # How different the ratings are
cv = (std / mean) * 100 # Variation compared to the average (in percent)

# Show results in terminal
print("Mean:", round(mean, 2))
print("Standard deviation:", round(std, 2))
print("CV:", round(cv, 1), "%")

# Draw chart of ratings
plt.hist(ratings, bins=20, color='skyblue', edgecolor='black')
plt.title("Customer Satisfaction - Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Users")
plt.savefig("rating_histogram.png")
plt.close()

# Calculate z-scores (how far from mean)
z_scores = (ratings - mean) / std

# Draw a chart of z-scores
plt.hist(z_scores, bins=30, color='salmon', edgecolor='black')
plt.title("Z-score Distribution")
plt.xlabel("Z-score")
plt.ylabel("Number of Users")
plt.axvline(-1.5, color='red', linestyle='--', label='Dissatisfied group')
plt.axvline(1.5, color='green', linestyle='--', label='Loyal group')
plt.legend()
plt.savefig("zscore_histogram.png")
plt.close()