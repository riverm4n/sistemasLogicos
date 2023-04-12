#include <stdio.h>
#include <math.h>

double retorna_resultado_eq(double massa, double luz){
    double energia = massa * pow(luz, 2); // Função pow pertencente a biblioteca math.h

    return energia;
}

double retorna_massa(double energia, double luz){
    double massa = energia / pow(luz,2);

    return massa;
}

int retorna_massa_inteiro(double energia, double luz){
    int massa = energia / pow(luz,2);

    return massa;
}

int main(){
    /* Esta atividade prática tem como objetivo explorar os limites de representação dos tipos int, long int, float e double da linguagem C.
       Para tanto, resolva o seguinte problema:
        A lei fundamental da relatividade de Einstein relaciona massa e energia com a velocidade da luz:
        E = mC2
        Os valores são arbitrários e as unidades devem ser de acordo com o SI. A constante da velocidade da luz deve ser a mais precisa possível (pesquise o valor) e declare ela como double;
        Usando computação em ponto fixo (Complemento de 2) e flutuante (IEEE 754), apresente o resultado pedido para a lei fundamental da relatividade para uma máquina de 32 bits nos seguintes casos.
    */

   // Declaração das variáveis referentes a equação da lei fundamental da relatividade de Einstein:
   double energia, massa, luz;

   luz = 299792458; // Este é o valor conhecido para a constante da velocidade da luz, em metros por segund (m/s)

   // No padrão IEE754, é dito que quando usamos 64 bits, temos 1 bit pro sinal, 11 para o expoente e 52 para a mantissa, 
   // desta forma, o maior valor que uma variável double (que possui 64 bits) pode ter é a notada abaixo (confesso que para essa informação, precisei googlar, assim como o valor da constante da velocidade da luz)

   energia = 1.7976931348623157e+308;

   int massa_como_int = retorna_massa_inteiro(energia, luz);  

   printf("%d", massa_como_int);
   
   return 0;
}