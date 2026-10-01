import math

def calculate_egg_drop_steps(floors: int = 100):
    # 1. Հաշվում ենք անհրաժեշտ նվազագույն քայլերի քանակը (N)
    # N * (N + 1) / 2 >= floors
    # N^2 + N - 2*floors >= 0
    N = math.ceil((-1 + math.sqrt(1 + 8 * floors)) / 2)
    
    print(f"100 հարկի և 2 ձվի համար անհրաժեշտ է ընդամենը {N} քայլ:\n")
    print("Առաջին ձվի նետման հարկերի հերթականությունը.")
    
    current_floor = 0
    step = N
    step_count = 1
    
    # 2. Տպում ենք հարկերի հաջորդականությունը
    while current_floor < floors:
        current_floor += step
        if current_floor > floors:
            current_floor = floors
            
        print(f"Քայլ {step_count}: Նետել {current_floor}-րդ հարկից (քայլի չափը = {step})")
        
        step -= 1
        step_count += 1

calculate_egg_drop_steps(100)
