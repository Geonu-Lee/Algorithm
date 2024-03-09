from itertools import product

def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    discount_list = list(product(discount, repeat=len(emoticons)))  # 모든 이모티콘 할인율 조합
    max_plus = 0
    max_money = 0
    for discount in discount_list:
        plus_users = 0
        sum_money = 0
        
        for user in users:
            user_discount, user_money = user
            money = 0
            for i in range(len(emoticons)):
                if discount[i] >= user_discount:
                    money += emoticons[i] * (1 - discount[i] / 100)
                
            if money >= user_money:
                plus_users += 1
            else:
                sum_money += money
                
        if plus_users > max_plus:
            max_plus = plus_users
            max_money = sum_money
        elif plus_users == max_plus and sum_money > max_money:
            max_money = sum_money
    
    return [max_plus, max_money]