# Relatório de Análise Didática e Comunicação Técnica Dessengessada

**Projeto:** Seminário Red Team 1 — Reconhecimento e OSINT  
**Autor:** Explorer 3 — Especialista em Didática e Comunicação Técnica  
**Data:** 31 de Outubro de 2026  
**Diretório:** `.agents/teamwork/teamwork_explorer_survey_3/`  
**Referencial Metodológico:** Diretrizes da skill `/no-ai-slop`, Princípios de Pedagogia Técnica e Redução de Carga Cognitiva (Sweller / Mayer).

---

## Sumário Executivo

A apresentação do seminário *Red Team 1 — Recon & OSINT* possui qualidades visuais e conceituais notáveis: a interface Reveal.js é refinada, as simulações de terminal (Nmap) e de pacotes (Wireshark) são de alto nível estético, e existe o embrião de um fio narrativo condutor espetacular (a personagem Marina Sousa e a empresa fictícia Acme Pagamentos).

Entretanto, sob a ótica didática e de comunicação falada para uma audiência técnica (banca examinadora e colegas de computação/cibersegurança), a apresentação enfrenta quatro grandes desafios estruturais:

1. **A Maratona Hiperestendida do Bloco 03 (Daniel):** O Bloco 03 concentra 25 slides consecutivos (do slide 16 ao 40) sob a responsabilidade de um único orador, representando 46% de todo o deck. Dentro desse bloco, ocorrem 16 slides com layouts praticamente idênticos (`cycle-detail` e `tool-detail-grid`), gerando monotonia visual e fadiga de atenção na audiência.
2. **Tripla Redundância Conceitual de *Certificate Transparency*:** O mesmo conceito técnico (CT Logs) é introduzido e explicado três vezes em subseções adjacentes: no Ciclo OSINT (slide 21), nas Técnicas Passivas (slide 28) e no detalhe de Ferramentas com `crt.sh` (slide 35), sem que haja uma progressão didática clara entre elas.
3. **Engessamento Defensivo e Linguagem Protocolar:** Para evitar a impressão de incentivo a ataques reais, muitos slides e notas do orador recorreram a uma linguagem excessivamente burocrática e engessada, repleta de rodeios ("cenário fictício", "observações anteriores", "não confirma a situação atual", "é importante notar"). Isso esconde a mecânica técnica viva atrás de ressalvas acadêmicas vazias.
4. **Fadiga de Nominalizações:** Presença reiterada de construções passivas e nomes abstratos onde verbos diretos de ação deveriam conduzir a explicação (*"realizar a verificação"*, *"proceder à coleta"*, *"separação entre sinal e ruído"*).

Abaixo, detalha-se a análise slide a slide, apontando gargalos, propostas de reformulação sob os princípios `/no-ai-slop` e um catálogo de modelos mentais e metáforas funcionais para elevar o impacto da apresentação sem "emburrecer" o conteúdo.

---

## 1. Auditoria Didática e Carga Cognitiva por Bloco

### Bloco 00: Capa e Agenda (Slides 01 e 02) — Todos

* **Slide 01 (Capa):**
  * *Observação:* Subtítulo atual: *"Tudo o que o alvo revela antes de ser atacado."*
  * *Carga Cognitiva:* Baixa e bem calibrada. O radar com efeito sweep e o bloco com redação tarjada (*"superfície de ataque"*) capturam o olhar imediatamente.
  * *Ajuste Didático:* "O alvo revela" coloca o alvo como agente passivo quase voluntário.
  * *Reformulação Dessengessada:* *"O que o alvo entrega sem perceber — e o que o atacante faz com isso."* (Traz tensão, ação e foco no processo investigativo).

