# ========== Part 1 - Raw Tournament Data ====================================

# Raw player data with intentional inconsistencies (casing, spaces, etc.)
raw_players = [
    {"name": "  anna  ", "team": "alpha", "country": "sweden", "score": 1200, "matches": 15, "wins": 10, "active": True},
    {"name": "DAVID", "team": "BETA", "country": "sweden", "score": 950, "matches": 12, "wins": 4, "active": True},
    {"name": "sara", "team": "Alpha", "country": "SWEDEN", "score": 1430, "matches": 18, "wins": 14, "active": True},
    {"name": "Leo", "team": "gamma", "country": "finland", "score": 1100, "matches": 10, "wins": 6, "active": False},
    {"name": "  mAX ", "team": "beta", "country": "Finland", "score": 800, "matches": 8, "wins": 0, "active": True},
    {"name": "ELENA", "team": "GAMMA", "country": "norway", "score": 1350, "matches": 16, "wins": 11, "active": True},
    {"name": "john ", "team": "delta", "country": "Norway", "score": 600, "matches": 5, "wins": 1, "active": False},
    {"name": "  MIA", "team": "Delta", "country": "denmark", "score": 1050, "matches": 11, "wins": 7, "active": True},
    {"name": "alex", "team": "ALPHA", "country": "Denmark", "score": 900, "matches": 9, "wins": 3, "active": True},
    {"name": "Nora ", "team": "beta", "country": "sweden", "score": 1250, "matches": 14, "wins": 9, "active": True},
    {"name": "  LUKAS", "team": "gamma", "country": "germany", "score": 700, "matches": 6, "wins": 0, "active": False},
    {"name": "sophia", "team": "DELTA", "country": "Germany", "score": 1150, "matches": 13, "wins": 8, "active": True},
    {"name": "  oliver  ", "team": "alpha", "country": "norway", "score": 1300, "matches": 15, "wins": 12, "active": True},
    {"name": "EMMA", "team": "Beta", "country": "sweden", "score": 500, "matches": 4, "wins": 1, "active": False},
    {"name": "  karl", "team": "Gamma", "country": "FINLAND", "score": 1000, "matches": 10, "wins": 5, "active": True}
]

formatted_players = [
    {
        'name': player['name'].strip().title(),
        'team': player['team'].strip().title(),
        'country': player['country'].strip().title(),
        'score': player['score'],
        'matches': player['matches'],
        'wins': player['wins'],
        'active': player['active'],

    }
    for player in raw_players
]

active_players = [
    player
    for player in formatted_players
    if player['active'] 
]

top_wins_players = [
    player
    for player in formatted_players
    if player['wins'] >= 10
]

highest_scores_players = [
    player
    for player in formatted_players
    if player['score'] >= 1000
]

norway_delta_players = [
    player
    for player in formatted_players
    if player['country'] == 'Norway' and player['team'] == 'Delta'
]

# Part 4
unique_countries = set(
    player['country']
    for player in formatted_players
)

unique_teams = set(
    player['team']
    for player in formatted_players
)

name_score_dict = [
    {
        'name': player['name'],
        'score': player['score']
    }
    for player in formatted_players
]

name_wins_dict = [
    {
        'name': player['name'],
        'wins': player['wins']
    }
    for player in formatted_players
]


# Part 5
# Separate lists provided by tournament organizers
extra_player_names = ["Anna", "David", "Sara", "Leo", "Max"]
ranking_points = [1200, 950, 1430, 1100, 800]
sponsor_names = ["RedBull", "Logitech", "Razer", "Monster"] # len 4
player_ages = [22, 25, 19, 21, 28]

leaderboard = zip(extra_player_names, ranking_points)
for name, points in leaderboard:
    print(f"Name: {name}, \nPoints: {points}")

for name, age, points in zip(extra_player_names, player_ages, ranking_points):
    print(f"Name: {name}, \nAge: {age}, \nPoints: {points}")

for name, sponsor in zip(extra_player_names, sponsor_names):
    print(f"Player: {name}, \nSponsor: {sponsor}")


# Part 6
highest_score_rating = sorted(
    formatted_players,
    key=lambda player: player['score'],
    reverse=True
)
most_wins_rating = sorted(
    formatted_players,
    key=lambda player: player['wins'],
    reverse=True
)
most_matches_rating = sorted(
    formatted_players,
    key=lambda player: player['matches'],
    reverse=True
)
alphabetically_names_rating = sorted(
    formatted_players,
    key=lambda player: player['name']
)


