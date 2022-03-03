G = int(input())
b_h = input()
B, H = [int(dem) for dem in b_h.split(" ")]
gold = input()
ingot = [int(length) for length in gold.split(" ")]
# print(ingot)
maximum = [val*B*H for val in ingot]
# print(maximum)

cuboid = [ingot[i:j] for i in range(0, G+1) for j in range(1, G+1) if i != j]
# print(cuboid)
minimum = [min(val)*len(val)*B*H for val in cuboid if val != []]
# print(minimum)

result = sum(maximum) - max(minimum)
print(result)