* **Slide 02 (Agenda):**
  * *Observação:* *"Seis blocos. Uma pergunta: o que o alvo já contou? / Começamos pelo conceito, passamos pelas duas faces do reconhecimento..."*
  * *Gargalo Didático:* "Duas faces do reconhecimento" é um clichê de livro-texto que antecipa pouco. No bloco 03, dizer *"OSINT, fontes abertas e o ecossistema"* é tautológico (OSINT já é *Open Source Intelligence*).
  * *Reformulação Dessengessada:*
    * Substituir *"duas faces"* por termos operacionais: *"tocar no alvo (ativo) e observar de longe (passivo)"*.
    * Bloco 03 na agenda: *"Reconhecimento passivo: OSINT, registros públicos e inteligência sem tocar no alvo."*

---

### Bloco 01: Conceito e Contexto (Slides 03 a 09) — Geovana

* **Slide 03 (Divisor 01):**
  * *Texto:* *"Todo ataque começa com uma pergunta. Reconhecer é descobrir a resposta antes de tocar no alvo."*
  * *Avaliação:* Excelente gancho. Didático, direto, cria o modelo mental correto.

* **Slide 04 (Era das mídias sociais):**
  * *Gargalo Cognitivo Grave:* O slide exibe três métricas lado a lado: **9h** de tela por dia, **3h** em redes sociais e **116h conectado por semana**.
  * *Conflito Lógico:* Uma audiência técnica divide instantaneamente: $116 \div 7 \approx 16,5\text{ h/dia}$. Como alguém passa 9h por dia diante de tela e 16,5h conectado por semana? A nota de rodapé tenta se desculpar (*"Métricas de pesquisas diferentes: use como ordem de grandeza, não como cronômetro"*), mas apresentar números conflitantes em destaque destrói a autoridade técnica do orador.
  * *Solução Pedagógica:* Cortar a métrica de 116h/semana. Manter uma única fonte coerente: **9 horas diárias de tela**, sendo **3 horas imersas em redes sociais**. O impacto didático é: *"Um terço do dia acordado gerando telemetria e rastro público."*

* **Slide 05 (Evolução das redes):**
  * *Gargalo Didático e Histórico:* A linha do tempo lista Usenet como 1974 (erro histórico: Usenet foi concebida em 1979 e operou em 1980; 1974 foi o protocolo TCP de Cerf/Kahn). Além disso, a linha do tempo parece um resumo genérico de Wikipedia descolado da segurança ofensiva.
  * *Salto Pedagógico ("Open it up, don't dumb it down"):* Transformar a linha do tempo na **Evolução da Superfície de Exposição**:
    * **1979 (Usenet):** Discussões técnicas em texto puro e vazamento precoce de e-mails de administradores.
    * **2003 (LinkedIn):** O organograma das corporações entregue de bandeja: quem manda, quem programa, qual firewall usam.
    * **2004 (Facebook/Orkut):** Relações pessoais e respostas prontas para perguntas de recuperação de senha (*"qual o nome do seu primeiro animal?"*).
    * **2006 (Twitter):** Telemetria em tempo real: *"o servidor caiu"*, *"estou no aeroporto"*.
    * **2010 (Instagram):** Metadados fotográficos, crachás no pescoço e telas de computadores ao fundo da selfie.

* **Slide 06 (Superexposição):**
  * *Avaliação:* Ponto alto do bloco. O post fictício de Marina Sousa (@marina.souza) comemorando o fim do plantão no novo datacenter da *Acme Pagamentos* é uma ilustração perfeita de vazamento de contexto operacional.
  * *Ajuste de Tom:* O texto atual diz: *"Nos tornamos dependentes de estímulo e superexpomos a própria vida."* Soa como sermão moralista. Substituir por foco analítico: *"O hábito de compartilhar rotinas corporativas transforma a conveniência do funcionário no mapa de entrada do adversário."*

* **Slide 07 (Caso Twitter):**
  * *Observação:* Relato de um post de cinema que resultou em confronto físico.
  * *Gargalo:* Uso da imagem de banco com nome tosco (`Estrategias-para-Lidar-com-o-Comportamento-Desafiador-das-Criancas...`). A explicação foca em "duas pessoas em atrito".
  * *Enquadramento Didático:* Enquadrar como **OSINT Tático e Rastreamento Físico com Latência Zero**:
    1. *Sinal:* Local + horário futuro imediato ("filme das 21h").
    2. *Consequência:* O observador ganha uma janela de 120 minutos de certeza física sem precisar colocar uma escuta ou seguir o alvo pela cidade.

