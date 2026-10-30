# Red Team 1 — Recon & OSINT

Apresentação de seminário sobre reconhecimento e inteligência de fontes abertas, construída em Reveal.js com navegação **exclusivamente horizontal** e animações de interface para as demonstrações de Nmap e Wireshark.

> **Duração estimada:** 45 minutos + Q&A
>
> **Formato:** 32 slides, 16:9, sem build e sem dependências locais além de um servidor HTTP simples.

---

## Equipe e divisão do conteúdo

| Integrante | Bloco | Slides |
| :--- | :--- | :---: |
| **Geovana** | Conceito e contexto · OpSec e fechamento | 03–06 · 27–30 |
| **Emilio** | Reconhecimento ativo · Nmap · Wireshark | 07–12 |
| **Daniel** | Reconhecimento passivo · OSINT | 13–18 |
| **João Pedro Gonçalves** | Estudos de caso — RSA e Strava | 19–22 |
| **João Pedro Almeida** | Demonstração — GEOSINT e OSINT | 23–26 |
| **Todos** | Capa, agenda, referências e Q&A | 01–02 · 31–32 |

---

## Roteiro da apresentação

| Bloco | Tema | Slides | Responsável |
| :---: | :--- | :---: | :--- |
| — | Capa e agenda | 01–02 | Todos |
| 01 | Conceito, superfície de ataque e caso Smart Sampa | 03–06 | Geovana |
| 02 | Reconhecimento ativo, redes, Nmap e Wireshark | 07–12 | Emilio |
| 03 | OSINT, técnicas passivas, ferramentas e ecossistema | 13–18 | Daniel |
| 04 | Estudos de caso: RSA SecurID e Strava | 19–22 | João Pedro Gonçalves |
| 05 | Demonstração: GEOSINT e grafo de OSINT | 23–26 | João Pedro Almeida |
| 06 | OpSec, hábitos e conclusão | 27–30 | Geovana |
| — | Referências e perguntas | 31–32 | Todos |

Cada slide possui **notas do orador** (`<aside class="notes">`) com pontos de fala, transições e cuidados de contextualização.

---

## Como executar

### Servidor local (recomendado)

Na raiz do projeto:

```bash
python3 -m http.server 8000
```

Acesse `http://localhost:8000/`.

O servidor local é necessário para o modo de notas do orador em alguns navegadores.

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

O workflow publica apenas `index.html`, `css/` e um `.nojekyll`, sem subir arquivos de desenvolvimento ou o roteiro em Markdown.

---

## Atalhos

| Tecla | Ação |
| :---: | :--- |
| `→` / `Espaço` | Próximo slide |
| `←` | Slide anterior |
| `S` | Modo do orador, com notas e cronômetro |
| `F` | Tela cheia |
| `O` / `Esc` | Visão geral dos slides |
| `B` / `.` | Pausa / tela preta |
| `Alt + clique` | Zoom no elemento clicado |

---

## Estrutura do projeto

```text
.
├── index.html                     # deck completo, 32 slides horizontais
├── css/
│   └── custom.css                 # identidade visual, componentes e animações
├── Red Team 1 - Recon e OSINT.md  # roteiro-fonte e atribuições
└── README.md
```

O deck usa Reveal.js 5.1 via CDN e as fontes Instrument Serif, IBM Plex Sans e IBM Plex Mono via Google Fonts. Não há etapa de compilação.

---

## Notas técnicas

- **Navegação horizontal:** não há seções verticais aninhadas; `Reveal.slide(i)` percorre os 32 slides.
- **Animações:** as transições são ativadas pela classe `.present` que o Reveal adiciona ao slide atual. Isso faz as animações reiniciarem ao revisitar um slide.
- **Fallback visual:** o estado base dos elementos já é o estado final; sem JavaScript ou com animações desativadas, o conteúdo continua legível.
- **Acessibilidade:** `prefers-reduced-motion` desativa as animações e mantém o resultado final.
- **Dimensões:** canvas de 1280 × 720, `center: false`, transição `slide`.
- **Demonstrações:** Nmap e Wireshark são simulações visuais em HTML/CSS/SVG, sem executar comandos reais ou tráfego de rede.
- **Dados sensíveis:** os casos e endereços usados são didáticos ou públicos; nenhum alvo real foi testado durante a apresentação.

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
