print('Assalamu alaikum!!')
print()
print('This app will help you send money with the correct app that will benifit you')

taptapsendrate = float(input('What is today rate on Tap Tap send app? '))
taptapsendtax = float(input('What is the fee? '))

worldremitrate = float(input('What is today rate on World Remit app? '))
worldremittax = float(input('What is the fee? '))

sending = float(input("How much do you want to send? "))

TodaysRate = float(input("Today's rupees rate? "))

def TapTapSend():
    print()
    print('TapTap Send:')
    print()
    receive = taptapsendrate * sending
    send = taptapsendtax + sending
    receiveWithFee = (taptapsendrate + taptapsendtax) * sending
    actualRate = TodaysRate * sending
    print()
    print(f'Altogether by using Tap Tap Send, you will be sending £{send}. They receive ₹{receive}. With fee you should be receiving ₹{receiveWithFee}.')
    print()
    print(f"Actual rate is {TodaysRate} and they should receive without any app fee: ₹{actualRate}")
    print()
    print('Their benifit is ₹',actualRate - receiveWithFee)
    print()
    print('______________________________________________________________________________________________________________________________')
    print()

def worldRemit():
    print()
    print('Worldremit:')
    print()
    receive = worldremitrate * sending
    send = worldremittax + sending
    receiveWithFee = (worldremitrate + worldremittax) * sending
    actualRate = TodaysRate * sending
    print()
    print(f'Altogether by using Worldremit, you will be sending £{send}. They receive ₹{receive}. With fee you should be receiving ₹{receiveWithFee}.')
    print()
    print(f"Actual rate is ₹{TodaysRate} and they should receive without any app fee: ₹{actualRate}")
    print()
    print('Their benifit is ₹',receiveWithFee - actualRate)
    print()
    print('______________________________________________________________________________________________________________________________')
    print()

TapTapSend()
worldRemit()