* **Slide 08 (Caso Smart Sampa):**
  * *Gargalo:* O slide diz que as credenciais ficaram expostas por 11 meses por *"uma falha de cuidado"*. Isso é abstrato e vago.
  * *Concretude Técnica:* Como a credencial ficou exposta? Estava indexada em busca pública, repositório ou planilha aberta? Explicar o princípio de recon: *"O invasor não precisou quebrar a criptografia de 58 mil câmeras; bastou consultar credenciais que estavam expostas sem rotação."*

* **Slide 09 (Definição):**
  * *Avaliação:* Muito sólido. Cita MITRE ATT&CK TA0043.
  * *Pedagogia de Síntese:* Enfatizar a dualidade didática: *"Para quem ataca, o recon define onde bater. Para quem defende, revela onde fechar antes da primeira batida."*

---

### Bloco 02: Reconhecimento Ativo (Slides 10 a 15) — Emilio

* **Slide 11 (Redes em 60 segundos):**
  * *Avaliação Didática:* Fantástica simplificação (IP, Porta, Pacote).
  * *Metáfora Funcional:* A analogia prédio (IP) / apartamento (porta) / envelope (pacote) funciona muito bem para nivelar a sala.
  * *Aprofundamento Didático:* Explicar *por que* a porta importa para o scan: a porta não é apenas um número; ela é a porta de entrada para um processo em execução. Se a porta 8080 está aberta, há um software escutando requisições e pronto para responder a comandos.

* **Slide 12 (Nmap: Simulação):**
  * *Avaliação:* Simulação de terminal impecável (`nmap -sS -sV -p- 10.10.14.23`).
  * *Gargalo nas Notas do Orador:* As notas sugerem perguntar *"o que vocês olhariam primeiro?"*, mas o orador precisa conduzir a dedução:
    * Portas 80 e 443 são esperadas (serviço web padrão).
    * Porta 22 (SSH) é administração remota.
    * **Porta 3306 (MySQL):** Por que um banco de dados está exposto diretamente para a rede externa em vez de isolado na DMZ?
    * **Porta 8080 (Jetty):** Aplicações em portas altas frequentemente são consoles de homologação ou painéis administrativos esquecidos.
  * *Metáfora do SYN Scan:* Explicar o `-sS`: *"É o toque de campainha do atacante: ele aperta a campainha (SYN), ouve alguém se aproximar e destrancar a fechadura (SYN/ACK), mas vai embora correndo antes de entrar (RST). O dono da casa não chega a registrar a visita, mas o atacante já sabe que tem gente em casa."*

* **Slide 13 e 14 (Wireshark e Handshake/Stream):**
  * *Carga Cognitiva:* Altíssima densidade visual de pacotes e hexadecimais no slide 13.
  * *Didática do Foco Visual:* No slide 13, o orador deve guiar a plateia: *"Ignorem o hexadecimal por dez segundos. Olhem apenas a coluna 'Info': 3 pacotes para dar as mãos, 1 pacote pedindo `/admin/`, e o servidor dizendo '401 Unauthorized'."*
  * *Slide 14 (Follow TCP Stream):* Momento "uau" da apresentação. Demonstrar que `YWRtaW46YWRtaW4=` é Base64 e não criptografia.
  * *Regra de Didática:* *"Base64 é apenas empacotamento para transporte, não é cofre. Qualquer observador no meio do caminho decodifica a senha no piscar de olhos."*

