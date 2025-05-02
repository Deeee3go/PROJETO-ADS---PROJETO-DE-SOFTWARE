RESUMO

Apesar dos avanços alcançados com as leis de transparência, a maneira como esses dados são publicados não estimulam o interesse e não contribuem com a fiscalização por parte da sociedade. Nesse artigo, é proposto um BI dos gastos dos deputados federais com as cotas parlamentares e ainda o perfil dos parlamentares que ocuparam e ocupam a Câmara dos Deputados. As visualizações desenvolvidas permitem conhecer como se dá a distribuição de gênero, faixa etária e nível de escolaridade dos deputados, além de compreender como as cotas parlamentares estão sendo utilizadas. Oferecendo, assim, uma ferramenta de fiscalização útil à população.

1 INTRODUÇÃO
 
Realizar um acompanhamento eficiente sobre os dados públicos não é uma atividade simples pois, apesar das leis nacionais de transparência exigirem que os órgãos públicos disponibilizem esses dados, não significa que esses estarão estruturados para fácil análise e interpretação da população.
É comum encontrar esses dados em formato de planilhas ou, para informações mais recentes, por meio de APIs (Application Programming Interface), dispostos visando unicamente cumprir com a regulamentação.
Assim, visando solucionar tal problemática, esse projeto teve como objetivo criar uma ferramenta que organiza e dispõe uma parte dos dados disponibilizados pela Câmara dos Deputados Federais [1], de forma a possibilitar que a população consiga acompanhar tanto as mudanças de paradigmas ao longo das legislaturas, como também os gastos realizados por partidos políticos, Estado e/ou Deputado eleito. 
Dito isso, o objetivo fundamental desse projeto foi, por meio do processo de Business Intelligence (BI), transformar esses dados brutos em informação útil para o público em geral, permitindo, assim, uma tomada de decisão consciente para as próximas eleições, cobrança aos deputados atualmente empossados e/ou meio de comprovação de notícias e combate às fake news. 

2 FONTE DE DADOS

 O primeiro item a ser estruturado na proposta do projeto foi a escolha da base de dados. Após a avaliação de bancos existentes, identificou-se que os dados disponibilizados pela Câmara dos Deputados Federais, dariam análises coerentes e, com isso, seria possível construir uma ferramenta útil para acompanhamento dos deputados.

Logo, após a avaliação da necessidade de negócio, prosseguiu-se o processo descrito na Figura 1 para construção da solução.

No website dos dados abertos, observou-se que os dados dos deputados são disponibilizados em APIs para integração usando o formato json ou xml e, para períodos mais antigos, em arquivos xml. As informações disponíveis variam entre dados dos deputados, despesas, fornecedores, discursos, eventos, entre outros. 

Após avaliação dos dados, definiu-se qual seria o foco do desenvolvimento, sendo ele, os gastos dos deputados e, também, partido político.  

Com essas informações dispostas de forma apropriada, algumas questões foram avaliadas, como:

 ●           Os deputados e/ou partidos que possuem mais gastos (quais são esses gastos? Quais os principais fornecedores?);
 ●           A média de gastos por Estado.
 
3 COLETA DE DADOS

-Para executar a coleta dos dados, utilizou-se o Pentaho Data Integration, ferramenta que permite realizar as etapas do ETL (Extraction, Transformation and Loading), que são:
 ●           Extração – os dados são coletados dos bancos originais, que podem ser de diferentes fontes. Conforme Costa [3], os dados devem ser extraídos diante da necessidade do projeto, para uma economia não só do espaço em disco, como também do tempo de extração.
 ●           Transformação – A transformação dos dados é o segundo e principal passo do processo ETL [5]. Nessa etapa, será realizada toda a limpeza de dados necessária e modificação dos dados.
 ●           Carga dos dados – Os dados são enviados para o banco de destino.
-Antes de iniciar o ETL, é necessário realizar a modelagem multidimensional dos dados, que possui dois tipos de tabelas:
 ●           Tabela fato - valores mensuráveis do negócio. 
 ●           Tabela dimensão - atributos das dimensões.

Assim, considerando o objetivo do BI e as questões levantadas, o esquema protagoniza com as tabelas de fato e dimensão, em que foi o escolhido para a modelagem dos dados em análise.
Após a definição do modelo, foram criadas as transformações necessárias para extração e tratamento dos dados, como pode ser visto, para ilustração, da dimensão deputado e de fato despesa.
Enfim, o modelo pôde ser criado com o auxílio do Pentaho.
