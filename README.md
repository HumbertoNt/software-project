# Software Project  
Trabalho de Humberto para a disciplina de Projeto de Software.

## Introdução:  
O trabalho consiste em um portal para o professor e um para os alunos. Dentro de cada portal, encontram-se funcionalidades tanto para edição (geralmente apenas o professor pode editar) quanto para visualização.

### Próximos passos:
- Criar portal *admin master*.
- Melhorar e organizar ainda mais o código.
- Comentar cada funcionalidade.

**Coisas importantes:**
- Usuário professor: **admin_badu**
- Matrículas/id dos alunos:
  - **0001 João**
  - **0002 Maria**
  - **0003 Pedro**

## Funcionalidades:

### Student Enrollment  
A matrícula é realizada através do portal do professor, onde são adicionados os nomes dos alunos, suas turmas e as parcelas/mensalidades pagas. Ao realizar a matrícula, é gerado um número de quatro dígitos, que será o *ID* do aluno e servirá para outras funcionalidades.

### Class and Timetable Management  
O horário é semanal, seguindo 5 períodos. Não estão classificados por hora do dia, mas sim como *"one, two, three, four e five"*. Os horários podem ser editados pelos professores e visualizados pelos alunos, cada um em seu respectivo portal.

### Attendance Tracking  
A frequência dos alunos começa zerada, e no portal dos professores existe a possibilidade de registrar a frequência diária de cada aluno. Cada aluno pode consultar suas faltas no portal do aluno.

### Gradebook Management  
As notas seguem o modelo da *Universidade Federal de Alagoas* (UFAL), com as avaliações AB1 e AB2. Elas podem ser registradas no portal do professor, divididas entre alunos e matérias, e também podem ser visualizadas pelos alunos no portal do aluno.

### Course Material Distribution  
A ideia seria anexar arquivos para distribuição, mas devido à falta de meios, essa opção mostrará apenas um texto. O acesso para adicionar os arquivos será feito pelo portal dos professores, e a visualização será realizada pelo portal dos alunos.

### Parent Portal  
O portal do aluno oferece o monitoramento de: frequência, horários, exames, biblioteca, boletim de notas, pagamentos e atividades extras.

### Fee and Payment Processing  
Optei pela ideia de parcelas mensais. Ao realizar a matrícula de um aluno no portal dos professores, haverá a opção de registrar quantas parcelas/mensalidades foram pagas. Isso será subtraído de 12, e o saldo restante será apresentado ao aluno em seu portal.

### Examination Management  
Os agendamentos de exames podem ser feitos pelo portal dos professores, onde serão fornecidas a data do exame e a matéria a ser cobrada para uma determinada turma.

### School Bus Tracking  
Ainda não foi implementado.

### Extra-Curricular Activities Management  
Atividades extra-curriculares podem ser oferecidas pelos professores, que podem inscrever seus alunos pelo número de matrícula/ID, com um número limitado de vagas. Os alunos podem ver suas atividades extras no portal dos alunos.
