import csv

# Data from the first CSV file should be read.
teams = {}
with open('input_sheet_1.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        team_name = row['Team Name']
        if team_name not in teams:
            teams[team_name] = {'members': [], 'statements': 0, 'reasons': 0}
        teams[team_name]['members'].append(row['User ID'])

# Data from the second CSV file is retrieved, and the teams dictionary is updated.
with open('input_sheet_2.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        uid = row['uid']
        total_statements = int(row['total_statements'])
        total_reasons = int(row['total_reasons'])
        for team in teams.values():
            if uid in team['members']:
                team['statements'] += total_statements
                team['reasons'] += total_reasons

# Calculate average statements and reasons for each team
for team in teams.values():
    num_members = len(team['members'])
    if num_members > 0:
        team['avg_statements'] = round(team['statements'] / num_members, 2)
        team['avg_reasons'] = round(team['reasons'] / num_members, 2)

# Sorting the teams based on common justifications and assertions
sorted_teams = sorted(teams.items(), key=lambda x: (x[1]['avg_statements'],
                                                    x[1]['avg_reasons']), reverse=True)

# Create a file with the output.
with open('user_leaderboard_1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team Rank', 'Thinking Teams Leaderboard', 'Average Statements', 'Average Reasons'])
    for i, (team_name, data) in enumerate(sorted_teams):
        avg_statements = data.get('avg_statements', 0)
        avg_reasons = data.get('avg_reasons', 0)
        writer.writerow([i+1, team_name, avg_statements, avg_reasons])

print("Output written to user_leaderboard_1.csv")
