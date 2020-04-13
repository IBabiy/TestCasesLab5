class Main():
    def __init__(self,x):

        while True:
            try:
                self.x = float(input("Введіть значеня Х в діапазоні x <= 36.868 або x >= 2.557: "))
                if (self.x <= 36.868 or self.x >= 2.557):
                    break
            except(ValueError):
                print('Введіть число! Invalid value')

    def outputting(self,x):

        print("Результат виразу y=x^4*4.769+x^3*4.159-x^2*2.745+x*4.503: ",
              (self.x)**4*4.769+(self.x)**3*4.159+(self.x)**2*2.745+(self.x)*4.503)
        print("Результат виразу y=x^3*2.027-x^2*2.578+x*6.966: ",
              (self.x)**3*2-(self.x)**2*2.578+(self.x)*6.966)
        print("Результат виразу y=x^2*1.575+x*3.894: ",
              (self.x)**2*1.575+x*3.894)
        print("Результат виразу y=x*2.644: ",
              (self.x)*2.664)

main = Main(1)
main.outputting(1)