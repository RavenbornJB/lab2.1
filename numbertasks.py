import caprecar_nums, leyland_nums, lischrel_nums, trimorph_nums


functions = {'caprecar': caprecar_nums.caprecar_process,
             'leyland': leyland_nums.leyland_process,
             'lischrel': lischrel_nums.lischrel_process,
             'trimorph': trimorph_nums.trimorph_process
}

func = input('Please enter a type of number (caprecar, leyland, lischrel, trimorph)\nthat you would like to analyze: ')
if func in functions:
    result = functions[func]()
    print(result[0])
    print(result[1])
else:
    print('You have entered incorrect data. Terminating the program.')