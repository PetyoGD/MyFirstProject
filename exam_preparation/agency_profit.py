air_company = input()
tickets_adult = int(input())
tickets_kids = int(input())
net_price_adult = float(input())
service_price = float(input())
kinder_ticket = net_price_adult * 0.3
adult_tickets = tickets_adult * (net_price_adult + service_price)
kid_ticket = (kinder_ticket + service_price) * tickets_kids
all_price = (adult_tickets + kid_ticket) * 0.2
print(f"The profit of your agency from {air_company} tickets is {all_price:.2f} lv.")
