# FPL Assistant Chatbot

## Overview

The FPL Assistant chatbot is currently in its development phase, hosted on Render at [FPL Assistant](https://fpl-assistant.onrender.com/chatbot/). It is designed to assist Fantasy Premier League (FPL) users with queries related to player stats, team stats, overall rank, and more. Currently, the chatbot handles basic interactions and displays data related to FPL.

## Testing Queries

Here are the testing questions to ensure the chatbot is working as expected:

### 1. **Get Player Stats**
   - **Query:** *"Give me stats of player: Haaland."*
   - **Expected Response:**
     - The chatbot should return the latest stats for Erling Haaland, including:
       - Goals scored
       - Assists
       - Appearances
       - Minutes played
       - Points
       - Yellow cards/red cards (if applicable)
     - Example Response:
       ```
       Player: Haaland
       - Goals: 18
       - Assists: 5
       - Appearances: 20
       - Minutes Played: 1600
       - Total Points: 120
       ```

### 2. **Get Overall Rank**
   - **Query:** *"Tell my overall rank."*
   - **Expected Response:**
     - The chatbot should retrieve and return the user's current overall rank in Fantasy Premier League.
     - Example Response:
       ```
       Your current overall rank is: 1,234 out of 8,000,000 players.
       ```

### 3. **Get Team Stats**
   - **Query:** *"Tell me my team stats."*
   - **Expected Response:**
     - The chatbot should return information related to the user's current Fantasy Premier League team, such as:
       - Total points
       - Current team value
       - Top-performing players
     - Example Response:
       ```
       Your team: FPL Masters
       - Total Points: 1,654
       - Team Value: £105.0m
       - Top Players: Haaland, Salah, Kane
       ```

### 4. **Get Player Transfer Information**
   - **Query:** *"Should I transfer out Son for Sterling?"*
   - **Expected Response:**
     - The chatbot should provide guidance or feedback based on recent player performance and team form.
     - Example Response:
       ```
       Transfer suggestion: Based on recent performances, Son has scored 5 points in the last 3 matches while Sterling has averaged 6.5. It might be a good move, but check for any injuries or upcoming fixtures.
       ```

### 5. **Fixture Information**
   - **Query:** *"What is the next fixture for Manchester City?"*
   - **Expected Response:**
     - The chatbot should retrieve the next fixture for the specified team.
     - Example Response:
       ```
       Next fixture for Manchester City:
       - Date: 2025-02-10
       - Opponent: Chelsea
       - Location: Home (Etihad Stadium)
       ```

## How to Test

1. **Access the chatbot**: Go to [FPL Assistant on Render](https://fpl-assistant.onrender.com/chatbot/).
2. **Input the queries**: Use the testing queries mentioned above.
3. **Verify Responses**: Check if the responses match the expected behavior and data for each query. If there are any discrepancies or errors, investigate the backend logic or data sources.

## Note:
Since the chatbot is in the development phase, some features may still be under construction or have mock data responses for testing purposes. Please report any issues with responses or data accuracy.
