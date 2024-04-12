cars_ = ['bmw', 'kia', 'lexus', 'audi', 'volvo']
for brend in cars_:
    cars = ['bmw', 'kia', 'lexus', 'audi', 'volvo']
    for brend in cars:
        print(f'Я езжу на автомобиле марки {brend.title()}')
        cars_count = 0
        for cars_count in range(0,5,2):
            cars_count += 10
            print(cars_count)

