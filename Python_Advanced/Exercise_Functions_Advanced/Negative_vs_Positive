def nums_sum(*args):
    negative_sum = 0
    positive_sum = 0

    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num

    return negative_sum, positive_sum

nums = map(int, input().split())
neg_sums, poss_sums= nums_sum(*nums)

print(neg_sums)
print(poss_sums)

if abs(neg_sums) > poss_sums:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
