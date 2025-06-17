# Customer Satisfaction Analysis

This project analyzes customer satisfaction scores collected through a 10-point rating system.  
Although the average score seems high (around 7.5), the system showed signs of instability.  
To explore this, we applied basic statistical techniques to better understand the data.

Using key metrics like mean, standard deviation, coefficient of variation (CV), and z-scores,  
we were able to identify patterns and segment users into different satisfaction groups.

---

## Key Concepts Used

- **Mean** – The average of all customer ratings
- **Standard Deviation** – Measures how much the ratings vary from the mean
- **Coefficient of Variation (CV)** – Shows how stable or unstable the system is
- **Z-score** – Detects users who are significantly more or less satisfied than average

---

## Outputs

- `rating_histogram.png` – Distribution of 5000 simulated customer ratings
- `zscore_histogram.png` – Z-score distribution with visual markers for dissatisfied and loyal segments

Example results:
- Mean: ~7.3  
- Standard Deviation: ~2.1  
- CV: ~28%

---

## How to Run

Make sure Python 3 is installed.

Then install the required libraries:

```bash
pip install numpy matplotlib
```

To run the script:

```bash
python customer_satisfaction_analysis.py
```

The code will print key statistics and generate two image files (`.png`) showing the analysis.

---

## Notes

This project is built using simulated data to demonstrate core statistical thinking.  
In a real-world scenario, this logic can be applied to actual customer feedback to detect early warning signals.


---

## 👩‍💻 About Me

I'm **Gülsarə Mirzəyeva**, transitioning into the field of data analytics and statistics.  
Through hands-on projects like this one, I aim to deepen my understanding of data interpretation, model evaluation, and visual storytelling using Python.

This project was created as part of my early exploration into applied statistics and aims to reflect both my learning journey and analytical thinking.

📫 [LinkedIn Profile](https://www.linkedin.com/in/gulsara-mirzayeva-298a3b359/)  
📧 Email: mirzayevagulsare@gmail.com
