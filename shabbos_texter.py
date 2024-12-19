from whatsapp_messenger import WhatsappMessenger
import time

def send_texts(filename: str) -> None:
    whatsapp_texter = WhatsappMessenger()
    whatsapp_texter.wait_for_qr_scan()
    print('starting texts...')
    with open(filename,'r') as file:
        for line in file:
            info = line.split(',')
            if(info[0]=='name'):
                continue
            if(info[0]=='end'):
                time.sleep(1.5)
                break
            phone_number = info[1]
            name = info[0]
            shabbos_text = input(f"{name}: ")
            if(shabbos_text == 's'):
                print(f'skipping {name}')
                continue
            if(shabbos_text == 'q'):
                break
            whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)

    print('finished with texts!')
            
def main():
    choice = input('enter an option (thursday,friday,all,custom,middle,quit) (t/f/a/c/m/q): ')
    if(choice=='t'):
        send_texts(filename='thursday_names.csv')
    elif(choice=='f'):
        send_texts(filename='friday_names.csv')
    elif(choice=='a'):
        send_texts(filename='all_names.csv')
    elif(choice == 'c'):
        whatsapp_texter = WhatsappMessenger()
        names = input("enter the people you would like to text, separated by commas: ")
        name_list = names.split(',')
        with open('all_names.csv', 'r') as file:
            for line in file:
                info = line.split(',')
                if(info[0]=='name'):
                    continue
                if(info[0]=='end'):
                    time.sleep(1.5)
                    break
                name = info[0]
                if name not in name_list:
                    print(name)
                    time.sleep(0.01)
                    continue
                phone_number = info[1]
                shabbos_text = input(f"{name}: ")
                if(shabbos_text == 's'):
                    print(f'skipping {name}')
                    continue
                if(shabbos_text == 'q'):
                    break
                whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)
            print('done with custom list!')
    elif(choice=='m'):
        starting_name = input("Enter a name to begin with: ")
        whatsapp_texter = WhatsappMessenger()
        whatsapp_texter.wait_for_qr_scan()
        with open('all_names.csv', 'r') as file:
            for line in file:
                info = line.split(',')
                name = info[0]
                if(name == 'name'):
                    continue
                if(name == 'end'):
                    time.sleep(1.5)
                    break
                if name != starting_name:
                    print(name)
                    time.sleep(0.01)
                    continue
                phone_number = info[1]
                shabbos_text = input(f"{name}: ")
                if(shabbos_text == 's'):
                    print(f'skipping {name}')
                    continue
                if(shabbos_text == 'q'):
                    break
                whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)
                break
            for line in file:
                info = line.split(',')
                if(info[0]=='name'):
                    continue
                if(info[0]=='end'):
                    time.sleep(1.5)
                    break
                phone_number = info[1]
                name = info[0]
                shabbos_text = input(f"{name}: ")
                if(shabbos_text == 's'):
                    print(f'skipping {name}')
                    continue
                if(shabbos_text == 'q'):
                    break
                whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)

    else:
        print('quitting')

if __name__ == '__main__':
    main()
