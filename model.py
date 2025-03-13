def get_percent_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def normalize(a, b):
    total = a + b
    if total == 0:
        return 0.5, 0.5
    return a / total, b / total

# Collect inputs
print("Please enter the following data for Team 1 and Team 2.")
team1_name = input("Enter Team 1 name: ")
team2_name = input("Enter Team 2 name: ")

# 1. Ranking positions
team1_rank = int(input(f"\nEnter {team1_name}'s ranking position in their group: "))
team2_rank = int(input(f"Enter {team2_name}'s ranking position in their group: "))

# 2. Head-to-head statistics
print("\nEnter head-to-head statistics (must sum to 100%):")
h2h_team1 = get_percent_input(f"{team1_name} Win%: ")
h2h_draw = get_percent_input("Draw%: ")
h2h_team2 = get_percent_input(f"{team2_name} Win%: ")
if abs(h2h_team1 + h2h_draw + h2h_team2 - 100) > 0.001:
    raise ValueError("Head-to-head percentages must sum to 100%.")

# 3. Injuries and suspensions
team1_injuries = int(input(f"\nEnter number of injured/suspended players for {team1_name}: "))
team2_injuries = int(input(f"Enter number of injured/suspended players for {team2_name}: "))

# 4. Recent performance (last 6 matches)
print(f"\nEnter {team1_name}'s recent performance (last 6 matches):")
team1_win = get_percent_input("Win%: ")
team1_draw = get_percent_input("Draw%: ")
team1_loss = get_percent_input("Loss%: ")
if abs(team1_win + team1_draw + team1_loss - 100) > 0.001:
    raise ValueError("Recent performance percentages must sum to 100%.")

print(f"Enter {team2_name}'s recent performance (last 6 matches):")
team2_win = get_percent_input("Win%: ")
team2_draw = get_percent_input("Draw%: ")
team2_loss = get_percent_input("Loss%: ")
if abs(team2_win + team2_draw + team2_loss - 100) > 0.001:
    raise ValueError("Recent performance percentages must sum to 100%.")

# 5. Home/Away performance
print(f"\nEnter {team1_name}'s home performance (last 6 home matches):")
team1_home_win = get_percent_input("Win%: ")
team1_home_draw = get_percent_input("Draw%: ")
team1_home_loss = get_percent_input("Loss%: ")
if abs(team1_home_win + team1_home_draw + team1_home_loss - 100) > 0.001:
    raise ValueError("Home performance percentages must sum to 100%.")

print(f"Enter {team2_name}'s away performance (last 6 away matches):")
team2_away_win = get_percent_input("Win%: ")
team2_away_draw = get_percent_input("Draw%: ")
team2_away_loss = get_percent_input("Loss%: ")
if abs(team2_away_win + team2_away_draw + team2_away_loss - 100) > 0.001:
    raise ValueError("Away performance percentages must sum to 100%.")

# 6. Total matches played (not used in calculation as per problem statement)
team1_matches = int(input(f"\nEnter total matches played by {team1_name}: "))
team2_matches = int(input(f"Enter total matches played by {team2_name}: "))

# 7. Goals statistics
team1_goals_scored = int(input(f"\nEnter goals scored by {team1_name}: "))
team1_goals_conceded = int(input(f"Enter goals conceded by {team1_name}: "))
team2_goals_scored = int(input(f"Enter goals scored by {team2_name}: "))
team2_goals_conceded = int(input(f"Enter goals conceded by {team2_name}: "))

# 8. Shooting statistics
team1_total_shots = int(input(f"\nEnter total shots by {team1_name}: "))
team1_blocked_shots = int(input(f"Enter blocked shots by {team1_name}: "))
team2_total_shots = int(input(f"Enter total shots by {team2_name}: "))
team2_blocked_shots = int(input(f"Enter blocked shots by {team2_name}: "))

# 9. Passing statistics
team1_total_passes = int(input(f"\nEnter total passes by {team1_name}: ").replace(',', ''))
team1_accurate_passes = int(input(f"Enter accurate passes by {team1_name}: ").replace(',', ''))
team1_possession = get_percent_input(f"Enter ball possession% for {team1_name}: ")
team2_total_passes = int(input(f"Enter total passes by {team2_name}: ").replace(',', ''))
team2_accurate_passes = int(input(f"Enter accurate passes by {team2_name}: ").replace(',', ''))
team2_possession = get_percent_input(f"Enter ball possession% for {team2_name}: ")

# 10. Total attacks
team1_attacks = int(input(f"\nEnter total attacks by {team1_name}: ").replace(',', ''))
team2_attacks = int(input(f"Enter total attacks by {team2_name}: ").replace(',', ''))

# 11. Dangerous attacks
team1_dangerous_attacks = int(input(f"\nEnter dangerous attacks by {team1_name}: ").replace(',', ''))
team2_dangerous_attacks = int(input(f"Enter dangerous attacks by {team2_name}: ").replace(',', ''))

# Weights for each factor
weights = {
    'ranking': 0.05,
    'h2h': 0.3,
    'injuries': 0.1,
    'recent_form': 0.1,
    'home_away': 0.05,
    'goals': 0.1,
    'shots': 0.05,
    'passing': 0.05,
    'attacks': 0.05,
    'dangerous_attacks': 0.05,
}