* **Slide 15 (Phishing e Engenharia Social):**
  * *Avaliação:* Excelente e-mail fictício de RH da Acme com anexo em macro.
  * *Conexão Didática de Causa e Efeito:* Amarrar o phishing ao Reconhecimento! Phishing corporativo (Spear-phishing) não cai do céu. O atacante só consegue enviar um e-mail crível de benefícios porque antes fez recon: descobriu no LinkedIn quem trabalha na empresa, o padrão de e-mail corporativo (`@acme.com.br`) e o período de renovação de benefícios.

---

### Bloco 03: Reconhecimento Passivo e OSINT (Slides 16 a 40) — Daniel

Este é o trecho mais crítico da apresentação inteira. São **25 slides consecutivos**. Se o orador gastar 1 minuto por slide, consumirá 25 minutos dos 45 minutos totais, deixando os outros 4 apresentadores espremidos.

#### Diagnóstico dos Três Sub-blocos de Daniel:
1. **Slides 16–18 (Introdução e Conceito):**
   * *Problema:* Slide 17 (*"Mapear a pegada sem consultar o alvo"*) e Slide 18 (*"O que é OSINT"*) competem entre si. Ambos trazem a mesma mensagem: consultar fontes externas sem gerar pacotes ao alvo.
   * *Solução Didática:* Tornar o Slide 17 puramente mecânico (a topologia do isolamento de tráfego) e o Slide 18 conceitual (a transformação de dados soltos em inteligência acionável).
2. **Slides 19–25 (O Ciclo de OSINT em 6 fases):**
   * *Problema:* Seis slides idênticos de layout cinza com o exemplo artificial `portal.example.com`. A repetição de *"Caso fictício · dados históricos não confirmam a situação atual"* a cada tela cria uma cadência sonolenta de manual burocrático.
   * *Solução Didática:* Variar a ênfase pedagógica de cada fase usando verbos e riscos reais:
     * *01 Planejar:* "Sem pergunta, você se afoga no oceano de dados. Escopo é bússola."
     * *02 Coletar:* "Coleta sem carimbo de data (timestamp) é inútil. Na web, o que existia ontem pode ter sumido hoje."
     * *03 Processar:* "Normalizar e deduplicar. Se você não separar o lixo do sinal, sua análise vai caçar fantasmas."
     * *04 Analisar:* "A armadilha mental: ver um certificado antigo não significa que o servidor está vulnerável hoje. Evidência é fato; inferência é aposta."
     * *05 Disseminar:* "Ninguém lê relatório de 80 páginas sem conclusão. O decisor quer saber: o que está exposto, quem conserta e qual a urgência."
     * *06 Feedback:* "Toda resposta técnica abre a próxima pergunta investigativa."
3. **Slides 26–30 (Técnicas) vs Slides 31–37 (Ferramentas):**
   * *Problema Didático Central — O Loop de Certificate Transparency:*
     * Slide 21 (Ciclo): Mostra CT log de `portal.example.com`.
     * Slide 28 (Técnica): Explica o que é CT log de `example.com`.
     * Slide 35 (Ferramenta `crt.sh`): Mostra busca em CT log de `example.com`.
     * A plateia ouve a mesma explicação três vezes em menos de 10 minutos!
   * *Desengessamento e Diferenciação Didática:*
     * No slide 28 (Técnica), explicar o **Mecanismo Global de CT**: *"Para emitir um certificado HTTPS válido que não dê tela vermelha no navegador, a autoridade certificadora é obrigada por lei técnica da internet a registrar o domínio em um cartório público global imutável. No momento em que a equipe de TI cria um subdomínio de testes (`vpn-homolog.empresa.com`), o mundo inteiro fica sabendo."*
     * No slide 35 (Ferramenta), focar na **Ação Prática**: *"O `crt.sh` é o buscador que consulta esse cartório em segundos usando o operador `%` (wildcard). Ele não toca na empresa; lê o histórico de nascimentos digitais do domínio."*

#### O Bloco Físico e o Ecossistema (Slides 38 a 40):
* **Slide 38 (Dumpster Diving):**
  * *Avaliação:* Excelente quebra de ritmo após tantos slides de terminal e tabelas. Mostra que segurança da informação não é apenas bytes.
