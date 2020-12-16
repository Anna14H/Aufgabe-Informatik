import matplotlib.pyplot as plt

def Geschwindigkeit_Konstant (t):
    t = s/v
    return t
    
    
def Beschleunigung_Konstant (t):
    t = v/a
    return t
    
    
print ('Was willst du geplotet haben ? Beschleunigung oder Geschwindigkeit ? Für Beschleunigung gebe bitt a ein und für die Geschwindigkeit ein v.')

value = input().lower ()

if value == 'a':
    print ('Dann Brauchen wir jetzt noch eine Strecken Angabe in Meter und eine Geschwindigkeitangabe in m pro Sekunde von dir. \n Erste Eingabe ist s für Strecke in Meter. Zweite Eingabe ist v für die Geschwindigkeit in Meter pro Sekunde.')
    s = int(input())
    v = int(input())
    print (Beschleunigung_Konstant (t))
    xs = [0, t]
    ys = [0, a]

    plt.plot(xs, ys)
    plt.xlabel('Zeit in s')
    plt.ylabel('Beschleunigung in m/s^2')
    plt.show ()

    
elif value == 'v':
    print ('In diesen Fall benötigen wir noch die Beschleunigung in m pro Sekunde^2 und eine Geschwindigkeit in meter pro Sekunde. Input1= a Input zwei gleich v')
    a = int(input ())
    v = int(intPut ())
    print (Geschwindigkeit_Konstant (t))
    xs = [0, t]
    ys = [0, v]

    plt.plot(xs, ys)
    plt.xlabel('Zeit in s')
    plt.ylabel('Geschwindigkeit in m/s')
    plt.show ()

        
else:
    print ('Ungültigeeingabe')


    
