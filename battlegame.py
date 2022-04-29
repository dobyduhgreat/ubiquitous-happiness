import time
wizard = 'Wizard'
elf = 'Elf'
human = 'Human'

wiz_hp = 70
elf_hp = 100
hum_hp = 150

wiz_dam = 150
elf_dam = 100
hum_dam = 20

dragon_hp = 300
dragon_dam = 50


while True:
    player_option = input(
        '1)    Wizard\n2)    Elf\n3)    Human\n\nChoose your Character: ')
    if player_option == '1':
        player_char = wizard
        player_hp = wiz_hp
        player_dam = wiz_dam
       # print(f'You have chose the Character: {player_char}')
        break
    elif player_option == '2':
        player_char = elf
        player_hp = elf_hp
        player_dam = elf_dam
       # print(f'You have chose the Character: {player_char}')
        break

    elif player_option == '3':
        player_char = human
        player_hp = hum_hp
        player_dam = hum_dam
       # print(f'You have chose the Character: {player_char}')
        break

    else:
        print('='*25 + '\n' + '='*25 + '\n' +
              '    INVALID SELECTION    \n\n     CHOOSE A NUMBER     \n'+'='*25 + '\n' + '='*25)
        continue
print(
    f'\nYou have chosen the Character:\n    {player_char}\n\nYou have:\n    {player_hp} Health Points\n    {player_dam} Damange Points')


while True:
    dragon_hp -= player_dam
    print(f'You struck the dragon for {player_dam}')
    if dragon_hp <= 0:
        print("\n\nIt's dead... It's fuckin' dead, man!\n\n")
        time.sleep(.6)
        print("\n\nCongratulations on Slaying th Dragon\n\n")
        time.sleep(.6)
        print("\n\nCredits:\n\n")
        time.sleep(.2)
        print("\n\nGame Written by:")
        time.sleep(.1)
        print("    Doby\n\n")
        time.sleep(.6)
        print("\n\nMusic by:")
        time.sleep(1.2)
        print("    ...there was no music...\n\n")
        time.sleep(.2)
        print("Thank you for playing!")
        break
    else:
        player_hp -= dragon_dam

        if player_hp <= 0:
            time.sleep(1)
            print('\nOOOF!!! That is rough. You ded.\n\n')
            play_again = input('Would you like to play again?\n')
            if play_again.lower() == 'yes' or play_again == 'y':
                continue
            else:
                break

        else:
            time.sleep(1)
            print(
                f"You were hit and suffered -{dragon_dam} damage!\nDon't worry. You still have {player_hp} hitpoints left")
            time.sleep(.5)
            continue
