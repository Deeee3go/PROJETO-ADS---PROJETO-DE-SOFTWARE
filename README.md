RESUMO

Apesar dos avanços alcançados com as leis de transparência, a maneira como esses dados são publicados não estimulam o interesse e não contribuem com a fiscalização por parte da sociedade. Nesse artigo, é proposto um BI dos gastos dos deputados federais com as cotas parlamentares e ainda o perfil dos parlamentares que ocuparam e ocupam a Câmara dos Deputados. As visualizações desenvolvidas permitem conhecer como se dá a distribuição de gênero, faixa etária e nível de escolaridade dos deputados, além de compreender como as cotas parlamentares estão sendo utilizadas. Oferecendo, assim, uma ferramenta de fiscalização útil à população.

1 INTRODUÇÃO
 
Realizar um acompanhamento eficiente sobre os dados públicos não é uma atividade simples pois, apesar das leis nacionais de transparência exigirem que os órgãos públicos disponibilizem esses dados, não significa que esses estarão estruturados para fácil análise e interpretação da população.
É comum encontrar esses dados em formato de planilhas ou, para informações mais recentes, por meio de APIs (Application Programming Interface), dispostos visando unicamente cumprir com a regulamentação.
Assim, visando solucionar tal problemática, esse projeto teve como objetivo criar uma ferramenta que organiza e dispõe uma parte dos dados disponibilizados pela Câmara dos Deputados Federais, de forma a possibilitar que a população consiga acompanhar tanto as mudanças de paradigmas ao longo das legislaturas, como também os gastos realizados por partidos políticos, Estado e/ou Deputado eleito. 
Dito isso, o objetivo fundamental desse projeto foi, por meio do processo de Business Intelligence (BI), transformar esses dados brutos em informação útil para o público em geral, permitindo, assim, uma tomada de decisão consciente para as próximas eleições, cobrança aos deputados atualmente empossados e/ou meio de comprovação de notícias e combate às fake news. 

2 FONTE DE DADOS

 O primeiro item a ser estruturado na proposta do projeto foi a escolha da base de dados. Após a avaliação de bancos existentes, identificou-se que os dados disponibilizados pela Câmara dos Deputados Federais, dariam análises coerentes e, com isso, seria possível construir uma ferramenta útil para acompanhamento dos deputados.

No website dos dados abertos, observou-se que os dados dos deputados são disponibilizados em APIs para integração usando o formato json ou xml e, para períodos mais antigos, em arquivos xml. As informações disponíveis variam entre dados dos deputados, despesas, fornecedores, discursos, eventos, entre outros. 

Após avaliação dos dados, definiu-se qual seria o foco do desenvolvimento, sendo ele, os gastos dos deputados e, também, partido político.  

Com essas informações dispostas de forma apropriada, algumas questões foram avaliadas, como:

 ●           Os deputados e/ou partidos que possuem mais gastos (quais são esses gastos? Quais os principais fornecedores?);
 ●           A média de gastos por Estado.
 
3 COLETA DE DADOS

-Para executar a coleta dos dados, utilizou-se o Pentaho Data Integration, ferramenta que permite realizar as etapas do ETL (Extraction, Transformation and Loading), que são:
 ●           Extração – os dados são coletados dos bancos originais, que podem ser de diferentes fontes. Os dados devem ser extraídos diante da necessidade do projeto, para uma economia não só do espaço em disco, como também do tempo de extração.

 ●           Transformação – A transformação dos dados é o segundo e principal passo do processo ETL. Nessa etapa, será realizada toda a limpeza de dados necessária e modificação dos dados.

 ●           Carga dos dados – Os dados são enviados para o banco de destino.

 ●           Tabela fato - valores mensuráveis do negócio. 

 ●           Tabela dimensão - atributos das dimensões.

Assim, considerando o objetivo do BI e as questões levantadas, o esquema protagoniza com as tabelas de fato e dimensão, em que foi o escolhido para a modelagem dos dados em análise.
Após a definição do modelo, foram criadas as transformações necessárias para extração e tratamento dos dados, como pode ser visto, para ilustração, da dimensão deputado e de fato despesa.
Enfim, o modelo pôde ser criado com o auxílio do Lucid Charts.

![image](https://github.com/user-attachments/assets/ac6d643d-d166-40c7-b7c5-1c3c82aba678)

![image](https://github.com/user-attachments/assets/cba8c308-4b67-43c5-9f00-76f5940728b9)


4 ANÁLISE DE DADOS
 
Como o principal objetivo do artigo é permitir um acompanhamento dos gastos públicos dos deputados e um maior conhecimento das pessoas que ocupam a Câmara do Deputados, a forma como as informações são apresentadas é a etapa fundamental do projeto e para realizar foi escolhido o software de visualização de dados Tableau, que possui uma série de produtos (Tableau Public, Tableau Desktop, Tableau Mobile, Tableau Online) e se propõe a facilitar ao usuário a exploração e gerenciamento dos dados e agiliza a descoberta e o compartilhamento de informações.
Para construir os dashboards, foi utilizado o Tableau Desktop - Public Edition que possui uma versão teste que permitiu a criação das visualizações necessárias.

5 METODOLOGIA


A interface desenvolvida foi separada em 2 dashboards: Gastos por Deputado; Gastos por Região. É importante destacar, que algumas comparações devem ser realizadas entre pares. Por exemplo, analisar os deputados de um estado ou região para validade da comparação, pois alguns gastos são diretamente relacionados com a localização, como Passagens Aéreas.


6 CONCLUSÕES

No contexto do projeto, é possível criar uma solução para que a população possa interpretar os dados de forma eficiente. Com isso, o cidadão pode acompanhar os gastos dos deputados do seu estado e realizar cobranças, validar notícias veiculadas pela mídia e, também, combater a divulgação de fake news. Tudo isso junto, serve como uma ferramenta útil para tomada de decisão nas próximas eleições.
Vale salientar, que por ausência de dados suficientes, as trocas entre partidos não foram consideradas, portanto, sendo considerado escopo negativo do trabalho desenvolvido.
Como forma de evoluir o trabalho atual, propomos a inclusão de mais legislaturas na base de dados, para que tendências possam ser identificadas. Também, podemos incluir um mecanismo para sincronização automática da base de dados, ou seja, com a disponibilização de novos dados, os dashboards seriam atualizados automaticamente. Outra melhoria possível, é reduzir a granularidade das categorias dos gastos e normalizar os fornecedores duplicados na base disponibilizada pela Câmara.
Além disso, a criação de um modelo de aprendizado de máquina para identificação de fraudes seria um passo importante para a análise do volume disponível de gastos.

REFERÊNCIAS

1- DADOS ABERTOS DA CÂMARA DOS DEPUTADOS. Disponível em: https://dadosabertos.camara.leg.br/swagger/api.html. Acesso em 16 de fev. de 2021. 

2- KIMBALL, R.; CASERTA, J. The Data Warehouse ETL Toolkit – Practical Techniques for Extracting, Cleaning, Conforming, and Delivering Data. Indianápolis. Wiley Publishing, Inc., 2004. 490p.

3- TABLEAU. O que é o Tableau? 2021. Disponível em: https://www.tableau.com/pt-br/why-tableau/what-is-tableau. Acesso em 23 de maio de 2021.

4- LINK DASHBOARD DEPUTADOS. Disponível em: [https://public.tableau.com/profile/diogo.kabbaz#!/vizhome/ProjetoCECDA2019_2/StoryDeputados-GastosePerfil](https://public.tableau.com/views/ProjetodeconclusoADS-DashBoarddeGastosParlamentardeDeputados/StoryDeputados-GastosePerfil?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

