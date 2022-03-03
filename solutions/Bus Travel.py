num_stops = int(input())
bus_stops = [input() for stop in range(num_stops)]
# bus_stops = ["A B | -", "C | -", "- | A B", "- | C"]
src_des_stops = [s for stop in bus_stops for s in stop.split(" | ")]
# print(src_des_stops)
src_stops = [stop for i, stop in enumerate(src_des_stops) if i % 2 == 0]
des_stops = [stop for i, stop in enumerate(src_des_stops) if i % 2 != 0]
# print(src_stops, des_stops)
passengers = [p for p in "".join(src_stops) if p.isalpha()]
src_gn = [str(i+1) for p in passengers for i, src in enumerate(src_stops) if p in src]
des_gn = [str(i+1) for p in passengers for i, des in enumerate(des_stops) if p in des]
# print(passengers, src_gn, des_gn)
num_tickets = int(input())
tickets = [input() for stop in range(num_tickets)]
# tickets = ["1 3", "1 2", "2 3"]
src_des_tickets = [s for stop in tickets for s in stop.split(" ")]
# print(src_des_tickets)
src_crt = [stop for i, stop in enumerate(src_des_tickets) if i % 2 == 0]
des_crt = [stop for i, stop in enumerate(src_des_tickets) if i % 2 != 0]
# print(src_crt, des_crt)
result = [[p, gs, cs, gd, cd] for p, gs, cs, gd, cd in zip(passengers, src_gn, src_crt, des_gn, des_crt)]
# print(result)
for res in result:
    if res[1] == res[2] and res[3] == res[4]:
        now = res[0] + " " + res[2] + " " + res[4] + " UT"
    else:
        now = res[0] + " " + res[2] + " " + res[4] + " OT"
    print(now)