* **Slide 39 (Shoulder Surfing):**
  * *Avaliação:* Muito visual e fácil de absorver.
* **Slide 40 (Ecossistema INT — 9 disciplinas):**
  * *Gargalo Cognitivo:* Uma tabela com 9 siglas militares (HUMINT, GEOINT, FININT, ELINT, IMINT, TECHINT, CYBINT, SOCMINT, SIGINT) disparadas de uma vez só pode assustar a audiência.
  * *Dica Didática:* Não leia as 9 siglas! Destaque apenas as quatro que se conectam ao seminário:
    * **OSINT:** Fontes abertas (nosso tema).
    * **HUMINT:** O fator humano (conectado ao Phishing do Emilio e ao caso RSA).
    * **GEOINT:** Inteligência geográfica (ponte direta para a demo do João Pedro Almeida e o caso Strava).
    * **SOCMINT:** Redes sociais (o post da Marina Sousa).

---

### Bloco 04: Estudos de Caso (Slides 41 a 44) — João Pedro Gonçalves

* **Slide 42 (Caso RSA — 2011):**
  * *Inconsistência Identificada:* O arquivo na reprodução do e-mail está nomeado como `2021_Recruitment_Plan.xlsx` para um ataque ocorrido em **março de 2011**! Um anacronismo de dez anos que distrai o leitor atento.
  * *Correção Didática:* Deve ser `2011_Recruitment_Plan.xls` (em 2011, arquivos maliciosos frequentemente usavam `.xls` ou exploits de Flash encapsulados em Excel).
  * *Mecânica do Recon:* Ressaltar que os invasores não escolheram a RSA ao acaso: estudaram os nomes de funcionários juniores no RH para disparar o e-mail direcionado.

* **Slide 43 (Caso Strava — 2018):**
  * *Avaliação:* Visual espetacular da base militar revelada pelas rotas circulares de corredores.
  * *Conceito Pedagógico Nobre:* **Inteligência Emergente por Agregação**.
    * Nenhum soldado vazou segredo militar de propósito.
    * Cada atividade física isolada parecia irrelevante.
    * A *sobreposição de dados autorizados* desenhou a base secreta no deserto afegão.
    * *Frase de efeito didático:* *"O adversário não precisou quebrar criptografia nem subornar sentinela: bastou abrir um mapa público de corrida."*

* **Slide 44 (Lição dos Casos):**
  * *Texto:* *"O dado mais perigoso é aquele que parece inofensivo. Reconhecimento é correlação, não coleta."*
  * *Avaliação:* Síntese perfeita. Fixa o aprendizado antes da demonstração prática.

---

### Bloco 05: Demonstração Prática (Slides 45 a 48) — João Pedro Almeida

* **Slide 46 e 47 (GEOSINT 1 e 2 — A foto da Ruta 40 e a Eliminação de Hipóteses):**
  * *Avaliação Didática:* Extraordinário exercício de pensamento crítico e dedução.
  * *O Método Científico em Ação:*
    * Pista 1 (Sombra longa para a esquerda com sol à direita): Define horário (fim de tarde) e orientação cardinal via SunCalc.
    * Pista 2 (Vegetação rasteira e relevo árido): Elimina regiões litorâneas ou florestais.
    * Pista 3 (Placa Ruta 40 / Mendoza): Restringe à província argentina.
    * Slide 47 (Eliminação de A e B, confirmação de C): Mostra que inteligência não é "adivinhar no chute", mas formular hipóteses testáveis e eliminar inconsistências.

