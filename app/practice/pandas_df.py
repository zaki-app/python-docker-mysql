import random
import pandas as pd

def create_dummy_scores(n):
  scores = [
    dict(
      user_id=f"user{i+1}",
      subject=subject,
      score=random.randint(0,100)
    )
    for i in range(n)
    for subject in ("国語", "数学", "英語", "理科", "社会")
  ]
  
  return scores

scores = create_dummy_scores(5)
score_df = pd.DataFrame(scores)
print(score_df)

