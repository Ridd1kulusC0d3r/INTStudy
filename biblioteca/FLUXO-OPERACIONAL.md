# Fluxo operacional — da inteligência à resposta

> Como encadear as fontes abertas da biblioteca num ciclo de trabalho de SOC/CTI. Cada etapa aponta para a disciplina e para as fontes que a sustentam.

```
 1 INTELIGÊNCIA ──► 2 PRIORIZAÇÃO ──► 3 CAÇA E DETECÇÃO ──► 4 VALIDAÇÃO ──► 5 RESPOSTA
   (02 CTI)           (02 CTI)          (02 · 16 Dados)       (16 Dados)       (04 DFIR)
       ▲                                                                           │
       └───────────────────────── 6 FEEDBACK / LIÇÕES APRENDIDAS ◄─────────────────┘
```

## 1 · Inteligência — coletar e estruturar
- Entender o nível operacional e tático: **CREST — What is CTI and How is it Used?**
- Estruturar análise e difusão: **MISP — Best Practices in Threat Intelligence**.
- Padronizar relatórios: **CTI Blueprints** (MITRE CTID).
- Traduzir texto em técnicas: **TRAM** (sempre com revisão humana — ver [18](../disciplinas/18-ia-aplicada/)).
- Encadear comportamento: **Attack Flow**.
- Pivotar infraestrutura: **The Art of Pivoting**.

## 2 · Priorização — o que defender primeiro
- **Top ATT&CK Techniques** — prevalência, choke points e acionabilidade.
- **Sightings Ecosystem** — o que realmente é visto in the wild.
- Contexto BR/LATAM: cruzar com o `apt4all` e com o TCE (TIEM/AXIS).

## 3 · Caça e detecção — formular e testar hipóteses
- Método: **TTP-Based Hunting** (MITRE).
- Hipóteses e consultas por técnica: **Threat Hunter Playbook** (OTRF).
- Artefatos e palavras-chave por técnica: **ThreatHunting-Keywords**.

## 4 · Validação — provar que a detecção funciona
- Telemetria de ataques simulados: **Security Datasets** (OTRF).
- Laboratório: **HELK** (checar se o projeto está ativo antes de adotar).
- Medir falsos positivos e cobertura — ver [16 · Engenharia de Dados](../disciplinas/16-engenharia-de-dados/).

## 5 · Resposta — conter e erradicar
- De TTPs observados para contramedidas: **Playbook-NG** (CISA).
- Triagem Tier 1: **SOC Analyst Hub** (CraftedSignal).
- Playbooks de inteligência → ação: **MISP Playbooks**.
- Estudo de caso de ransomware: **MITRE — Ransomware Getting Started Guide and Deep Dive into REvil**.

## 6 · Feedback — fechar o ciclo
- Avaliar o programa como um todo: **CORA** e **11 Strategies of a World-Class SOC**.
- Registrar no `DIARIO.md` o que a detecção perdeu (Detecção pela Ausência).

## ▶ Próxima ação (uma só)
Escolher uma técnica do **Top ATT&CK Techniques**, abrir o playbook dela no **Threat Hunter Playbook** e rodar a consulta contra um dataset do **Security Datasets**.
