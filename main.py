import random
import collections

res = random.choices(
    population=[[0,10], [10,30], [30, 40], [40,50], [50,60], [60,70], [70,80], [80,100]],
    weights=[0.05, 0.2, 0.3, 0.2, 0.1, 0.05, 0.025, 0.025],
    k=100)

res = sorted(collections.Counter(map(str,res)).items())
print(res)