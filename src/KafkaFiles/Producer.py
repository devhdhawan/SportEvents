import os
import sys
import os

# Add the parent directory of 'KafkaFiles' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from KafkaFiles.KafkaClientFactory import KafkaClientFactory
import threading
import time
import random

def simulate_innings(producer, topic, match_id, batting_team, bowling_team, max_overs=5,compareScore=False,chaseScore=0,bWickets=0):
    score = 0
    wickets = 0
    balls = 0
    total_balls = max_overs * 6
    overs = 0

    while balls < total_balls and wickets < 10:
        runs = random.choice([0,1,2,3,4,6])
        wicket_fell = random.random() < 0.1  # 10% chance of wicket per ball
        if wicket_fell:
            wickets += 1
        else:
            score += runs
        balls += 1

        if balls % 6 == 0:
            overs += 1


        
        event = {
                'match_id': match_id,
                'event_type': 'score_updates',
                'batting_team': batting_team,
                'bowling_team': bowling_team,
                'runs': runs,
                'overs': overs,
                'balls': balls,
                'batting_score': score,
                'batting_wickets': wickets,
                'bowling_score': chaseScore,
                'bowling_wickets': bWickets,
                'timestamp': time.time(),
                'chaseScore': chaseScore
            }
        

        
        producer.send(topic, event, key=match_id)
        print(f"Sent event: {event}")
        if(compareScore==True and score > chaseScore):
            print(f"{batting_team} won the match")
            break
        elif(compareScore==True and score == chaseScore and balls == total_balls):
            print(f"Match tied")
            break

        time.sleep(1)  # wait one second per ball to simulate live feed
    
    if(compareScore==True and score<chaseScore):
        print(f"{bowling_team} won the match")

    print(f"Innings over for {batting_team} with score {score}/{wickets}")
    return score,wickets


def simulate_match(producer,topic,match_id, teams_a,team_b):

    team_a_score, team_a_wickets= simulate_innings(producer,topic,match_id, teams_a, team_b,5,False,0,0)
    team_b_score,teams_b_wickets = simulate_innings(producer,topic,match_id, team_b, teams_a,5,True,team_a_score,team_a_wickets)

def main():
    bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    factory = KafkaClientFactory(bootstrap_servers=bootstrap_servers)
    producer = factory.create_producer()
    topic = 'Sports'

    matches = [
        ('INDvsAUS', 'IND', 'AUS'),
        ('ENGvsWI', 'ENG', 'WI'),
    ]

    threads = []
    for match_id, team_a, team_b in matches:
        t = threading.Thread(target=simulate_match, args=(producer, topic, match_id, team_a, team_b))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