* **Slide 48 (Grafo de OSINT — O Fechamento da Narrativa):**
  * *Oportunidade Didática de Ouro:* O grafo mostra `@marina.souza` $\rightarrow$ `marina@acme.com` $\rightarrow$ vazamentos de senhas antigas $\rightarrow$ VPN de borda exposta $\rightarrow$ cargo financeiro.
  * *Alinhamento Narrativo:* O orador DEVE dizer: *"Vocês se lembram da Marina do Slide 06, comemorando o fim do plantão no datacenter da Acme? Aqui está o ciclo fechado: o nome de usuário dela no post levou ao e-mail corporativo; o e-mail apareceu em vazamentos de bases antigas; o domínio revelou uma VPN desatualizada; e o cargo dela no LinkedIn mostrou que ela aprova pagamentos. Em vinte minutos de correlação pública, o invasor montou o mapa completo sem tocar no firewall da empresa."*
  * Isso une o início, o meio e o fim do seminário em um único arco inesquecível.

---

### Bloco 06: OpSec e Fechamento (Slides 49 a 52) — Geovana & Todos

* **Slide 50 (OpSec — Conceito):**
  * *Diagrama:* Anéis concêntricos com VOCÊ no centro e os dados irradiando.
  * *Definição Didática:* *"OpSec não é sobre viver como um fantasma ou cortar os cabos de internet. É sobre saber o que suas ações cotidianas revelam, avaliar quem se interessa por isso e diminuir o ruído para continuar operando."*

* **Slide 51 (OpSec no dia a dia — Seis hábitos):**
  * *Avaliação:* Prático, aplicável e sem jargões desnecessários (2FA, senhas únicas com cofre, atualizações automáticas, revisão de permissões, separação de identidades e limpeza de metadados EXIF).
  * *Pedagogia de Fixação:* Ligar os hábitos diretamente ao grafo do slide 48:
    * Se a Marina usasse autenticador em dois fatores (2FA), a senha vazada no fórum não permitiria login.
    * Se ela limpasse o EXIF da foto do datacenter, o atacante não teria as coordenadas exatas da sala de servidores.

* **Slide 52 (Takeaways):**
  * *Três Conclusões de Impacto:*
    1. *Método:* Recon é processo e hipótese, não aperto de botão em ferramenta.
    2. *Superfície:* O firewall não protege o que os funcionários publicam na internet.
    3. *Contra-inteligência:* Segurança começa antes do ataque.
  * *Frase de Encerramento:* *"Recon é a única etapa do ataque que a defesa também pode — e deve — praticar todos os dias."*

---

## 2. Diagnóstico de Engessamento e AI Slop Didático

Com base no catálogo de padrões e princípios da skill `/no-ai-slop`, identificamos os seguintes vícios recorrentes na redação atual dos slides e notas:

### A. Nominalizações Abstratas vs. Verbos de Ação ("Make verbs do the work")

| Trecho Atual (Engessado / Passivo) | Por que soa a AI Slop / Burocrático | Reformulação com Verbo Ativo |
| :--- | :--- | :--- |
| *"A realização da verificação autorizada é necessária para confirmação."* (Slide 23) | Amontoado de substantivos abstratos (*realização, verificação, confirmação*). | *"A equipe precisa verificar o servidor com autorização expressa."* |
| *"Permite a extração de metadados e histórico de autores."* (Slide 31) | *"Permite a extração"* enfraquece a ferramenta. | *"Extrai o autor, a câmera e a versão do software usado."* |
| *"Consultam índices de serviços, portas e banners já coletados por terceiros."* (Slide 31) | Construção frouxa e enciclopédica. | *"Buscam portas abertas e serviços já mapeados na internet."* |
| *"Separação de sinal e ruído através do agrupamento de duplicatas."* (Slide 22) | Jargão corporativo abstrato. | *"Remove duplicatas e descarta o que não responde à pergunta."* |

### B. Rodeios Textuais e Falsas Modéstias ("Throat-clearing openers & caveats")

* **No Slide 04:** *"Métricas de pesquisas diferentes: use como ordem de grandeza, não como cronômetro."*  
  $\rightarrow$ *Ajuste:* Corte o preâmbulo defensivo. Diga o fato concreto: *"Passamos 9 horas por dia diante de telas — um terço do dia gerando rastro público."*
