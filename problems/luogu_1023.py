import math

def main():
    target_price = int(input())
    cost, cost_sales = map(int, input().split())
    price_sales = [(cost, cost_sales)]
    
    while True:
        line = input().strip()
        if line == '-1 -1':
            break
        price, sales = map(int, line.split())
        price_sales.append((price, sales))
    price_sales.sort()
    decrease_rate = int(input())
    
    def get_sales(p):
        if p < cost:
            return 0
        for i in range(len(price_sales) - 1):
            a, a_sales = price_sales[i]
            b, b_sales = price_sales[i+1]
            if a <= p <= b:
                delta_sales = b_sales - a_sales
                delta_price = b - a
                return a_sales + (p - a) * delta_sales // delta_price
        last_price, last_sales = price_sales[-1]
        sales = last_sales - decrease_rate * (p - last_price)
        return max(0, sales)
    
    p_list = []
    p = cost
    while True:
        sales = get_sales(p)
        if sales <= 0:
            break
        p_list.append(p)
        p += 1
    
    if target_price not in p_list:
        print("NO SOLUTION")
        return
    
    S_target = get_sales(target_price)
    t_min = -float('inf')
    t_max = float('inf')
    
    for p in p_list:
        if p == target_price:
            continue
        S_p = get_sales(p)
        
        if S_target > S_p:
            numerator = (p - cost) * S_p - (target_price - cost) * S_target
            denominator = S_target - S_p
            if denominator == 0:
                continue
            lower = numerator / denominator
            if denominator > 0:
                t_min = max(t_min, math.ceil(lower))
            else:
                t_max = min(t_max, math.floor(lower))
        elif S_target < S_p:
            numerator = (p - cost) * S_p - (target_price - cost) * S_target
            denominator = S_target - S_p
            if denominator == 0:
                continue
            upper = numerator / denominator
            t_max = min(t_max, math.floor(upper))
        else:
            if (target_price - cost) < (p - cost):
                print("NO SOLUTION")
                return
        
        if t_min > t_max:
            print("NO SOLUTION")
            return
    
    if t_min > t_max:
        print("NO SOLUTION")
        return
    
    if t_min <= 0 <= t_max:
        best_t = 0
    elif t_max < 0:
        best_t = t_max
    else:
        best_t = t_min
    
    if best_t < t_min or best_t > t_max:
        print("NO SOLUTION")
    else:
        print(int(best_t))

if __name__ == "__main__":
    main()