# Calculate contributions for each factor
# 1. Ranking
team1_rank_score = 1 / team1_rank
team2_rank_score = 1 / team2_rank
n1, n2 = normalize(team1_rank_score, team2_rank_score)
contrib_rank_team1 = n1 * weights['ranking']
contrib_rank_team2 = n2 * weights['ranking']

# 2. H2H
contrib_h2h_team1 = (h2h_team1 / 100) * weights['h2h']
contrib_h2h_team2 = (h2h_team2 / 100) * weights['h2h']
contrib_h2h_draw = (h2h_draw / 100) * weights['h2h']

# 3. Injuries
team1_inj_score = 1 / (team1_injuries + 1)
team2_inj_score = 1 / (team2_injuries + 1)
n1, n2 = normalize(team1_inj_score, team2_inj_score)
contrib_inj_team1 = n1 * weights['injuries']
contrib_inj_team2 = n2 * weights['injuries']

# 4. Recent Form
team1_form = (team1_win + 0.5 * team1_draw) / 100
team2_form = (team2_win + 0.5 * team2_draw) / 100
n1, n2 = normalize(team1_form, team2_form)
contrib_form_team1 = n1 * weights['recent_form']
contrib_form_team2 = n2 * weights['recent_form']

# 5. Home/Away
team1_home = (team1_home_win + 0.5 * team1_home_draw) / 100
team2_away = (team2_away_win + 0.5 * team2_away_draw) / 100
n1, n2 = normalize(team1_home, team2_away)
contrib_home_away_team1 = n1 * weights['home_away']
contrib_home_away_team2 = n2 * weights['home_away']

# 6. Goals
team1_goal_diff = team1_goals_scored - team1_goals_conceded
team2_goal_diff = team2_goals_scored - team2_goals_conceded
n1, n2 = normalize(team1_goal_diff, team2_goal_diff)
contrib_goals_team1 = n1 * weights['goals']
contrib_goals_team2 = n2 * weights['goals']

# 7. Shots
team1_shots_ratio = (team1_total_shots - team1_blocked_shots) / team1_total_shots if team1_total_shots != 0 else 0
team2_shots_ratio = (team2_total_shots - team2_blocked_shots) / team2_total_shots if team2_total_shots != 0 else 0
n1, n2 = normalize(team1_shots_ratio, team2_shots_ratio)
contrib_shots_team1 = n1 * weights['shots']
contrib_shots_team2 = n2 * weights['shots']

# 8. Passing
team1_acc_pass_percent = (team1_accurate_passes / team1_total_passes * 100) if team1_total_passes != 0 else 0
team2_acc_pass_percent = (team2_accurate_passes / team2_total_passes * 100) if team2_total_passes != 0 else 0
team1_passing_score = (team1_acc_pass_percent + team1_possession) / 2
team2_passing_score = (team2_acc_pass_percent + team2_possession) / 2
n1, n2 = normalize(team1_passing_score, team2_passing_score)
contrib_passing_team1 = n1 * weights['passing']
contrib_passing_team2 = n2 * weights['passing']

# 9. Attacks
n1, n2 = normalize(team1_attacks, team2_attacks)
contrib_attacks_team1 = n1 * weights['attacks']
contrib_attacks_team2 = n2 * weights['attacks']

# 10. Dangerous Attacks
n1, n2 = normalize(team1_dangerous_attacks, team2_dangerous_attacks)
contrib_dangerous_team1 = n1 * weights['dangerous_attacks']
contrib_dangerous_team2 = n2 * weights['dangerous_attacks']

# Sum contributions
team1_total = (
    contrib_rank_team1 +
    contrib_h2h_team1 +
    contrib_inj_team1 +
    contrib_form_team1 +
    contrib_home_away_team1 +
    contrib_goals_team1 +
    contrib_shots_team1 +
    contrib_passing_team1 +
    contrib_attacks_team1 +
    contrib_dangerous_team1
)

team2_total = (
    contrib_rank_team2 +
    contrib_h2h_team2 +
    contrib_inj_team2 +
    contrib_form_team2 +
    contrib_home_away_team2 +
    contrib_goals_team2 +
    contrib_shots_team2 +
    contrib_passing_team2 +
    contrib_attacks_team2 +
    contrib_dangerous_team2
)

draw_total = contrib_h2h_draw

total = team1_total + team2_total + draw_total

# Calculate probabilities
prob_team1 = (team1_total / total) * 100
prob_team2 = (team2_total / total) * 100
prob_draw = (draw_total / total) * 100

# Determine prediction
max_prob = max(prob_team1, prob_team2, prob_draw)
if max_prob == prob_team1:
    prediction = f"{team1_name} Win"
elif max_prob == prob_team2:
    prediction = f"{team2_name} Win"
else:
    prediction = "Draw"

# Display results
print("\nPrediction Results:")
print(f"1. Final Score Prediction: {team1_name} vs {team2_name} - {prediction}")

if prediction == "Draw":
    print(f"2. Draw Probability: {prob_draw:.0f}% chance of a draw.")
else:
    winning_team = prediction.split()[0]
    win_prob = prob_team1 if winning_team == team1_name else prob_team2
    print(f"2. Win Probability: {winning_team} has a {win_prob:.0f}% chance of victory.")
