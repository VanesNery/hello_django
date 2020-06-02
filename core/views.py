from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello, {nome} de {idade} anos </h1>')

def calc(request, n1, n2):
    return HttpResponse(f'<h1>Bem vindo a Calculadora</h1> <p>A soma de {n1} + {n2} é: {n1+n2}</p> <p>A substração de {n1} - {n2} é: {n1 - n2}</p> <p>A Multiplicação de {n1} x {n2} é: {n1 * n2}</p> <p>A Divisão de {n1} / {n2} é: {n1 / n2}</p>')