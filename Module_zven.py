def usilitel(X, K):
    """Функция, описывающая работу усилителя,
где X - значение входного сигнала в текущий момент времени,
K - коэффициент усиления"""
    return X * K

def summator(X1, X2):
    """Функция, описывающая работу сумматора,
где X1 и X2 - сигналы на входе сумматора"""
    return X1 + X2

def inert_zveno(X,  Y, T):
    """Функция, описывающая работу инерционного звена,
где X - значение входного сигнала в текущий момент времени,
Y - значение выходного сигнала в предыдущий момент времени
T - постоянная времени"""
    return (X + Y * T) / (1+T)

def integrator(X, Y):
    """Функция, описывающая работу интегратора,
где X - значение входного сигнала в текущий момент времени,
Y - значение выходного сигнала в предыдущий момент времени"""
    return 0.001 * X + Y

def skhema(X, param, start):
    """Функция, описывающая работу всей системы автоматического регулирования,
где X - значение входного сигнала в текущий момент времени,
param - параметры системы,
start - нулевые начальные параметры"""
    Y_usil_K1 = usilitel(X, param[0]) #Выходной сигнал на усилителе с коэффициентом K1
    Y_usil_K7 = usilitel(X, param[6]) #Выходной сигнал на усилителе с коэффициентом K7
    Y_sum_1 = summator(Y_usil_K1, start[0]) #Выходной сигнал на 1 сумматоре
    Y_sum_2 = summator(Y_sum_1, start[1]) #Выходной сигнал на 2 сумматоре
    Y_usil_K2 = usilitel(Y_sum_2, param[1]) #Выходной сигнал на усилителе с коэффициентом K2
    Y_integ = integrator(Y_usil_K2, start[2]) #Выходной сигнал на интеграторе
    start[2] = Y_integ
    Y_usil_K5 = usilitel(Y_integ, param[4]) #Выходной сигнал на усилителе с коэффициентом K5
    start[1] = Y_usil_K5
    Y_usil_K3 = usilitel(Y_integ, param[2]) #Выходной сигнал на усилителе с коэффициентом K3
    Y_sum_3 = summator(Y_usil_K7, Y_usil_K3) #Выходной сигнал на 3 сумматоре
    Y_usil_K4 = usilitel(Y_sum_3, param[3]) #Выходной сигнал на усилителе с коэффициентом K4
    Y_inzv = inert_zveno(Y_usil_K4, start[3], param[7]) #Выходной сигнал на инерционном звене
    start[3] = Y_inzv
    Y_usil_K6 = usilitel(Y_inzv, param[5]) #Выходной сигнал на усилителе с коэффициентом K6
    start[0] = Y_usil_K6
    return Y_inzv
    
    
    
    
    
    

