# Red Team 1 — Recon & OSINT

Apresentação de seminário sobre reconhecimento e inteligência de fontes abertas, construída em Reveal.js com navegação **exclusivamente horizontal** e animações de interface para as demonstrações de Nmap e Wireshark.

> **Duração estimada:** 45 minutos + Q&A
>
> **Formato:** 54 slides, 16:9, gerados como uma página estática com Python 3.

---

## Equipe e divisão do conteúdo

| Integrante | Bloco | Slides |
| :--- | :--- | :---: |
| **Geovana** | Conceito e contexto · OpSec e fechamento | 03–09 · 49–52 |
| **Emilio** | Reconhecimento ativo · Nmap · Wireshark | 10–15 |
| **Daniel** | Reconhecimento passivo · OSINT | 16–40 |
| **João Pedro Gonçalves** | Estudos de caso — RSA e Strava | 41–44 |
| **João Pedro Almeida** | Demonstração — GEOSINT e OSINT | 45–48 |
| **Todos** | Capa, agenda, referências e Q&A | 01–02 · 53–54 |

---

## Roteiro da apresentação

| Bloco | Tema | Slides | Responsável |
| :---: | :--- | :---: | :--- |
| — | Capa e agenda | 01–02 | Todos |
| 01 | Era das mídias, caso Twitter, superexposição, Smart Sampa e conceito | 03–09 | Geovana |
| 02 | Reconhecimento ativo, redes, Nmap e Wireshark | 10–15 | Emilio |
| 03 | Recon passivo, ciclo de OSINT, técnicas físicas, ferramentas e ecossistema | 16–40 | Daniel |
| 04 | Estudos de caso: RSA SecurID e Strava | 41–44 | João Pedro Gonçalves |
| 05 | Demonstração: GEOSINT e grafo de OSINT | 45–48 | João Pedro Almeida |
| 06 | OpSec, hábitos e conclusão | 49–52 | Geovana |
| — | Referências e perguntas | 53–54 | Todos |

Cada slide possui **notas do orador** (`<aside class="notes">`) com pontos de fala, transições e cuidados de contextualização.

---

## Como executar

### Servidor local (recomendado)

Na raiz do projeto:

```bash
python3 -m http.server 8000
```

Acesse `http://localhost:8000/`.

O `index.html` da raiz é gerado e mantido no repositório, então pode ser servido diretamente. O servidor local é necessário para o modo de notas do orador em alguns navegadores.

### Editar e gerar

Edite os blocos em `slides/`; a ordem está em `slides/manifest.json`. O documento externo fica em `src/presentation.html`, o comportamento em `js/` e os estilos em `css/`. Não edite `index.html` diretamente: regenere-o após alterar os blocos ou o template.

```bash
python3 scripts/build.py
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
```

O primeiro comando atualiza `index.html` e monta `_site/`. Os demais conferem se o HTML gerado está atualizado, se os slides são horizontais e se os recursos necessários são publicados. Se `_site/` contiver um arquivo estranho à publicação, a geração para sem removê-lo.

Para testar também o tema e o Speaker View em um navegador, com Playwright e Chromium instalados e o servidor local ativo em `localhost:8791`, execute `node tests/theme_browser.cjs`. Use `TEST_URL` para outro endereço.

### Alternativas

```bash
npx serve .
```

Também é possível abrir `index.html` diretamente no navegador, mas o modo de notas e o carregamento de alguns recursos podem ser limitados por políticas de CORS.

---

## Deploy no GitHub Pages

O deploy é automático pelo workflow [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml), disparado em cada push para `main` ou manualmente pela aba **Actions**.

Na primeira configuração, acesse **Settings → Pages** no repositório e selecione **Source: GitHub Actions**. Depois disso, o site fica disponível em:

`https://jpedro-fsgs.github.io/IntroReconSeminario/`

O workflow valida o HTML gerado, executa os testes e monta `_site/` com `index.html`, `css/`, `js/`, `assets/` e `.nojekyll`. Os blocos-fonte e os roteiros não são publicados.

---

## Atalhos

| Tecla | Ação |
| :---: | :--- |
| `→` / `Espaço` | Próximo slide |
| `←` | Slide anterior |
| `S` | Modo do orador, com notas e cronômetro |
| `T` | Alternar entre os temas claro e escuro |
| `F` | Tela cheia |
| `O` / `Esc` | Visão geral dos slides |
| `B` / `.` | Pausa / tela preta |
| `Alt + clique` | Zoom no elemento clicado |

