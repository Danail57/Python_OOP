from collections import deque

suggested_links = deque(map(int, input().split()))
featured_articles = list(map(int, input().split()))
target = int(input())

final_feed = []

while suggested_links and featured_articles:
    curr_suggested = suggested_links.popleft() # Take the first element from the Suggested Links
    curr_featured = featured_articles.pop() # Take the last element from the Featured Articles

    if curr_suggested == curr_featured:
        final_feed.append(0)
    elif curr_featured > curr_suggested:
        remainder = curr_featured % curr_suggested
        final_feed.append(remainder)

        if remainder != 0:
            featured_articles.append(remainder * 2)
    else:
        remainder = curr_suggested % curr_featured
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)

total_engagement_value = sum(final_feed)
print(f'Final Feed: {", ".join(map(str,final_feed))}')

if total_engagement_value >= target:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")