# Part 7
print("TOURNAMENT LEADERBOARD")
for index, player in enumerate(highest_score_rating, start=1):
    print(f"{index}. {player['name']} - {player['score']} points")


# Part 8
# Which players belong to a particular team
gamma_players = [
    player['name']
    for player in formatted_players
    if player['team'] == 'Gamma'
]
# Which players have more than a chosen number of wins? as dictionary
low_score_players = {
    player['name']: player['score']
    for player in formatted_players
    if player['score'] <= 700
}
# Which countries are represented?
countries = {player['country'] for player in formatted_players}

# Which teams are represented in the tournament?
teams = {player['team'] for player in formatted_players}

# Active players who reached a score threshold
active_top_scorers = {
    player['name']: player['score']
    for player in formatted_players
    if player['active'] and player['score'] >= 1000
}


# Part 9
perfomance_players = [
    {
        'name': player['name'],
        'team': player['team'],
        'country': player['country'],
        'score': player['score'],
        'matches': player['matches'],
        'wins': player['wins'],
        'active': player['active'],
        'perfomance': player['score'] + (player['wins'] * 100) - (player['matches'] * 10)
    }
    for player in formatted_players
]
print(perfomance_players)

# 1. Rank players by performance (descending)
ranked_by_performance = sorted(
    perfomance_players,
    key=lambda player: player['perfomance'],
    reverse=True
)

# 2. Find top performers (top 3)
top_performers = ranked_by_performance[:3]

# 3. Filter players above a performance threshold (e.g. > 1200)
high_perf_players = [
    player for player in ranked_by_performance
    if player['perfomance'] > 1200
]

# 4. Map player names to performance values (dictionary)
performance_dict = {
    player['name']: player['perfomance']
    for player in perfomance_players
}


# Final Challenge - Tournament Analytics Report

print("=" * 50)
print("       FINAL TOURNAMENT ANALYTICS REPORT       ")
print("=" * 50)

# 1. Basic Stats
print(f"Total Players: {len(formatted_players)}")
print(f"Active Players: {len([player for player in formatted_players if player['active']])}")
print(f"Unique Teams ({len(teams)}): {', '.join(sorted(teams))}")
print(f"Unique Countries ({len(countries)}): {', '.join(sorted(countries))}\n")

# 2. Leaderboard by Score
print("--- RANKED BY SCORE ---")
for index, player in enumerate(highest_score_rating, start=1):
    print(f"{index}. {player['name']} ({player['team']}) - {player['score']} points")

# 3. Leaderboard by Wins
print("\n--- RANKED BY WINS ---")
for index, player in enumerate(most_wins_rating, start=1):
    print(f"{index}. {player['name']} - {player['wins']} wins")

# 4. Top 5 Performers
print("\n--- TOP 5 PERFORMERS ---")
top_5_perf = ranked_by_performance[:5]
for index, player in enumerate(top_5_perf, start=1):
    print(f"{index}. {player['name']} - Performance Rating: {player['perfomance']}")

# 5. Players above Performance Threshold (> 1200)
print("\n--- PLAYERS ABOVE PERFORMANCE THRESHOLD (> 1200) ---")
for player in high_perf_players:
    print(f"- {player['name']}: {player['perfomance']} rating")

# 6. Additional Analysis 1: Players with No Wins (0 wins)
zero_win_players = [player['name'] for player in formatted_players if player['wins'] == 0]
print(f"\n--- PLAYERS WITH NO WINS ---")
print(f"Players: {', '.join(zero_win_players) if zero_win_players else 'None'}")

# 7. Additional Analysis 2: Average Score in Tournament
avg_score = round(sum(player['score'] for player in formatted_players) / len(formatted_players), 2)
print(f"\n--- TOURNAMENT AVERAGE SCORE ---")
print(f"Average Score: {avg_score} points")

# 8. Additional Analysis 3: Highest Scoring Team (Total Points)
team_scores = {
    team: sum(player['score'] for player in formatted_players if player['team'] == team)
    for team in teams
}

best_team = None
highest_team_score = 0

for team, score in team_scores.items():
    if score > highest_team_score:
        highest_team_score = score
        best_team = team
print(f"\n--- TOP PERFORMING TEAM ---")
print(f"Team '{best_team}' with total score: {team_scores[best_team]} pts")
print("=" * 50)