Após o slide **O kit de coleta**, os seis grupos de ferramentas são apresentados em slides horizontais comuns, com notas próprias.

Pressione **T** para alternar entre os modos claro e escuro, inclusive na janela de notas aberta com **S**. O tema é sincronizado com as prévias e as notas e lembrado no navegador quando o armazenamento local está disponível.

---

## Estrutura do projeto

```text
.
├── index.html                     # HTML gerado, servido localmente
├── src/presentation.html          # documento externo e ordem dos scripts
├── slides/
│   ├── manifest.json              # ordem explícita dos blocos
│   ├── 00-abertura.html           # capa e agenda
│   ├── 01-conceito-contexto.html
│   ├── 02-recon-ativo.html
│   ├── 03a-passivo-introducao.html
│   ├── 03b-ciclo-osint.html
│   ├── 03c-tecnicas-ferramentas.html
│   ├── 03c1-ferramentas-detalhes.html
│   ├── 03d-fisico-ecossistema.html
│   ├── 04-estudos-caso.html
│   ├── 05-geosint-osint.html
│   ├── 06-opsec-fechamento.html
│   └── 07-referencias-perguntas.html
├── css/
│   ├── main.css                   # imports na ordem original da cascata
│   ├── 01-base.css
│   ├── 02-contexto.css
│   ├── 03-ativo.css
│   ├── 04-passivo-casos.css
│   ├── 05-geosint-fechamento.css
│   ├── 06-reveal-movimento.css
│   ├── 07-tema.css                # modo claro da apresentação
│   └── 08-speaker-theme.css       # tema da janela de notas
├── js/
│   ├── reveal-init.js             # configuração e plugins do Reveal
│   └── theme.js                   # preferência e sincronização do tema
├── scripts/build.py               # montagem e validação sem dependências externas
├── tests/test_build.py            # testes da estrutura e publicação
├── assets/
│   ├── cinema.jpg                 # foto usada no post fictício do slide 07
│   ├── Estrategias-para-Lidar-com-o-Comportamento-Desafiador-das-Criancas-1024x683.jpg
│   └── twitter.svg                # ícone antigo do Twitter
├── Red Team 1 - Recon e OSINT.md  # roteiro-fonte e atribuições
└── README.md
```

O deck usa Reveal.js 5.1 via CDN e as fontes Instrument Serif, IBM Plex Sans e IBM Plex Mono via Google Fonts. A montagem usa apenas a biblioteca padrão do Python e gera HTML estático, sem buscar blocos de slides em tempo de execução.

---

## Notas técnicas

- **Navegação horizontal:** não há seções verticais aninhadas; `Reveal.slide(i)` percorre os 54 slides.
- **Animações:** as transições são ativadas pela classe `.present` que o Reveal adiciona ao slide atual. Isso faz as animações reiniciarem ao revisitar um slide.
- **Fallback visual:** o estado base dos elementos já é o estado final; sem JavaScript ou com animações desativadas, o conteúdo continua legível.
- **Acessibilidade:** `prefers-reduced-motion` desativa as animações e mantém o resultado final.
- **Dimensões:** canvas de 1280 × 720, `center: false`, transição `slide`.
- **Demonstrações:** Nmap, Wireshark e os exemplos do kit de coleta são simulações visuais, sem executar comandos reais ou consultar os serviços mostrados. Os dados dos exemplos são fictícios.
- **Dados sensíveis:** os casos e endereços usados são didáticos ou públicos; nenhum alvo real foi testado durante a apresentação.
- **Ícone do Twitter:** [Font Awesome Free 6.7.2](https://github.com/FortAwesome/Font-Awesome/blob/6.7.2/svgs/brands/twitter.svg), por Fonticons, Inc., sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

## Referências principais

- MITRE ATT&CK — [TA0043 Reconnaissance](https://attack.mitre.org/tactics/TA0043/)
- OWASP — [Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- Michael Bazzell — *Open Source Intelligence Techniques*, 9ª ed., 2022
- G1 — *Smart Sampa e as senhas expostas por 11 meses* (21 out. 2026)
- The Guardian — [Strava e as bases militares](https://www.theguardian.com/world/2018/jan/28)
- Zoho Workplace — [RSA spear-phishing attack](https://www.zoho.com/workplace/articles/rsa-spear-phishing-attack.html)
- [Nmap Reference Guide](https://nmap.org/book/man.html) · [Wireshark User's Guide](https://www.wireshark.org/docs/) · [Shodan](https://www.shodan.io/) · [Censys](https://censys.com/)

> Os casos foram resumidos para fins didáticos. Exposição não é o mesmo que invasão.
