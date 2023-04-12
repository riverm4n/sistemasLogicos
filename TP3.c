#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <float.h>

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

int retorna_massa_inteiro_energia_inteiro(int energia, double luz){
    int massa = (int) energia / pow(luz, 2);

    return massa;
}

long int retorna_massa_longint_energia_inteiro(int energia, double luz){
    long int massa = (long int) energia/pow(luz, 2);

    return massa;
}

long int retorna_massa_longint_energia_longint(long int energia, double luz){
    long int massa = (long int) energia/pow(luz, 2);

    return massa;
}

float retorna_massa_float_energia_longint(long int energia, double luz){
    float massa = (float) energia/pow(luz, 2);

    return massa;
}

float retorna_massa_float_energia_float(float energia, double luz){
    float massa = (float) energia/pow(luz, 2);

    return massa;
}

double retorna_massa_double_energia_float(float energia, double luz){
    double massa = (double) energia/pow(luz, 2);

    return massa;
}

double retorna_massa_double_energia_double(double energia, double luz){
    double massa = energia/pow(luz, 2);

    return massa;
}

int execucao_atividade(double energia, double massa, double luz){
    printf("Esta é a execução do Trabalho Prático 3.\n Questão 1: Qual a massa associada à energia máxima representável pelos seguintes tipos:");
    printf("\n \t\t a) int Energia, int massa");
    printf("\n \t\t\t Valor da massa: %a", retorna_massa_inteiro_energia_inteiro(INT_MAX, luz));

    printf("\n\n \t\t b) int Energia, long int massa");
    printf("\n \t\t\t Valor da massa: %a", retorna_massa_longint_energia_inteiro(INT_MAX, luz));

    printf("\n\n \t\t c) long int Energia, long int massa");
    printf("\n \t\t\t Valor da massa: %a", retorna_massa_longint_energia_longint(LONG_MAX, luz));

    printf("\n\n \t\t d) long int Energia, float massa");
    printf("\n \t\t\t Valor da massa: %a", retorna_massa_float_energia_longint(LONG_MAX, luz));

    printf("\n\n \t\t e) float Energia, float massa");
    printf("\n \t\t\t Valor da massa: %a", retorna_massa_float_energia_float(FLT_MAX, luz));

    printf("\n\n \t\t f) double Energia, double massa");
    printf("\n \t\t\t Valor da massa: %a", retorna_massa_double_energia_float(DBL_MAX, luz));

    return 0;
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

   energia = DBL_MAX;

   execucao_atividade(energia, massa, luz);
   
   return 0;
}