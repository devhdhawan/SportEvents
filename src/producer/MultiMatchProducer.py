import threading
import time
import json
from kafka import KafkaProducer
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8')
)

topic = 'CricketEvent'

def simulate_innings(match_id, batting_team, bowling_team, max_overs=5,compareScore=False,chaseScore=0):
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
            'wickets': wickets,
            'overs': overs,
            'balls': balls,
            'score': score,
            'timestamp': time.time()
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
    return score


def simulate_match(match_id, teams_a,team_b):

    team_a_score = simulate_innings(match_id, teams_a, team_b,5,False,0)
    team_b_score = simulate_innings(match_id, team_b, teams_a,5,True,team_a_score)
    



if __name__ == "__main__":
    matches = [
        ('INDvsAUS', 'IND', 'AUS'),
        ('ENGvsWI', 'ENG', 'WI')
    ]
    threads = []
    for match in matches:
        t = threading.Thread(target=simulate_match, args=match)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