* **Nos Slides 20 a 25:** Repetição sistemática da etiqueta *"CASO FICTÍCIO · PERGUNTA INICIAL"*, *"HIPÓTESE · CASO FICTÍCIO"*, *"DADOS FICTÍCIOS"*.  
  $\rightarrow$ *Ajuste:* Um aviso discreto no rodapé ou na abertura do bloco é suficiente. Rotular cada caixa de texto como "fictício" quebra a imersão pedagógica da plateia e faz os slides parecerem petições jurídicas de conformidade.
* **No Slide 17:** *"Mapear a pegada sem consultar o alvo."*  
  $\rightarrow$ *Ajuste:* "Pegada" isolada é vago. Especifique: *"Mapear domínios, e-mails e tecnologias sem enviar um único pacote ao servidor do alvo."*

### C. A Regra do "Open it up, don't dumb it down"

Simplificar não significa infantilizar. Quando o slide aborda **Certificate Transparency (CT)** ou **ASN (Autonomous System Number)**, ele não deve esconder o termo técnico, mas abrir sua anatomia:
* *Errado (engessado/vago):* *"ASN é uma métrica de rede de provedores observada em bases de infraestrutura."*
* *Errado (simplista demais):* *"ASN é o nome da internet."*
* *Certo (aberto, preciso e concreto):* *"ASN é o código postal que identifica quem é o dono de um bloco de IPs: se o servidor do alvo está hospedado na nuvem da AWS, num provedor local em São Paulo ou em uma máquina esquecida no escritório."*

---

## 3. Catálogo de Metáforas Funcionais e Modelos Mentais

Para que a apresentação seja vibrante e imediatamente apreensível por qualquer espectador, os oradores devem ancorar os conceitos técnicos nas seguintes metáforas operacionais:

```
+-----------------------------------+-------------------------------------------------------------+
| Conceito Técnico                  | Metáfora Funcional / Modelo Mental                          |
+-----------------------------------+-------------------------------------------------------------+
| Reconhecimento Passivo            | "A Vitrine da Loja": Andar pela calçada anotando os preços |
| vs. Reconhecimento Ativo          | e horários na vitrine (Passivo) vs. Tentar girar a maçaneta |
|                                   | para ver se a porta dos fundos abre (Ativo).                |
+-----------------------------------+-------------------------------------------------------------+
| Nmap SYN Scan (-sS)               | "Bater e Correr": O atacante aperta a campainha (SYN), ouve |
|                                   | o morador destrancar o trinco (SYN/ACK), mas vai embora     |
|                                   | antes de a porta abrir (RST). O dono da casa não registra   |
|                                   | visita, mas o atacante já sabe que tem gente lá dentro.     |
+-----------------------------------+-------------------------------------------------------------+
| Certificate Transparency (CT)     | "O Diário Oficial do Cartório Web": Nenhum certificado SSL  |
|                                   | tem validade sem ser publicado nesse livro público global.  |
|                                   | Criou um subdomínio de teste, ele vai para a vitrine.       |
+-----------------------------------+-------------------------------------------------------------+
| Dados Agregados (Caso Strava)     | "A Trilha de Formigas": Uma formiga no quintal é invisível. |
|                                   | Dez mil formigas marchando no mesmo caminho abrem uma vala  |
|                                   | na grama perceptível até por satélite.                      |
+-----------------------------------+-------------------------------------------------------------+
| Google Dorking                    | "A Lente Polarizada": O Google indexou bilhões de arquivos; |
|                                   | os operadores apenas filtram a água suja para enxergar      |
|                                   | planilhas de senhas e arquivos de configuração esquecidos.  |
+-----------------------------------+-------------------------------------------------------------+
| Base64 em HTTP                    | "Envelope Transparente": Não é cofre trancado com segredo;  |
|                                   | é apenas papel celofane. Qualquer um lê através dele.       |
+-----------------------------------+-------------------------------------------------------------+
| OpSec                             | "Higiene Pessoal": Não é tomar banho de armadura medieval;   |
|                                   | é lavar as mãos antes das refeições todos os dias.          |
+-----------------------------------+-------------------------------------------------------------+
```

