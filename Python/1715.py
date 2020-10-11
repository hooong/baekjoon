# 1715번 카드 정렬하기
import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

bundle = []
while cards:
    if len(cards) == 1:
        break
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    heapq.heappush(cards, card1 + card2)
    bundle.append(card1+card2)

print(sum(bundle))
