from imperial import Imperial

def input_dimentions(): #rise, run, target_height, target_depth, tread_thickness
    valid_target_height = False
    valid_target_depth = False
    print("For archetectural input, use this format:")
    print("""4' 9" 3/16""")
    rise = input(f"What is the dimension of the rise?\n: ")
    ri = Imperial(rise)
    f_rise = ri.convert_from_arch(rise)
    print(f_rise)

    run = input(f"What is the dimension of the run?\n: ")
    ru = Imperial(run)
    f_run = ru.convert_from_arch(run) 
    print(f_run)
        
    while valid_target_height == False:
        target_height = input(f'What is the target height of the stairs?\n(Source: IBC §1009.7.2, A-Mezz) 4-7":')
        he = Imperial(target_height)
        f_height = he.convert_from_arch(target_height)
        print(f_height)
        if f_height > 4:
            if f_height < 7:
                break

    while valid_target_depth == False:
        target_depth = input(f'What is the target depth of the stairs?\n((Source: IBC §1009.7.2, A-Mezz) 11" minimum:')
        de = Imperial(target_depth)
        f_depth = de.convert_from_arch(target_depth)
        print(f_depth)
        if f_depth > 11:
            if f_depth > 84:
                print("The maximum slope for a ramp is 8.33%\n (Source: IBC 1012.2 and ICC A117.1-2017)")
            elif f_depth < 84:
                break

    tread_thickness = input(f"How thick is the material for the treads?\n:")
    tr = Imperial(tread_thickness)
    f_tread = tr.convert_from_arch(tread_thickness)
    print(f_tread)


    return (f_rise, f_run, f_height, f_depth, f_tread)
