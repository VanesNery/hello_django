# Meu Primeiro Projeto em Django

## Indice
1. [Como criar um ambiente virtual (pyenv)?](pyenv)
2. [Como ativa o ambiente virtual?](ativa)
3. [Como instalar o Django?](Django) 
4. [Como criar um projeto?](criar)
5. [Como startar um projeto?](startar)
6. [Como escolher o interpretador no VsCode?](VsCode)
7. [Como rodar o projeto?](rodar)

* * * 

Os passos abaixo vai auxiliar você na criação de um ambiente virtual, porém antes de começar, precisa ter instalado em sua maquina:

* Vscode
* Python
* Pyenv

* Como criar um ambiente virtual (pyenv)?  
  
  ~~~
   pyenv virtualenv versão nome_do_projeto 
   ~~~

* Como ativa o ambiente virtual?  

  ~~~
  pyenv activate nome_do_projeto
  ~~~

* Como instalar o Django?  
  
  ~~~
  pip install django
  ~~~

* Como criar um projeto?  
Nesse passo vocẽ vai escolher o lugar onde deseja salvar e verificar as libs instaladas  
  
  ~~~
  cd diretorio/onde/deseja/salvar 
  pip freeze
  ~~~

* Como startar um projeto?  
Nesse momento você vai dá o start no projeto e vai ser criada uma pasta no diretório escolhido no passo anterior

    ~~~
    django-admin startproject nome_do_projeto_será_inicializado_pode_ser_outro_nome
    ~~~

* Como escolher o interpretador no VsCode?  
  
  Abra o projeto no vscode, se você não souber como fazer isso via terminal, basta:
  
  ~~~
  code nome_do_projeto
  ~~~

  Com o Vscode aberto, aperte essas teclas:

  ~~~
  CRTL + SHIFT + P
  ~~~

  Vai aparece uma barra na parte superior do software, basta digitar:
    
    ~~~
    > Python: Select Interpreter
    ~~~

  Vai mostrar uma lista de opções e clicar na opção desejada, você vai percebe um diretório no seu projeto chamado **.vscode**. Nele vai consta o "settings e o launch"

  No **Settings** terá a configuração do seu projeto.
  No **Launch** terá a forma de debugar ou executar o seu projeto.

* Como rodar o projeto?  
  
  É possível rodar seu projeto sem ter criado o launch antes, utilizado o comando:

  ~~~python 
  python manage.py runserver
  ~~~

  Para criar o launch, vá na opção de **Run**, clique na opção de **_create launch.json_**, ele já vem com algumas coisas configuradas, no meu caso eu tirei a opção _noreload_. O nome já diz, se ele tiver nos paramentos o projeto não será recarregado quando você estiver fazendo as mudanças, será necessário rodar o projeto novamente.

 Espero que vocês tenham gostado do tutorial  :facepunch: :kissing_heart:
  
