Warning: This model has been developed solely for educational and learning purposes. Under no circumstances can it provide absolute certainty in predictions (at least for now). Here, I have translated mathematical calculations into code. The developer assumes no responsibility for your subsequent actions.

I have attempted to create a model that computes final outcomes based on statistical data entered by the user from https://www.forebet.com/.

---

# Match Outcome Prediction Model

This program predicts the outcome of a match between two teams by combining various performance factors. The prediction is based on a weighted sum of contributions from factors such as team ranking, head-to-head statistics, injuries, recent form, home/away performance, goals, shots, passing, and attacking play.

---

## Overview

1. **Input Collection:**  
   The program collects a range of inputs for each team, including:
   - **Team names and rankings:** Lower ranking numbers indicate a better position.
   - **Head-to-head (H2H) statistics:** Percentages for team1 wins, draws, and team2 wins (all summing to 100%).
   - **Player availability:** The number of injured or suspended players.
   - **Recent performance:** Win, draw, and loss percentages over the last 6 matches.
   - **Home/Away performance:** Win, draw, and loss percentages in home (for team1) and away (for team2) matches.
   - **Goals, shots, passing, and attacking metrics:** These include goals scored and conceded, shot data (total and blocked), passing data (total, accurate passes, and possession), and the numbers of attacks and dangerous attacks.

2. **Weights for Each Factor:**  
   Each factor is given a predetermined weight, and the sum of the weights equals 1.0. The weights are as follows:
   - Ranking: 0.05
   - Head-to-Head: 0.30
   - Injuries: 0.10
   - Recent Form: 0.10
   - Home/Away Performance: 0.05
   - Goals: 0.10
   - Shots: 0.05
   - Passing: 0.05
   - Attacks: 0.05
   - Dangerous Attacks: 0.05

---

## Mathematical Computations

For each factor, the program calculates a “score” or “contribution” for each team. A normalization function is used to compare two values by returning each value’s proportion of the total.

### 1. Ranking
- **Calculation:**  
  Each team’s ranking score is computed as the inverse of their ranking position:
  \[
  \text{score} = \frac{1}{\text{ranking position}}
  \]
  Lower ranking numbers (better performance) give a higher score.
- **Normalization:**  
  Let \(a\) and \(b\) be the two scores:
  \[
  n_1 = \frac{a}{a+b}, \quad n_2 = \frac{b}{a+b}
  \]
- **Contribution:**  
  Multiply each normalized score by the ranking weight (0.05):
  \[
  \text{contrib\_rank\_team1} = n_1 \times 0.05,\quad \text{contrib\_rank\_team2} = n_2 \times 0.05
  \]

---

### 2. Head-to-Head Statistics (H2H)
- **Input Percentages:**  
  The user provides winning percentages for team1 and team2, plus a draw percentage (all summing to 100).
- **Calculation:**  
  Each team's contribution is given by:
  \[
  \text{contrib\_h2h\_team} = \left(\frac{\text{H2H win percentage}}{100}\right) \times 0.30
  \]
  The draw contribution is:
  \[
  \text{contrib\_h2h\_draw} = \left(\frac{\text{H2H draw percentage}}{100}\right) \times 0.30
  \]

---

### 3. Injuries
- **Calculation:**  
  The injury score is computed as:
  \[
  \text{injury score} = \frac{1}{\text{injured players} + 1}
  \]
  This reduces the score as the number of injuries increases.
- **Normalization & Contribution:**  
  Normalize the scores between the two teams and multiply by the injuries weight (0.10).

---

### 4. Recent Form
- **Calculation:**  
  The performance score combines the win and draw percentages by giving half weight to draws:
  \[
  \text{form score} = \frac{\text{win\%} + 0.5 \times \text{draw\%}}{100}
  \]
- **Normalization & Contribution:**  
  Normalize the two teams’ form scores and multiply by the recent form weight (0.10).

---

### 5. Home/Away Performance
- **Calculation:**  
  - **Home performance (for team1):**
    \[
    \text{home score} = \frac{\text{home win\%} + 0.5 \times \text{home draw\%}}{100}
    \]
  - **Away performance (for team2):**
    \[
    \text{away score} = \frac{\text{away win\%} + 0.5 \times \text{away draw\%}}{100}
    \]
- **Normalization & Contribution:**  
  Normalize and then multiply by the home/away weight (0.05).

---

### 6. Goals
- **Calculation:**  
  The goal difference is computed as:
  \[
  \text{goal difference} = \text{goals scored} - \text{goals conceded}
  \]
- **Normalization & Contribution:**  
  Normalize the two teams’ goal differences and multiply by the goals weight (0.10).

---

### 7. Shots
- **Calculation:**  
  The shot efficiency (or quality) ratio is:
  \[
  \text{shots ratio} = \frac{\text{total shots} - \text{blocked shots}}{\text{total shots}}
  \]
  (If total shots is 0, the ratio is taken as 0.)
- **Normalization & Contribution:**  
  Normalize these ratios and multiply by the shots weight (0.05).

---

### 8. Passing
- **Calculation:**  
  First, compute the accurate pass percentage:
  \[
  \text{accurate pass\%} = \frac{\text{accurate passes}}{\text{total passes}} \times 100
  \]
  Then, create an overall passing score by averaging the accurate pass percentage with the ball possession percentage:
  \[
  \text{passing score} = \frac{\text{accurate pass\%} + \text{possession\%}}{2}
  \]
- **Normalization & Contribution:**  
  Normalize these passing scores and multiply by the passing weight (0.05).

---

### 9. Attacks
- **Calculation:**  
  Use the total number of attacks directly.
- **Normalization & Contribution:**  
  Normalize and multiply by the attacks weight (0.05).

---

### 10. Dangerous Attacks
- **Calculation:**  
  Use the dangerous attacks count directly.
- **Normalization & Contribution:**  
  Normalize and multiply by the dangerous attacks weight (0.05).

---

## Final Outcome Computation

After each factor has contributed a weighted score for both teams, the program computes:

1. **Total Score per Team:**  
   \[
   \text{team total} = \text{ranking} + \text{H2H} + \text{injuries} + \text{recent form} + \text{home/away} + \text{goals} + \text{shots} + \text{passing} + \text{attacks} + \text{dangerous attacks}
   \]
2. **Draw Contribution:**  
   The draw score is solely taken from the H2H draw contribution.
3. **Combined Total:**  
   \[
   \text{combined total} = \text{team1 total} + \text{team2 total} + \text{draw contribution}
   \]
4. **Probabilities:**  
   The program then calculates the probabilities for each outcome as:
   \[
   \text{Probability (Team1)} = \frac{\text{team1 total}}{\text{combined total}} \times 100
   \]
   \[
   \text{Probability (Team2)} = \frac{\text{team2 total}}{\text{combined total}} \times 100
   \]
   \[
   \text{Probability (Draw)} = \frac{\text{draw contribution}}{\text{combined total}} \times 100
   \]
5. **Prediction:**  
   The outcome (Team1 win, Team2 win, or Draw) is determined by which probability is the highest.

---

## Summary

- **Data Gathering:** The program collects detailed match-related statistics from the user.  
- **Weighting and Normalization:** Each performance metric is first weighted by its importance. When comparing metrics between two teams, the values are normalized so that each factor contributes to the overall score in a proportional way.  
- **Final Computation:** Total scores for team1, team2, and the possibility of a draw are computed. Their respective probabilities are then derived by comparing each score with the combined total of all scores.  
- **Outcome Determination:** The team (or draw) with the highest percentage is chosen as the predicted result for the match.

---


