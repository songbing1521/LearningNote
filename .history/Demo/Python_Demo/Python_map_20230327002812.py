scores = {'songbing':95, '李元芳':78, '狄仁杰':82}
print(scores)
print(scores['狄仁杰'])
for key in scores:
    print(f'{key}:{scores[key]}')
scores.update(冷面 = 67, 方齐禾 = 85)
scores["诸葛亮"] = 15
print(scores)
print(scores.get('诸葛亮'))
print(scores.pop('songbing', 100))
print(scores)