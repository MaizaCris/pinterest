# // for (int x = 0; x < 10; x++) {
# //     if ((1450 + x)&7==0) {
# //       print('''$x é solução''');
# //     }
# // }d

for n in range(10):
    if((1450+n)%7 == 0):
        print(n)