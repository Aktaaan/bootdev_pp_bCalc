from imperial import Imperial

def input_dimentions(): #rise, run, target_height, target_depth, tread_thickness
    valid_target_height = False
    valid_target_depth = False
    print("For archetectural input, use this format:")
    print("""4' 9" 3/16""")
    #rise = input(f"What is the dimension of the rise?\n: ")
    rise = """4' 3" 3/16"""
    m = Imperial(rise)
    return m.convert_from_arch(rise)
    
'''
    run = input(f"What is the dimension of the run?\n: ")
        
    while valid_target_height == False:
        target_height = input(f'What is the target height of the stairs?\n(Source: IBC §1009.7.2, A-Mezz) 4-7":')
        if target_height > 4:
            if target_height < 7:
                break

    while valid_target_depth == False:
        target_depth = input(f'What is the target depth of the stairs?\n((Source: IBC §1009.7.2, A-Mezz) 11" minimum:')
        if target_depth > 11:
            if target_depth > 84:
                print("The maximum slope for a ramp is 8.33%\n (Source: IBC 1012.2 and ICC A117.1-2017)")
            elif target_depth < 84:
                break

    tread_thickness = input(f"How thick is the material for the treads?\n:")

    return (rise) #, run, target_height, target_depth, tread_thickness)
'''