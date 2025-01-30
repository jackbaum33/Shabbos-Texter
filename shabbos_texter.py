from whatsapp_messenger import WhatsappMessenger
from datetime import datetime
import time

def send_texts(filename: str) -> dict:
    results = {}
    results['total'] = 0
    results['smiley'] = 0
    results['exclamation'] = 0
    results['other'] = 0
    whatsapp_texter = WhatsappMessenger()
    whatsapp_texter.wait_for_qr_scan()
    print(f'starting texts at {datetime.now().strftime("%I:%M:%S %p")}:')
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
            results['total'] += 1
            last_char = shabbos_text[-1]
            if last_char == '!':
                results['exclamation'] += 1
            elif last_char == ')':
                results['smiley'] +=1
            else:
                results['other'] += 1
            whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)

    return results
            
def main():
    start_time = time.time()
    choice = input('enter an option (thursday,friday,all,custom,middle,quit) (t/f/a/c/m/q): ')
    if(choice=='t'):
        results = send_texts(filename='thursday_names.csv')
    elif(choice=='f'):
        results = send_texts(filename='friday_names.csv')
    elif(choice=='a'):
        results = send_texts(filename='all_names.csv')
    elif(choice == 'c'):
        whatsapp_texter = WhatsappMessenger()
        results = {}
        results['total'] = 0
        results['smiley'] = 0
        results['exclamation'] = 0
        results['other'] = 0
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
                results['total'] += 1
                last_char = shabbos_text[-1]
                if last_char == '!':
                    results['exclamation'] += 1
                elif last_char == ')':
                    results['smiley'] +=1
                else:
                    results['other'] += 1
                whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)

    elif(choice=='m'):
        starting_name = input("Enter a name to begin with: ")
        whatsapp_texter = WhatsappMessenger()
        whatsapp_texter.wait_for_qr_scan()
        results = {}
        results['total'] = 0
        results['smiley'] = 0
        results['exclamation'] = 0
        results['other'] = 0
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
                results['total'] += 1
                last_char = shabbos_text[-1]
                if last_char == '!':
                    results['exclamation'] += 1
                elif last_char == ')':
                    results['smiley'] +=1
                else:
                    results['other'] += 1
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
                results['total'] += 1
                last_char = shabbos_text[-1]
                if last_char == '!':
                    results['exclamation'] += 1
                elif last_char == ')':
                    results['smiley'] +=1
                else:
                    results['other'] += 1
                whatsapp_texter.send_text(body=shabbos_text,
                                      name=name,
                                      phone_number=phone_number)

    else:
        results = None
        print('quitting')
    
    print("-------------------------------")
    difference = time.time() - start_time
    num_hours = int(difference / 3600)
    difference %= 3600
    num_minutes = int(difference / 60)
    difference %= 60
    num_seconds = difference
    print('finished with texts!')
    print(f"time taken: {num_hours} hours, {num_minutes} minutes, {int(num_seconds)} seconds")
    print("Metrics:")
    if results is None:
        print('No texts were sent.')
    elif results['total'] == 0:
        print('No texts were sent.')
    else:
        smiley_ratio = float(results['smiley']/results['total']) * 100
        exclamation_ratio = float(results['exclamation']/results['total']) * 100
        other_ratio = float(results['other']/results['total']) * 100
        print(f"Number of texts sent: {results['total']}")
        print(f"Number of texts ending in a smiley face: {results['smiley']}/{results['total']} ({smiley_ratio:.2f}%)")
        print(f"Number of texts ending in an exclamation point: {results['exclamation']}/{results['total']} ({exclamation_ratio:.2f}%)")
        print(f"Number of texts ending in a different character: {results['other']}/{results['total']} ({other_ratio:.2f}%)")


if __name__ == '__main__':
    main()