---

## 4. Reestruturação Pedagógica e Fluxo Causa-Efeito

### Resolvendo a Fadiga do Bloco 03 (Daniel — 25 Slides)

Recomenda-se uma dinâmica de apresentação que alterne o peso cognitivo:

1. **Agrupamento Dinâmico no Ciclo OSINT (Slides 19 a 25):**
   * Em vez de ler cada slide como se fosse uma nova aula teórica, o orador Daniel deve tratar os slides 20 a 25 como uma **sequência cinematográfica em 6 passos rápidos**. Cada passo deve demorar no máximo 25 a 30 segundos, guiando o olhar pelo elemento diferenciador (o filtro, o gráfico, o relatório).
2. **Diferenciação Clara entre Técnica e Ferramenta:**
   * Slide de Técnica = *Qual a lógica do dado na internet?* (ex: O que é um log de certificados).
   * Slide de Ferramenta = *Como o analista consulta isso em 3 segundos?* (ex: O comando ou consulta no `crt.sh`).
3. **Exploração do "Fio de Ariadne" — O Caso Marina / Acme Pagamentos:**
   * O seminário ganha coesão magistral ao transformar o post da Marina (Slide 06) no alvo que percorre o deck:
     * *Slide 06:* O post no Instagram revela que ela trabalha na Acme Pagamentos e está no novo datacenter.
     * *Slide 15:* O phishing do RH chega direcionado para colaboradores da Acme.
     * *Slide 21/28/35:* Os certificados revelam o subdomínio `datacenter-sp.acme.com`.
     * *Slide 48:* O grafo final conecta o username dela ao e-mail, às credenciais vazadas e ao painel de acesso da VPN.
   * Essa conexão narrativa amarra os cinco apresentadores em um time coeso, demonstrando que não são apresentações individuais desconexas, mas uma investigação encadeada.

---

## 5. Recomendações para os Oradores (Speaker Notes e Performance)

1. **Nunca leia as listas completas dos slides:**
   * No slide de ferramentas (Slide 31) ou de disciplinas INT (Slide 40), o maior erro didático é ler linha por linha. O orador deve escolher duas ou três linhas de alto contraste e dizer: *"Vejam estes dois exemplos extremos..."*.
2. **Uso de Pausas Dramáticas:**
   * No Slide 08 (Smart Sampa) e Slide 44 (Strava): deixar a tela por 3 segundos em silêncio após enunciar: *"58 mil câmeras. 11 meses de senhas expostas."* e *"Ninguém invadiu o Strava. O dado era público."* A pausa permite que o impacto afunde na mente da banca.
3. **Controle de Tempo do Deck:**
   * Bloco 00 (Abertura): 2 minutos.
   * Bloco 01 (Geovana - Conceito): 6 minutos.
   * Bloco 02 (Emilio - Ativo): 8 minutos.
   * Bloco 03 (Daniel - Passivo e OSINT): 14 minutos (ritmo ágil nos detalhes).
   * Bloco 04 (João Pedro G. - Casos): 6 minutos.
   * Bloco 05 (João Pedro A. - Demo): 6 minutos.
   * Bloco 06 (Geovana - OpSec): 3 minutos.
   * Total estimado de apresentação: **45 minutos cravados**, sobrando tempo ideal para arguição da banca.

---

## Conclusão

O material dos slides tem uma base técnica sólida e design de ponta. O trabalho de desengessamento não exige remover conteúdo ou simplificar conceitos, mas sim:
1. Libertar o texto de amarras burocráticas e ressalvas excessivas;
2. Fazer os verbos liderarem as frases;
3. Potencializar a história da Acme Pagamentos como âncora de retenção para a plateia;
4. Equalizar a cadência de apresentação para garantir que a densidade técnica do Bloco 03 brilhe sem cansar os avaliadores.
